import grpc
import greeter_pb2
import greeter_pb2_grpc
import concurrent.futures
import logging
import random
import time

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        response = greeter_pb2.HelloReply(message=f"Hello, {request.name}!")
        logging.info("Received request: %s", request)
        return response

def serve():
    logging.basicConfig(filename='grpc_server.log', level=logging.INFO)

    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")

    logging.info("Starting server in [::]:50051")

    server.start()

    try:
        while True:
            # Add random log messages for testing
            random_log_level = random.choice([logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR])
            logging.log(random_log_level, "This is a random log message for testing")

            time.sleep(5)  # Sleep for 5 seconds before the next random log message

    except KeyboardInterrupt:
        logging.info("Server stopped by user")
        server.stop(0)

if __name__ == "__main__":
    serve()
