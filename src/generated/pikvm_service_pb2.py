# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pikvm_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'pikvm_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13pikvm_service.proto\x12\x05pikvm\"\x8f\x01\n\x13PowerControlRequest\x12\x31\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32!.pikvm.PowerControlRequest.Action\x12\x0c\n\x04wait\x18\x02 \x01(\x08\"7\n\x06\x41\x63tion\x12\x06\n\x02ON\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0c\n\x08OFF_HARD\x10\x02\x12\x0e\n\nRESET_HARD\x10\x03\"\x84\x01\n\x12\x42uttonClickRequest\x12\x30\n\x06\x62utton\x18\x01 \x01(\x0e\x32 .pikvm.ButtonClickRequest.Button\x12\x0c\n\x04wait\x18\x02 \x01(\x08\".\n\x06\x42utton\x12\t\n\x05POWER\x10\x00\x12\x0e\n\nPOWER_LONG\x10\x01\x12\t\n\x05RESET\x10\x02\":\n\x10MSDUploadRequest\x12\x12\n\nimage_path\x18\x01 \x01(\t\x12\x12\n\nimage_name\x18\x02 \x01(\t\"W\n\x12GPIOControlRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\x05\x12\x0c\n\x04wait\x18\x03 \x01(\x08\x12\x13\n\x0bpulse_delay\x18\x04 \x01(\x02\"3\n\x0f\x43ommandResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xe9\x02\n\x13PikvmControlService\x12\x44\n\x0cPowerControl\x12\x1a.pikvm.PowerControlRequest\x1a\x16.pikvm.CommandResponse\"\x00\x12\x42\n\x0b\x42uttonClick\x12\x19.pikvm.ButtonClickRequest\x1a\x16.pikvm.CommandResponse\"\x00\x12\x43\n\x0eUploadMSDImage\x12\x17.pikvm.MSDUploadRequest\x1a\x16.pikvm.CommandResponse\"\x00\x12\x41\n\nSwitchGPIO\x12\x19.pikvm.GPIOControlRequest\x1a\x16.pikvm.CommandResponse\"\x00\x12@\n\tPulseGPIO\x12\x19.pikvm.GPIOControlRequest\x1a\x16.pikvm.CommandResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pikvm_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_POWERCONTROLREQUEST']._serialized_start=31
  _globals['_POWERCONTROLREQUEST']._serialized_end=174
  _globals['_POWERCONTROLREQUEST_ACTION']._serialized_start=119
  _globals['_POWERCONTROLREQUEST_ACTION']._serialized_end=174
  _globals['_BUTTONCLICKREQUEST']._serialized_start=177
  _globals['_BUTTONCLICKREQUEST']._serialized_end=309
  _globals['_BUTTONCLICKREQUEST_BUTTON']._serialized_start=263
  _globals['_BUTTONCLICKREQUEST_BUTTON']._serialized_end=309
  _globals['_MSDUPLOADREQUEST']._serialized_start=311
  _globals['_MSDUPLOADREQUEST']._serialized_end=369
  _globals['_GPIOCONTROLREQUEST']._serialized_start=371
  _globals['_GPIOCONTROLREQUEST']._serialized_end=458
  _globals['_COMMANDRESPONSE']._serialized_start=460
  _globals['_COMMANDRESPONSE']._serialized_end=511
  _globals['_PIKVMCONTROLSERVICE']._serialized_start=514
  _globals['_PIKVMCONTROLSERVICE']._serialized_end=875
# @@protoc_insertion_point(module_scope)