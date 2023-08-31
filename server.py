import grpc
import greeter_pb2
import greeter_pb2_grpc
import concurrent.futures

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        response = greeter_pb2.HelloReply(message=f"Hello, {request.name}!")
        print("Printing the request in console for us to see",request)
        return response

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("Starting server in [::]:50051")
    serve()
