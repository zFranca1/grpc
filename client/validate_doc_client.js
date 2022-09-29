var PROTO_PATH = __dirname + '/../proto/validate_doc.proto';

var parseArgs = require('minimist');
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var validate_proto = grpc.loadPackageDefinition(packageDefinition);

function main() {
  var argv = parseArgs(process.argv.slice(2), {
    string: 'target'
  });
  var target;
  if (argv.target) {
    target = argv.target;
  } else {
    target = 'localhost:50051';
  }
  var client = new validate_proto.validator(target,
                                       grpc.credentials.createInsecure());
  var user = {};
  if (argv._.length > 0) {
    user = argv._[0]; 
  } else {
    //123456789012345 - invalidos
    //90306453000103 - invalidos
    //90306453000133 - valido
    //31049514000165 - valido

    //49047651847 - valido
    user.type = 2;
    user.doc = '31049514000165';
  }
  client.OrderDocument(user, function(err, response) {
    console.log('Greeting:', response);
  });
}

main();