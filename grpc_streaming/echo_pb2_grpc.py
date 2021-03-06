# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import echo_pb2 as echo__pb2


class EchoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.reverse = channel.stream_stream(
        '/Echo/reverse',
        request_serializer=echo__pb2.Message.SerializeToString,
        response_deserializer=echo__pb2.Message.FromString,
        )


class EchoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def reverse(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'reverse': grpc.stream_stream_rpc_method_handler(
          servicer.reverse,
          request_deserializer=echo__pb2.Message.FromString,
          response_serializer=echo__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Echo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
