# ROS ZeroMQ Tutorial

This tutorial shows how to use [ZeroMQ](http://zeromq.org) with ROS for publishing and subscribing to messages. The following two languages are supported:

* CPP
* Python (see [thanks](#thanks) section)


## Dependencies
1. [ZeroMQ](http://zeromq.org/): Install ZeroMQ using following command: 
    ```
    sudo apt-get install libzmq3-dev
    ```
    _It should be easy to install newer versions of ZeroMQ, and this repository should be compatible with them. However, please note that this repository is only for demonstration purposes. Therefore, we have not tested it thoroughly. In such cases, please feel free to open a new [issue](#issue) to inform the changes to authors._


## Compilation
1. Make sure to download complete repository. Use `git clone` or download zip as per convenience.
1. Invoke catkin tool inside ros workspace i.e., `catkin_make`


## Steps to run
1. Start ROS Core by using the following command:
    ```
    roscore
    ```
1. Invoke the publisher by using the following command:
    ```
    rosrun ros_zeromq_tutorial talker_zmq
    ```
    Alternatively, the python version of talker can be started by using the following command:
    ```
    rosrun ros_zeromq_tutorial talker_zmq.py
    ```
1. The published data can be seen by using the following command:
    ```
    rosrun ros_zeromq_tutorial listener_zmq
    ```
    Alternatively, the python version of listener can be started by using the following command:
    ```
    rosrun ros_zeromq_tutorial listener_zmq.py
    ```


## Issue
Please check [here](https://github.com/ravijo/ros_zeromq_tutorial/issues) and create issues accordingly.


## Thanks
The following authors are sincerely acknowledged for the improvements of this package:
* [Md Rakin Sarder](https://github.com/tunchunairarko): For providing python nodes
