# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"V\n\x04User\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12 \n\x06status\x18\x03 \x01(\x0e\x32\x10.user.UserStatus\x12\x12\n\nhobby_list\x18\x04 \x03(\t\"\x19\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\r\"H\n\x0cUserResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x04user\x18\x03 \x01(\x0b\x32\n.user.User*0\n\nUserStatus\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x32;\n\x0bUserService\x12,\n\x03get\x12\x11.user.UserRequest\x1a\x12.user.UserResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERSTATUS._serialized_start=209
  _USERSTATUS._serialized_end=257
  _USER._serialized_start=20
  _USER._serialized_end=106
  _USERREQUEST._serialized_start=108
  _USERREQUEST._serialized_end=133
  _USERRESPONSE._serialized_start=135
  _USERRESPONSE._serialized_end=207
  _USERSERVICE._serialized_start=259
  _USERSERVICE._serialized_end=318
# @@protoc_insertion_point(module_scope)
