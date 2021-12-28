# Gazebo-Ardupilot-World-Generator

Running "Generate_Gazebo_World.py will prompt you to specify the number of Ardupilot instances you want.

It will copy the contents of BaseDrone into multiple numbered subfolders. 

it will load default_world.world and add the extra uavs

It then writes the config file to each rone with a different port number, starting from 9002 and incrementing by 10 per drone
