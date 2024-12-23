# PIKVM Client Service gRPC Microservice

## Overview
This microservice provides a gRPC interface for controlling a PI-KVM device. It offers a robust and type-safe way to interact with PI-KVM's various APIs.

## Setup and Installation

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate gRPC Code
```bash
python generate_grpc.py
```

### 4. Start gRPC Server
```bash
python Services/grpc_server.py
```

## Using the gRPC Service

### From Another Service
1. Install the same `requirements.txt`
2. Generate gRPC code using `generate_grpc.py`
3. Use the client example as a reference

### Client Example
```python
import grpc
import pikvm_service_pb2
import pikvm_service_pb2_grpc

# Create channel
channel = grpc.insecure_channel('localhost:50051')
stub = pikvm_service_pb2_grpc.PikvmControlServiceStub(channel)

# Power on example
response = stub.PowerControl(
    pikvm_service_pb2.PowerControlRequest(
        action=pikvm_service_pb2.ON,
        wait=True
    )
)
print(response.success, response.message)
```

## Environment Variables
- `PIKVM_HOST`: PI-KVM device hostname/IP
- `PIKVM_USERNAME`: Authentication username
- `PIKVM_PASSWORD`: Authentication password

## Security Considerations
- Current implementation uses an insecure channel
- For production, implement SSL/TLS
- Use authentication mechanisms

## Supported Operations
- Power Control
- Button Click
- MSD Image Upload
- GPIO Switching
- GPIO Pulsing

## Troubleshooting
- Ensure gRPC code is generated before running
- Check network connectivity
- Verify environment variables
