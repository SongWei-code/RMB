# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aster/protos/predictor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aster.protos import rnn_cell_pb2 as aster_dot_protos_dot_rnn__cell__pb2
from aster.protos import hyperparams_pb2 as aster_dot_protos_dot_hyperparams__pb2
from aster.protos import label_map_pb2 as aster_dot_protos_dot_label__map__pb2
from aster.protos import loss_pb2 as aster_dot_protos_dot_loss__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aster/protos/predictor.proto',
  package='aster.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x61ster/protos/predictor.proto\x12\x0c\x61ster.protos\x1a\x1b\x61ster/protos/rnn_cell.proto\x1a\x1e\x61ster/protos/hyperparams.proto\x1a\x1c\x61ster/protos/label_map.proto\x1a\x17\x61ster/protos/loss.proto\"\xad\x01\n\tPredictor\x12\x17\n\x04name\x18\x01 \x01(\t:\tPredictor\x12?\n\x13\x61ttention_predictor\x18\x02 \x01(\x0b\x32 .aster.protos.AttentionPredictorH\x00\x12\x33\n\rctc_predictor\x18\x03 \x01(\x0b\x32\x1a.aster.protos.CtcPredictorH\x00\x42\x11\n\x0fpredictor_oneof\"\x97\x03\n\x12\x41ttentionPredictor\x12\'\n\x08rnn_cell\x18\x01 \x01(\x0b\x32\x15.aster.protos.RnnCell\x12\x32\n\x0frnn_regularizer\x18\x02 \x01(\x0b\x32\x19.aster.protos.Regularizer\x12 \n\x13num_attention_units\x18\x03 \x01(\x05:\x03\x31\x32\x38\x12\x19\n\rmax_num_steps\x18\x04 \x01(\x05:\x02\x34\x30\x12\x1e\n\x0fmulti_attention\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x15\n\nbeam_width\x18\x06 \x01(\x05:\x01\x31\x12\x16\n\x07reverse\x18\x07 \x01(\x08:\x05\x66\x61lse\x12)\n\tlabel_map\x18\x08 \x01(\x0b\x32\x16.aster.protos.LabelMap\x12 \n\x04loss\x18\t \x01(\x0b\x32\x12.aster.protos.Loss\x12\x37\n\x0blm_rnn_cell\x18\n \x01(\x0b\x32\".aster.protos.LanguageModelRnnCell\x12\x12\n\x04sync\x18\x0b \x01(\x08:\x04true\"W\n\x14LanguageModelRnnCell\x12\'\n\x08rnn_cell\x18\x01 \x03(\x0b\x32\x15.aster.protos.RnnCell\x12\x16\n\x0crestore_path\x18\x02 \x01(\t:\x00\"\x0e\n\x0c\x43tcPredictor')
  ,
  dependencies=[aster_dot_protos_dot_rnn__cell__pb2.DESCRIPTOR,aster_dot_protos_dot_hyperparams__pb2.DESCRIPTOR,aster_dot_protos_dot_label__map__pb2.DESCRIPTOR,aster_dot_protos_dot_loss__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PREDICTOR = _descriptor.Descriptor(
  name='Predictor',
  full_name='aster.protos.Predictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='aster.protos.Predictor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("Predictor").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attention_predictor', full_name='aster.protos.Predictor.attention_predictor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctc_predictor', full_name='aster.protos.Predictor.ctc_predictor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='predictor_oneof', full_name='aster.protos.Predictor.predictor_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=163,
  serialized_end=336,
)


_ATTENTIONPREDICTOR = _descriptor.Descriptor(
  name='AttentionPredictor',
  full_name='aster.protos.AttentionPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rnn_cell', full_name='aster.protos.AttentionPredictor.rnn_cell', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rnn_regularizer', full_name='aster.protos.AttentionPredictor.rnn_regularizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_attention_units', full_name='aster.protos.AttentionPredictor.num_attention_units', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=128,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_num_steps', full_name='aster.protos.AttentionPredictor.max_num_steps', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=40,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_attention', full_name='aster.protos.AttentionPredictor.multi_attention', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beam_width', full_name='aster.protos.AttentionPredictor.beam_width', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse', full_name='aster.protos.AttentionPredictor.reverse', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_map', full_name='aster.protos.AttentionPredictor.label_map', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss', full_name='aster.protos.AttentionPredictor.loss', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lm_rnn_cell', full_name='aster.protos.AttentionPredictor.lm_rnn_cell', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync', full_name='aster.protos.AttentionPredictor.sync', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=339,
  serialized_end=746,
)


_LANGUAGEMODELRNNCELL = _descriptor.Descriptor(
  name='LanguageModelRnnCell',
  full_name='aster.protos.LanguageModelRnnCell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rnn_cell', full_name='aster.protos.LanguageModelRnnCell.rnn_cell', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restore_path', full_name='aster.protos.LanguageModelRnnCell.restore_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  serialized_start=748,
  serialized_end=835,
)


_CTCPREDICTOR = _descriptor.Descriptor(
  name='CtcPredictor',
  full_name='aster.protos.CtcPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=837,
  serialized_end=851,
)

_PREDICTOR.fields_by_name['attention_predictor'].message_type = _ATTENTIONPREDICTOR
_PREDICTOR.fields_by_name['ctc_predictor'].message_type = _CTCPREDICTOR
_PREDICTOR.oneofs_by_name['predictor_oneof'].fields.append(
  _PREDICTOR.fields_by_name['attention_predictor'])
_PREDICTOR.fields_by_name['attention_predictor'].containing_oneof = _PREDICTOR.oneofs_by_name['predictor_oneof']
_PREDICTOR.oneofs_by_name['predictor_oneof'].fields.append(
  _PREDICTOR.fields_by_name['ctc_predictor'])
_PREDICTOR.fields_by_name['ctc_predictor'].containing_oneof = _PREDICTOR.oneofs_by_name['predictor_oneof']
_ATTENTIONPREDICTOR.fields_by_name['rnn_cell'].message_type = aster_dot_protos_dot_rnn__cell__pb2._RNNCELL
_ATTENTIONPREDICTOR.fields_by_name['rnn_regularizer'].message_type = aster_dot_protos_dot_hyperparams__pb2._REGULARIZER
_ATTENTIONPREDICTOR.fields_by_name['label_map'].message_type = aster_dot_protos_dot_label__map__pb2._LABELMAP
_ATTENTIONPREDICTOR.fields_by_name['loss'].message_type = aster_dot_protos_dot_loss__pb2._LOSS
_ATTENTIONPREDICTOR.fields_by_name['lm_rnn_cell'].message_type = _LANGUAGEMODELRNNCELL
_LANGUAGEMODELRNNCELL.fields_by_name['rnn_cell'].message_type = aster_dot_protos_dot_rnn__cell__pb2._RNNCELL
DESCRIPTOR.message_types_by_name['Predictor'] = _PREDICTOR
DESCRIPTOR.message_types_by_name['AttentionPredictor'] = _ATTENTIONPREDICTOR
DESCRIPTOR.message_types_by_name['LanguageModelRnnCell'] = _LANGUAGEMODELRNNCELL
DESCRIPTOR.message_types_by_name['CtcPredictor'] = _CTCPREDICTOR

Predictor = _reflection.GeneratedProtocolMessageType('Predictor', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTOR,
  __module__ = 'aster.protos.predictor_pb2'
  # @@protoc_insertion_point(class_scope:aster.protos.Predictor)
  ))
