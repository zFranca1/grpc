const grpc = require('grpc');
const messages = require('./validate_doc_pb')
const services = require('./validate_doc_grpc_pb')

function main(){

    var client = new services.validatorService(
        'localhost:50051', grpc.credentials.createInsecure()
    );

    var documentRequest = new messages.documentRequest();
    documentRequest.setType(0);
    documentRequest.setDoc('49047651847');

    client.orderDocument(documentRequest, function(err, response){

        if (err) {
            console.log("deu ruim", err);
        } else {
            console.log('response from python', response);
        }
    })

}

main();