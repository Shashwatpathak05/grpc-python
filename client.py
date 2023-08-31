import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    # Replace "your_server_domain.com" with the DNS name of your Ingress
    target = "<dns of external facing LB>"

    # Create the channel credentials
    creds = grpc.ssl_channel_credentials()

    # Override the target name to match the certificate's Common Name (CN) or Subject Alternative Name (SAN)
    channel = grpc.secure_channel(target, creds, options=(('grpc.ssl_target_name_override', '<dns of external facing LB>'),))

    # Create the gRPC stub
    stub = greeter_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(greeter_pb2.HelloRequest(name="Vishnu"))
    print("Greeter client received: " + response.message)

if __name__ == "__main__":
    run()