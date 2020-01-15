# ros_zeromq_tutorial
ZeroMQ tutorial for ROS

This tutorial shows how to use [ZeroMQ](http://zeromq.org/) inside ros for publishing and subscribing messages.

## Dependencies
1. [ZeroMQ](http://zeromq.org/): Install ZeroMQ using following command `sudo apt-get install libzmq3-dev`

## Compilation
1. Make sure to download compelte repository. Use `git clone` or download zip as per convenience.
1. Invoke catkin tool inside ros workspace i.e., `catkin_make`

## Steps to run
1. Invoke the publisher by using following command `rosrun ros_zeromq_tutorial talker_zmq`
1. The published data can be seen by using following command `rosrun ros_zeromq_tutorial listener_zmq`

## Issues (or Error Reporting)
Please check [here](https://github.com/ravijo/ros_zeromq_tutorial/issues) and create issues accordingly.
