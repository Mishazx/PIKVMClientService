import logging
import json
import threading
import time
import ssl
import websocket
import pymongo
from datetime import datetime, timezone
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from settings import settings
from controllers.pikvm import PikvmController
from controllers.WebSocket import PikvmWebSocketClient
from grpc_server import serve as grpc_serve

class MongoDBHandler:
    def __init__(self, settings):
        """
        Initialize MongoDB connection
        
        :param settings: PikvmSettings instance
        """
        self.client = None
        self.db = None
        self.collection = None
        self.is_connected = False

        try:
            # Create MongoDB client
            self.client = pymongo.MongoClient(settings.mongodb_uri, 
                                              serverSelectionTimeoutMS=5000,  # 5 seconds timeout
                                              connectTimeoutMS=5000)  # 5 seconds connection timeout
            
            # Test connection
            self.client.admin.command('ismaster')
            
            # Select database and collection
            self.db = self.client[settings.mongodb_database]
            self.collection = self.db[settings.mongodb_collection]
            
            self.is_connected = True
            logging.info("MongoDB connection established successfully")
        except pymongo.errors.ConnectionFailure as e:
            logging.warning(f"Could not connect to MongoDB: {e}. Continuing without database.")
        except Exception as e:
            logging.warning(f"Unexpected error connecting to MongoDB: {e}. Continuing without database.")

    def save_websocket_event(self, event_data):
        """
        Save WebSocket event to MongoDB
        
        :param event_data: Dictionary containing event information
        """
        if not self.is_connected:
            logging.debug("MongoDB not connected. Skipping event save.")
            return

        try:
            # Add timezone-aware timestamp to the event
            event_data['timestamp'] = datetime.now(timezone.utc)
            
            # Insert event into collection
            result = self.collection.insert_one(event_data)
            logging.debug(f"Saved event to MongoDB. Insert ID: {result.inserted_id}")
        except Exception as e:
            logging.error(f"Failed to save event to MongoDB: {e}")

    def close(self):
        """
        Close MongoDB connection
        """
        if self.client:
            try:
                self.client.close()
                logging.info("MongoDB connection closed")
            except Exception as e:
                logging.warning(f"Error closing MongoDB connection: {e}")
            finally:
                self.is_connected = False

def start_websocket_client(controller, mongodb_handler):
    """
    Start WebSocket client in a separate thread
    
    :param controller: PiKVM controller instance
    :param mongodb_handler: MongoDB handler instance
    """
    try:
        websocket_client = PikvmWebSocketClient(controller, mongodb_handler)
        websocket_thread = threading.Thread(target=websocket_client.connect)
        websocket_thread.daemon = True
        websocket_thread.start()
        logging.info("WebSocket client started successfully")
        return websocket_thread
    except Exception as e:
        logging.error(f"Failed to start WebSocket client: {e}")
        return None

def start_grpc_server():
    """
    Start gRPC server in a separate thread
    """
    try:
        grpc_thread = threading.Thread(target=grpc_serve)
        grpc_thread.daemon = True
        grpc_thread.start()
        logging.info("gRPC server started successfully on port 50051")
        return grpc_thread
    except Exception as e:
        logging.error(f"Failed to start gRPC server: {e}")
        return None

def main():
    try:
        # Enable WebSocket debug logging if debug mode is on
        if settings.debug:
            websocket.enableTrace(True)
        
        # Create controller using global settings
        controller = PikvmController()
        logging.info("PikvmController initialized successfully")
        
        # Initialize MongoDB handler
        mongodb_handler = MongoDBHandler(settings)
        
        # Test HTTP connection first
        http_status = controller.test_http_connect()
        logging.info(f"HTTP Connection Status: {http_status}")
        
        # Start WebSocket client
        websocket_thread = start_websocket_client(controller, mongodb_handler)
        
        # Start gRPC server
        grpc_thread = start_grpc_server()
        
        # Main thread loop
        while True:
            try:
                # Periodic health checks or additional logic can be added here
                time.sleep(60)
                
                # Check thread health
                if websocket_thread and not websocket_thread.is_alive():
                    logging.warning("WebSocket thread died. Attempting restart...")
                    websocket_thread = start_websocket_client(controller, mongodb_handler)
                
                if grpc_thread and not grpc_thread.is_alive():
                    logging.warning("gRPC server thread died. Attempting restart...")
                    grpc_thread = start_grpc_server()
            
            except KeyboardInterrupt:
                logging.info("Received keyboard interrupt. Shutting down...")
                break
            except Exception as loop_error:
                logging.error(f"Error in main loop: {loop_error}")
                time.sleep(5)  # Prevent rapid error logging
    
    except Exception as e:
        logging.critical(f"Critical error in main application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
