"""Server for the data collector service.

This file uses gRPC to communicate with other processes.  It contains
a single method, `Collect` which expects no data and returns the parsed
CSV file.

"""

from concurrent import futures
import csv
from datetime import datetime
from signal import signal, SIGTERM

from google.protobuf.timestamp_pb2 import Timestamp
import grpc

from collector_pb2 import ElectricalState, ElectricalData
import collector_pb2_grpc

class DataCollectorService(collector_pb2_grpc.DataCollectorServicer):

    """Object to serve data to gRPC clients."""

    def Collect(self, request, context):
        """Read the CSV file and send the ElectricalData response."""
        data = []
        with open("meterusage.csv", "r", encoding="utf-8") as file:
            for i, line in enumerate(csv.reader(file)):
                if i == 0:
                    continue

                # Try to extract the information from this line of data.
                timestamp = Timestamp()
                try:
                    time, meter = line
                    time = datetime.fromisoformat(time)
                    meter = float(meter)
                except ValueError:
                    # It might be worth logging something here.
                    continue
                else:
                    timestamp.FromDatetime(time)
                    data.append(ElectricalState(step=timestamp, meter=meter))

        return ElectricalData(states=data)


def serve():
    """Start the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    collector_pb2_grpc.add_DataCollectorServicer_to_server(
            DataCollectorService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    def handle_sigterm(*_):
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)

    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
