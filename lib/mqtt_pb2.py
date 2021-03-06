# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mqtt.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmqtt.proto\x12\x0cMQTTFunction\"9\n\nComingData\x12\r\n\x05Topic\x18\x01 \x01(\t\x12\x0f\n\x07Payload\x18\x02 \x01(\t\x12\x0b\n\x03Qos\x18\x03 \x01(\x05\"9\n\nReturnType\x12+\n\x0e\x41\x63knowledgment\x18\x01 \x01(\x0e\x32\x13.MQTTFunction.state*\xed\x01\n\x05state\x12\x12\n\x0ePublishSuccess\x10\x00\x12\x13\n\x0fPublish_Success\x10\x01\x12\x11\n\rPublishFailed\x10\x02\x12\x12\n\x0e\x43onnexion_Lost\x10\x03\x12\x18\n\x14\x43lient_NOT_Connected\x10\x04\x12\x14\n\x10\x43lient_Connected\x10\x05\x12\x1b\n\x17Incorrect_Proto_Version\x10\x06\x12\x11\n\rBad_Client_ID\x10\x07\x12\x15\n\x11Server_Unvailable\x10\x08\x12\x0f\n\x0b\x42\x61\x64_User_Pw\x10\t\x12\x0c\n\x08Not_AUTH\x10\n2V\n\x0bMQTTManager\x12G\n\x0fPublishMessages\x12\x18.MQTTFunction.ComingData\x1a\x18.MQTTFunction.ReturnType\"\x00\x62\x06proto3')

_STATE = DESCRIPTOR.enum_types_by_name['state']
state = enum_type_wrapper.EnumTypeWrapper(_STATE)
PublishSuccess = 0
Publish_Success = 1
PublishFailed = 2
Connexion_Lost = 3
Client_NOT_Connected = 4
Client_Connected = 5
Incorrect_Proto_Version = 6
Bad_Client_ID = 7
Server_Unvailable = 8
Bad_User_Pw = 9
Not_AUTH = 10


_COMINGDATA = DESCRIPTOR.message_types_by_name['ComingData']
_RETURNTYPE = DESCRIPTOR.message_types_by_name['ReturnType']
ComingData = _reflection.GeneratedProtocolMessageType('ComingData', (_message.Message,), {
  'DESCRIPTOR' : _COMINGDATA,
  '__module__' : 'mqtt_pb2'
  # @@protoc_insertion_point(class_scope:MQTTFunction.ComingData)
  })
_sym_db.RegisterMessage(ComingData)

ReturnType = _reflection.GeneratedProtocolMessageType('ReturnType', (_message.Message,), {
  'DESCRIPTOR' : _RETURNTYPE,
  '__module__' : 'mqtt_pb2'
  # @@protoc_insertion_point(class_scope:MQTTFunction.ReturnType)
  })
_sym_db.RegisterMessage(ReturnType)

_MQTTMANAGER = DESCRIPTOR.services_by_name['MQTTManager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATE._serialized_start=147
  _STATE._serialized_end=384
  _COMINGDATA._serialized_start=28
  _COMINGDATA._serialized_end=85
  _RETURNTYPE._serialized_start=87
  _RETURNTYPE._serialized_end=144
  _MQTTMANAGER._serialized_start=386
  _MQTTMANAGER._serialized_end=472
# @@protoc_insertion_point(module_scope)
