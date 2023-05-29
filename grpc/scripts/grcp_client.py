#!/usr/bin/env python3
## @file
# gRPC client script

import grpc
import logging
import rpc_pb2
import rpc_pb2_grpc

## Function to run the gRPC client
def run():
    ## Establish an insecure channel to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        ## Create a stub for the RPC service
        stub = rpc_pb2_grpc.RPCStub(channel)
        ## Make a request to the GetCoord RPC method
        response = stub.GetCoord(rpc_pb2.Coords())

    ## Print the received coordinates and timestamp
    print("-----------------")
    print(f"X: {str(response.values[0])}, Y: {str(response.values[1])}\nTimestamp - secs: {str(response.values[2])}, Timestamp - nsecs: {str(response.values[3])}")
    print("-----------------")

if __name__ == '__main__':
    logging.basicConfig()
    run()
