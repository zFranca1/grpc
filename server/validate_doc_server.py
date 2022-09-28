from urllib.request import Request
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


def validation(request):
    if request.type == validate_doc_pb2.TYPE.CPF:
        cpf = request.document

        soma = 0
        count = 10
        for i in range(0, len(cpf)-2):
            soma = soma + (int(cpf[i])*count)
            i+=1
            count-=1
        dg1 = 11-(soma%11)
        if dg1 >= 10:
            dg1 = 0

        soma = 0
        count = 10
        for j in range(1, len(cpf)-1):
            soma = soma + (int(cpf[j])*count)
            j+=1
            count-=1
        dg2 = 11-(soma%11)
        if dg2 >= 10:
            dg2 = 0

        if int(cpf[9]) != dg1 or int(cpf[10]) != dg2:
            return 1, validate_doc_pb2.STATUS.VALID
        else:
            return 0, validate_doc_pb2.STATUS.VALID


main()            

