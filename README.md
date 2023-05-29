# M4-midterm
Repository for a gRPC server and client using ROS for color detection and image coordinates adquisition.
## Video demostration
https://www.youtube.com/watch?v=BmOSbtz3M_k
## Data Flow Diagram
![DFD](DFD_M4MidTerm.drawio.png)
## CORS uses and benefits
Cross-Origin Resource Sharing best known as CROS is a security policy for browsers that increases security and protection to users when accessing or loading resources from various origins.
It has the main feature of allowing controlled-access to CO(Cross-Origin) resources while preventing unauthorized access from unknown sources which in return allows modern web application access to resources from different domains.
Some of the key points as to why CORS is used are:
•	Same-Origin Policy Enforcement
•	Cross-Origin Resource Access
•	API Integration and Data Sharing
•	Authentication and Authorization
•	Security Considerations
•	Development and Testing
CORS is a technology that could prove extremely beneficial to an application that uses gRPC server and getaway since we are dealing with HTTPS requests and REST-API since it would provide the application with a secure way to fetch data from APIs and through HTTP.
## gRPC Service setup and execution
### Start image coordinates detector
1. To run start de server and use the client you first need need to create a catkin workspace and set up a ROS package
2. git clone https://github.com/salazarch/M4-midterm.git to the src directory of the package and then run in a separate cmd
```
roscore
```
After that, open a second terminal and run
```
cd M4-midterm/grpc/scripts
rosrun grpc detectCoord.py
```
Note: you may need to source devel/setup.sh in order for the rosrun to properly work
### Start gRPC Server
In the same directory run
```
python3 grpc_server.py
```
### Use gRPC Client
In the same directory run
```
python3 grpc_client.py
```
