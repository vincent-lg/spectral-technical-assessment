# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collector.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63ollector.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\r\n\x0b\x44\x61taRequest\"J\n\x0f\x45lectricalState\x12(\n\x04step\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05meter\x18\x02 \x01(\x02\"2\n\x0e\x45lectricalData\x12 \n\x06states\x18\x01 \x03(\x0b\x32\x10.ElectricalState2C\n\rDataCollector\x12\x32\n\x07\x43ollect\x12\x16.google.protobuf.Empty\x1a\x0f.ElectricalDatab\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DATAREQUEST = _descriptor.Descriptor(
  name='DataRequest',
  full_name='DataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=94,
)


_ELECTRICALSTATE = _descriptor.Descriptor(
  name='ElectricalState',
  full_name='ElectricalState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='ElectricalState.step', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meter', full_name='ElectricalState.meter', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=170,
)


_ELECTRICALDATA = _descriptor.Descriptor(
  name='ElectricalData',
  full_name='ElectricalData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='states', full_name='ElectricalData.states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=222,
)

_ELECTRICALSTATE.fields_by_name['step'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ELECTRICALDATA.fields_by_name['states'].message_type = _ELECTRICALSTATE
DESCRIPTOR.message_types_by_name['DataRequest'] = _DATAREQUEST
DESCRIPTOR.message_types_by_name['ElectricalState'] = _ELECTRICALSTATE
DESCRIPTOR.message_types_by_name['ElectricalData'] = _ELECTRICALDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUEST,
  '__module__' : 'collector_pb2'
  # @@protoc_insertion_point(class_scope:DataRequest)
  })
_sym_db.RegisterMessage(DataRequest)

ElectricalState = _reflection.GeneratedProtocolMessageType('ElectricalState', (_message.Message,), {
  'DESCRIPTOR' : _ELECTRICALSTATE,
  '__module__' : 'collector_pb2'
  # @@protoc_insertion_point(class_scope:ElectricalState)
  })
_sym_db.RegisterMessage(ElectricalState)

ElectricalData = _reflection.GeneratedProtocolMessageType('ElectricalData', (_message.Message,), {
  'DESCRIPTOR' : _ELECTRICALDATA,
  '__module__' : 'collector_pb2'
  # @@protoc_insertion_point(class_scope:ElectricalData)
  })
_sym_db.RegisterMessage(ElectricalData)



_DATACOLLECTOR = _descriptor.ServiceDescriptor(
  name='DataCollector',
  full_name='DataCollector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=224,
  serialized_end=291,
  methods=[
  _descriptor.MethodDescriptor(
    name='Collect',
    full_name='DataCollector.Collect',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ELECTRICALDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATACOLLECTOR)

DESCRIPTOR.services_by_name['DataCollector'] = _DATACOLLECTOR

# @@protoc_insertion_point(module_scope)