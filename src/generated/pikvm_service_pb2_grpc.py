# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pikvm_service_pb2 as pikvm__service__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pikvm_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PikvmControlServiceStub(object):
    """Service for controlling PI-KVM device
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PowerControl = channel.unary_unary(
                '/pikvm.PikvmControlService/PowerControl',
                request_serializer=pikvm__service__pb2.PowerControlRequest.SerializeToString,
                response_deserializer=pikvm__service__pb2.CommandResponse.FromString,
                _registered_method=True)
        self.ButtonClick = channel.unary_unary(
                '/pikvm.PikvmControlService/ButtonClick',
                request_serializer=pikvm__service__pb2.ButtonClickRequest.SerializeToString,
                response_deserializer=pikvm__service__pb2.CommandResponse.FromString,
                _registered_method=True)
        self.UploadMSDImage = channel.unary_unary(
                '/pikvm.PikvmControlService/UploadMSDImage',
                request_serializer=pikvm__service__pb2.MSDUploadRequest.SerializeToString,
                response_deserializer=pikvm__service__pb2.CommandResponse.FromString,
                _registered_method=True)
        self.SwitchGPIO = channel.unary_unary(
                '/pikvm.PikvmControlService/SwitchGPIO',
                request_serializer=pikvm__service__pb2.GPIOControlRequest.SerializeToString,
                response_deserializer=pikvm__service__pb2.CommandResponse.FromString,
                _registered_method=True)
        self.PulseGPIO = channel.unary_unary(
                '/pikvm.PikvmControlService/PulseGPIO',
                request_serializer=pikvm__service__pb2.GPIOControlRequest.SerializeToString,
                response_deserializer=pikvm__service__pb2.CommandResponse.FromString,
                _registered_method=True)


class PikvmControlServiceServicer(object):
    """Service for controlling PI-KVM device
    """

    def PowerControl(self, request, context):
        """Power control methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ButtonClick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadMSDImage(self, request, context):
        """Media and storage methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchGPIO(self, request, context):
        """GPIO control methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PulseGPIO(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PikvmControlServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PowerControl': grpc.unary_unary_rpc_method_handler(
                    servicer.PowerControl,
                    request_deserializer=pikvm__service__pb2.PowerControlRequest.FromString,
                    response_serializer=pikvm__service__pb2.CommandResponse.SerializeToString,
            ),
            'ButtonClick': grpc.unary_unary_rpc_method_handler(
                    servicer.ButtonClick,
                    request_deserializer=pikvm__service__pb2.ButtonClickRequest.FromString,
                    response_serializer=pikvm__service__pb2.CommandResponse.SerializeToString,
            ),
            'UploadMSDImage': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadMSDImage,
                    request_deserializer=pikvm__service__pb2.MSDUploadRequest.FromString,
                    response_serializer=pikvm__service__pb2.CommandResponse.SerializeToString,
            ),
            'SwitchGPIO': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchGPIO,
                    request_deserializer=pikvm__service__pb2.GPIOControlRequest.FromString,
                    response_serializer=pikvm__service__pb2.CommandResponse.SerializeToString,
            ),
            'PulseGPIO': grpc.unary_unary_rpc_method_handler(
                    servicer.PulseGPIO,
                    request_deserializer=pikvm__service__pb2.GPIOControlRequest.FromString,
                    response_serializer=pikvm__service__pb2.CommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pikvm.PikvmControlService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pikvm.PikvmControlService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PikvmControlService(object):
    """Service for controlling PI-KVM device
    """

    @staticmethod
    def PowerControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pikvm.PikvmControlService/PowerControl',
            pikvm__service__pb2.PowerControlRequest.SerializeToString,
            pikvm__service__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ButtonClick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pikvm.PikvmControlService/ButtonClick',
            pikvm__service__pb2.ButtonClickRequest.SerializeToString,
            pikvm__service__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UploadMSDImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pikvm.PikvmControlService/UploadMSDImage',
            pikvm__service__pb2.MSDUploadRequest.SerializeToString,
            pikvm__service__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SwitchGPIO(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pikvm.PikvmControlService/SwitchGPIO',
            pikvm__service__pb2.GPIOControlRequest.SerializeToString,
            pikvm__service__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PulseGPIO(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pikvm.PikvmControlService/PulseGPIO',
            pikvm__service__pb2.GPIOControlRequest.SerializeToString,
            pikvm__service__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)