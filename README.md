# Turtlebot_Hallway_Guidance
Repository containing code for turtlebots to navigate the hallways of Halligan. 

Currently contains a srv files and servers to either look up the coordinates of one location by name OR to print out all locations. 

There is a patrol program where the robot patrols between two coordinates, and a door to door program where the robot moves from door to door for all the mapped locations on the second floor of the Halligan building.

This repository does not contain any packages so it cannot be run alone in a terminal. Purpose is just to store the files, the files must be copied into another package in order to run. 


HOW TO RUN Door to Door Program
- Start up the turtlebot with roslaunch tbot2_launch tbot2_lidar.launch and roslaunch tbot2_launch amcl_navigation.launch 

- Make sure to get a very accurate 2D Pose Estimate in Rviz. Start the robot at a place that is very obvious to mark on the map. The first door the robot will travel to is Room 202 so starting the robot near there is a good idea. Without a good initial pose estimate, the robot will become confused and it will be less likely to finish successfully. 

- The robot will go door to door of the right hallway, then cross to the left hallway through the Collab room. The robot will then move back down the left hallway going door to door. Finally, it will cross back and end near the stairs/main office. 

