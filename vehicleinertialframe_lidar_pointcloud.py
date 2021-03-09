# Python client example to get Lidar data from a drone
# This script is for Lidar sensors using 'VehicleInertialFrame' as DataFrame under settings.json

import setup_path 
import airsim

import sys
import math
import time
import argparse
import pprint
import numpy as np

# Makes the drone fly and get Lidar data
class LidarTest:

    def __init__(self):

        # connect to the AirSim simulator
        self.client = airsim.VehicleClient()
        self.client.confirmConnection()
        print('Connected!\n')

    def execute(self):
        #self.client.reset()
        print('Scanning Has Started\n')
        print('Use Keyboard Interrupt \'CTRL + C\' to Stop Scanning\n')
        f = open('data.asc', "w")
        try:
            while True:
                lidarData = self.client.getLidarData();
                flag = 0
                for item in lidarData.point_cloud:
                    if (flag == 0):
                        X = item
                    elif (flag == 1):
                        Y = item
                    else:
                        Z = item
                    flag = flag + 1
                    if (flag == 3):
                        f.write("%f %f %f %d %d %d \n" % (X,Y,Z,255,255,0))
                        flag=0
                    else:
                        pass
        except KeyboardInterrupt:
            f.close()
            pass
            #time.sleep(5)
            airsim.wait_key('Press any key to reset to original state')
            self.client.reset()
            print("Done!\n")

# main
if __name__ == "__main__":
    lidarTest = LidarTest()
    lidarTest.execute()
