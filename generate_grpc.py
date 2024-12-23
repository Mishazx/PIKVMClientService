import os
import sys
from grpc_tools import protoc

def generate_grpc_code():
    # Paths
    proto_dir = os.path.join(os.path.dirname(__file__), 'protos')
    output_dir = os.path.join(os.path.dirname(__file__))

    # Ensure output directories exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate gRPC code
    protoc.main((
        '',
        f'-I{proto_dir}',
        f'--python_out={output_dir}',
        f'--grpc_python_out={output_dir}',
        'pikvm_service.proto'
    ))

    # Rename generated files to match Python import conventions
    os.rename(
        os.path.join(output_dir, 'pikvm_service_pb2.py'),
        os.path.join(output_dir, 'pikvm_service_pb2.py')
    )
    os.rename(
        os.path.join(output_dir, 'pikvm_service_pb2_grpc.py'),
        os.path.join(output_dir, 'pikvm_service_pb2_grpc.py')
    )

    print("gRPC code generated successfully!")

if __name__ == '__main__':
    generate_grpc_code()