_sym_db.RegisterMessage(Predictor)

AttentionPredictor = _reflection.GeneratedProtocolMessageType('AttentionPredictor', (_message.Message,), dict(
  DESCRIPTOR = _ATTENTIONPREDICTOR,
  __module__ = 'aster.protos.predictor_pb2'
  # @@protoc_insertion_point(class_scope:aster.protos.AttentionPredictor)
  ))
_sym_db.RegisterMessage(AttentionPredictor)

LanguageModelRnnCell = _reflection.GeneratedProtocolMessageType('LanguageModelRnnCell', (_message.Message,), dict(
  DESCRIPTOR = _LANGUAGEMODELRNNCELL,
  __module__ = 'aster.protos.predictor_pb2'
  # @@protoc_insertion_point(class_scope:aster.protos.LanguageModelRnnCell)
  ))
_sym_db.RegisterMessage(LanguageModelRnnCell)

CtcPredictor = _reflection.GeneratedProtocolMessageType('CtcPredictor', (_message.Message,), dict(
  DESCRIPTOR = _CTCPREDICTOR,
  __module__ = 'aster.protos.predictor_pb2'
  # @@protoc_insertion_point(class_scope:aster.protos.CtcPredictor)
  ))
_sym_db.RegisterMessage(CtcPredictor)


# @@protoc_insertion_point(module_scope)
