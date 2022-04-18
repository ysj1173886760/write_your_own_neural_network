# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import common_pb2 as common__pb2
from . import parameter_server_pb2 as parameter__server__pb2


class ParameterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VariableWeightsInit = channel.unary_unary(
                '/ParameterService/VariableWeightsInit',
                request_serializer=common__pb2.VariableWeightsReqResp.SerializeToString,
                response_deserializer=common__pb2.VariableWeightsReqResp.FromString,
                )
        self.Push = channel.unary_unary(
                '/ParameterService/Push',
                request_serializer=parameter__server__pb2.ParameterPushReq.SerializeToString,
                response_deserializer=parameter__server__pb2.ParameterPushResp.FromString,
                )
        self.Pull = channel.unary_unary(
                '/ParameterService/Pull',
                request_serializer=parameter__server__pb2.ParameterPullReq.SerializeToString,
                response_deserializer=parameter__server__pb2.ParameterPullResp.FromString,
                )


class ParameterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VariableWeightsInit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Push(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pull(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ParameterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VariableWeightsInit': grpc.unary_unary_rpc_method_handler(
                    servicer.VariableWeightsInit,
                    request_deserializer=common__pb2.VariableWeightsReqResp.FromString,
                    response_serializer=common__pb2.VariableWeightsReqResp.SerializeToString,
            ),
            'Push': grpc.unary_unary_rpc_method_handler(
                    servicer.Push,
                    request_deserializer=parameter__server__pb2.ParameterPushReq.FromString,
                    response_serializer=parameter__server__pb2.ParameterPushResp.SerializeToString,
            ),
            'Pull': grpc.unary_unary_rpc_method_handler(
                    servicer.Pull,
                    request_deserializer=parameter__server__pb2.ParameterPullReq.FromString,
                    response_serializer=parameter__server__pb2.ParameterPullResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ParameterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ParameterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VariableWeightsInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParameterService/VariableWeightsInit',
            common__pb2.VariableWeightsReqResp.SerializeToString,
            common__pb2.VariableWeightsReqResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Push(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParameterService/Push',
            parameter__server__pb2.ParameterPushReq.SerializeToString,
            parameter__server__pb2.ParameterPushResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pull(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParameterService/Pull',
            parameter__server__pb2.ParameterPullReq.SerializeToString,
            parameter__server__pb2.ParameterPullResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
