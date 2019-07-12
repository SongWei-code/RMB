# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aster/protos/feature_extractor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aster.protos import convnet_pb2 as aster_dot_protos_dot_convnet__pb2
from aster.protos import bidirectional_rnn_pb2 as aster_dot_protos_dot_bidirectional__rnn__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aster/protos/feature_extractor.proto',
  package='aster.protos',
  syntax='proto2',
  serialized_pb=_b('\n$aster/protos/feature_extractor.proto\x12\x0c\x61ster.protos\x1a\x1a\x61ster/protos/convnet.proto\x1a$aster/protos/bidirectional_rnn.proto\"\x9b\x01\n\x10\x46\x65\x61tureExtractor\x12&\n\x07\x63onvnet\x18\x01 \x01(\x0b\x32\x15.aster.protos.Convnet\x12\x39\n\x11\x62idirectional_rnn\x18\x02 \x03(\x0b\x32\x1e.aster.protos.BidirectionalRnn\x12$\n\x15summarize_activations\x18\x03 \x01(\x08:\x05\x66\x61lse')
  ,
  dependencies=[aster_dot_protos_dot_convnet__pb2.DESCRIPTOR,aster_dot_protos_dot_bidirectional__rnn__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FEATUREEXTRACTOR = _descriptor.Descriptor(
  name='FeatureExtractor',
  full_name='aster.protos.FeatureExtractor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convnet', full_name='aster.protos.FeatureExtractor.convnet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidirectional_rnn', full_name='aster.protos.FeatureExtractor.bidirectional_rnn', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summarize_activations', full_name='aster.protos.FeatureExtractor.summarize_activations', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=276,
)

_FEATUREEXTRACTOR.fields_by_name['convnet'].message_type = aster_dot_protos_dot_convnet__pb2._CONVNET
_FEATUREEXTRACTOR.fields_by_name['bidirectional_rnn'].message_type = aster_dot_protos_dot_bidirectional__rnn__pb2._BIDIRECTIONALRNN
DESCRIPTOR.message_types_by_name['FeatureExtractor'] = _FEATUREEXTRACTOR

FeatureExtractor = _reflection.GeneratedProtocolMessageType('FeatureExtractor', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREEXTRACTOR,
  __module__ = 'aster.protos.feature_extractor_pb2'
  # @@protoc_insertion_point(class_scope:aster.protos.FeatureExtractor)
  ))
_sym_db.RegisterMessage(FeatureExtractor)


# @@protoc_insertion_point(module_scope)
