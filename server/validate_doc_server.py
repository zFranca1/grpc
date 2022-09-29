
from urllib.request import Request
import grpc
import concurrent
from concurrent import futures
from itertools import cycle


import validate_doc_pb2
import validate_doc_pb2_grpc
import re


LENGTH_CNPJ = 14


class validatorServicer(validate_doc_pb2_grpc.validatorServicer):
    def OrderDocument(self, request: validate_doc_pb2.DocumentResquest,
                      context: grpc.aio.ServicerContext) -> validate_doc_pb2.DocumentResponse:
        print(request)
        if cpf_validate(request.doc) == True and request.type == 1:
            return validate_doc_pb2.DocumentResponse(message='Valido', type=1, validation=True)
        elif cpf_validate(request.doc) == False and request.type == 1:
            return validate_doc_pb2.DocumentResponse(message='Invalido', type=1, validation=False)
        elif is_cnpj_valido(request.doc) == True and request.type == 2:
            return validate_doc_pb2.DocumentResponse(message='Valido', type=2, validation=True)
        elif is_cnpj_valido(request.doc) == False and request.type == 2:
            return validate_doc_pb2.DocumentResponse(message='Invalido', type=2, validation=False)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    validate_doc_pb2_grpc.add_validatorServicer_to_server(
        validatorServicer(), server)
    print('listening on port 50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def is_cnpj_valido(cnpj: str) -> bool:
    if len(cnpj) != LENGTH_CNPJ:
        return False

    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True


main()
