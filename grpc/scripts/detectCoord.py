#!/usr/bin/env python3
## @file
# Detect green object through webcam and print coordinates

# Libraries
import cv2
import numpy as np
import ctypes
import rospy
from ctypes import *
from std_msgs.msg import Int32MultiArray

## @class m4_t1
# Class for detecting green objects through a webcam and publishing their coordinates
class m4_t1:

    ## Constructor
    def __init__(self):
        ## Publish of coord*100
        self.pub = rospy.Publisher('/coord', Int32MultiArray, queue_size=10)

        ## Cpp library
        libname = "/home/izacs/m4_midterm_ws/src/M4_t1/src/t1/lib/libmulti.so"
        self.mylib = ctypes.cdll.LoadLibrary(libname)
        self.funct = self.mylib.multi
        self.funct.restype = ctypes.POINTER(ctypes.c_int)

    ## Method to capture video and detect green objects
    def video(self):
        # Define a video capture object
        vid = cv2.VideoCapture(0)

        while(True):

            # Capture the video
            ret, frame = vid.read()

            # Convert the BGR image to HSV colour space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Set the lower and upper bounds for the green hue
            low = np.array([35,80,0])
            up = np.array([80,255,255])

            # Create mask
            maskG = cv2.inRange(hsv, low, up)

            # Eliminate small blobs
            c, h = cv2.findContours(maskG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

            # Minimum area for accepted blobs
            threshold_blob_area = 1000

            # Noise blobs
            for i in range(1, len(c)):
                index_level = int(h[0][i][1])
                if index_level <= i:
                    cnt = c[i]
                    area = cv2.contourArea(cnt)
                if(area) <= threshold_blob_area:
                    cv2.drawContours(maskG, [cnt], -1, 0, -1, 1)

            # Find contour of blob
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
            contour = cv2.morphologyEx(maskG, cv2.MORPH_OPEN, kernel, iterations=4)

            # Get coordinates
            x,y,w,h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (139,0,0), 4)

            # Display text with coordinates 'x' and 'y' on frame
            cv2.putText(frame, "x: "+str(x), (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
            cv2.putText(frame, "y: "+str(y), (x+130, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)

            # Display original coordinates
            timestamp = rospy.Time.now()

            # Use library
            ret_ptr = self.funct(ctypes.c_int(x), ctypes.c_int(y))
            ret_arr = ret_ptr[:2]

            # Publish coordinates to topic
            self.pub.publish(Int32MultiArray(data=[ret_arr[0], ret_arr[1], timestamp.secs, timestamp.nsecs]))

            # Eliminate return value
            self.mylib.delete_arr.argtypes = [ctypes.POINTER(ctypes.c_int)]
            self.mylib.delete_arr.restype = None
            self.mylib.delete_arr(ret_ptr)

            # Displays
            cv2.imshow('Frame', frame)

            # 'q' = quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

if __name__ == '__main__':
    m = m4_t1()
    rospy.init_node('m4_t1', anonymous=True)
    m.video()
    try:
        while not rospy.is_shutdown():
            rospy.Rate(100)
    # Exit
    except KeyboardInterrupt:
        print("Shutting down")
