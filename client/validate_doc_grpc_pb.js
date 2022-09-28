// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var validate_doc_pb = require('./validate_doc_pb.js');

function serialize_DocumentResponse(arg) {
  if (!(arg instanceof validate_doc_pb.DocumentResponse)) {
    throw new Error('Expected argument of type DocumentResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DocumentResponse(buffer_arg) {
  return validate_doc_pb.DocumentResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_DocumentResquest(arg) {
  if (!(arg instanceof validate_doc_pb.DocumentResquest)) {
    throw new Error('Expected argument of type DocumentResquest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DocumentResquest(buffer_arg) {
  return validate_doc_pb.DocumentResquest.deserializeBinary(new Uint8Array(buffer_arg));
}


var validatorService = exports.validatorService = {
  orderDocument: {
    path: '/validator/OrderDocument',
    requestStream: false,
    responseStream: false,
    requestType: validate_doc_pb.DocumentResquest,
    responseType: validate_doc_pb.DocumentResponse,
    requestSerialize: serialize_DocumentResquest,
    requestDeserialize: deserialize_DocumentResquest,
    responseSerialize: serialize_DocumentResponse,
    responseDeserialize: deserialize_DocumentResponse,
  },
};

exports.validatorClient = grpc.makeGenericClientConstructor(validatorService);
