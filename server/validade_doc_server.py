import grpc
import concurrent
from concurrent import futures

import validate_doc_pb2
import validate_doc_pb2_grpc
import re

class validatorServicer(validate_doc_pb2_grpc.validatorServicer):
    def OrderDocument(self, request, context):
        print("we got something!!")


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    validate_doc_pb2_grpc.add_validatorServicer_to_server(validatorServicer(), server)
    print('listening on port 50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()





main()            

