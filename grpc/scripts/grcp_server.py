#!/usr/bin/env python3
## @file
# gRPC server script

import grpc
import rospy
import rpc_pb2
import logging
import rpc_pb2_grpc
from concurrent import futures
from std_msgs.msg import Int32MultiArray

## @class RPC
# gRPC server class
class RPC(rpc_pb2_grpc.RPCServicer):

    ## Constructor
    def __init__(self):
        ## Data storage for received coordinates
        self.data = []
        rospy.init_node("listener", anonymous=True)
        rospy.Subscriber('/coord', Int32MultiArray, self.callback)

    ## Callback function for subscriber
    # @param data The received data from the subscriber
    def callback(self, data):
        self.data = [data.data[0], data.data[1], data.data[2], data.data[3]]
        
    ## Data collection to be published for the client
    # @param request The request message of type google.protobuf.Empty
    # @param context The gRPC context object
    # @return The response message of type rpc_pb2.Coords
    def GetCoord(self, request, context):
        return rpc_pb2.Coords(values=[self.data[0], self.data[1], self.data[2],self.data[3]])

## Function to initiate the gRPC server
def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc_pb2_grpc.add_RPCServicer_to_server(RPC(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
