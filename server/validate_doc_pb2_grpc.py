# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import validate_doc_pb2 as validate__doc__pb2


class validatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OrderDocument = channel.unary_unary(
                '/validator/OrderDocument',
                request_serializer=validate__doc__pb2.DocumentResquest.SerializeToString,
                response_deserializer=validate__doc__pb2.DocumentResponse.FromString,
                )


class validatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OrderDocument(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_validatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OrderDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderDocument,
                    request_deserializer=validate__doc__pb2.DocumentResquest.FromString,
                    response_serializer=validate__doc__pb2.DocumentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'validator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class validator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OrderDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/validator/OrderDocument',
            validate__doc__pb2.DocumentResquest.SerializeToString,
            validate__doc__pb2.DocumentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
