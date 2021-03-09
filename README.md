# AirSimLiDARpointcloud

*DISCLAIMER: This Script is made to run in parallel to existing multirotor/car movement scripts. It does not have any effect on the vehicle used when it comes to displacement of any sort, it is just meant to scan and model whatever the LiDAR sensor is able to see at any given moment.<br /> 
*Additional Note: Make sure you have a LiDAR sensor configured under the AirSim settings.json file before running this script, based on the DataFrame chosen, please run the relevant script<br />  

The best way to run this script is through the 'CMD.exe Prompt' application on anaconda3<br /> 

Steps Involved:<br /> 
1.Make sure the vehicle is at the desired starting location (This will be very important for how the script arranges the points of the point cloud).<br /> 
2.Run the script through CMD.exe<br /> 
3.(Optional,but highly recommended) Run a Second Script that allows the vehicle to move in your desired path for optimal scanning purposes<br /> 
4.Once the movement script is completed, or when you decided that enough points have been collected, select the terminal where you are running the point cloud script from, and input the keyboard interrupt: 'Ctrl+C', this will end the script and save the point cloud data<br /> 
5.The point cloud data will then be stored as 'data.asc' in the selected file location where the lidar point cloud script was run in<br /> 
6.You can open 'data.asc' with third party software (CloudCompare is highly recommended) to view the point cloud according to your specific usecase (de-noising, segmentation, transformation, alignment, etc.). Another good alternative for this is MeshLab<br /> 

CloudCompare Download Link: http://www.danielgm.net/cc/release/<br /> 
MeshLab Download Link: https://www.meshlab.net/#download<br /> 

*Another Additional Note: So long as the starting position of the drone is constant, multiple scans can be superimposed onto each other by merging the contents of the .asc files. This may be used for additional accuracy<br />

Example Outputs:

![Capture 1](https://user-images.githubusercontent.com/44498143/110518904-affa2700-8147-11eb-9b53-ac47e56a1c8d.PNG)
![Capture 2](https://user-images.githubusercontent.com/44498143/110518912-b2f51780-8147-11eb-992e-c09fd336abd8.PNG)

Configuration of LiDAR sensor used:

![Capture 3](https://user-images.githubusercontent.com/44498143/110519310-1da65300-8148-11eb-9fc8-e1593f6430ec.PNG)
