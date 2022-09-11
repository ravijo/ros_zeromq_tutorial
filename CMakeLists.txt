# cmake_minimum_required(VERSION 2.8.3)
# project(ros_zeromq_tutorial)

# find_package(PythonLibs 2.7 REQUIRED)
# set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake CACHE INTERNAL "" FORCE)

# find_package(ZeroMQ)
# find_package(catkin REQUIRED COMPONENTS rospy)

# catkin_package()
# include_directories(include ${catkin_INCLUDE_DIRS} ${ZeroMQ_INCLUDE_DIRS})

# add_executable(talker_zmq src/talker_zmq.py)
# target_link_libraries(talker_zmq ${catkin_LIBRARIES} ${ZeroMQ_LIBRARIES})

# add_executable(listener_zmq src/listener_zmq.py)
# target_link_libraries(listener_zmq ${catkin_LIBRARIES} ${ZeroMQ_LIBRARIES})

cmake_minimum_required(VERSION 2.8.3)
project(ros_zeromq_tutorial)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

find_package(ZeroMQ)


catkin_package()
# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
catkin_install_python(PROGRAMS
  src/talker_zmq
  src/talker_zmq.py
  src/listener_zmq
  src/listener_zmq.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/src
)