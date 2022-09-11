/**
 * talker_zmq.cpp
 * Author: Ravi Joshi
 * Date: 2018/01/18
 */

#include <ros/ros.h>

#include <zmq.hpp>

int main(int argc, char** argv) {
  ros::init(argc, argv, "talker_zmq", ros::init_options::AnonymousName);

  ros::Time::init();  // Workaround since we are not using NodeHandle
  ros::Rate loop_rate(10);

  //  Prepare our context and publisher
  zmq::context_t context(1);
  zmq::socket_t publisher(context, ZMQ_PUB);
  publisher.bind("tcp://*:6666");

  while (ros::ok()) {
    std::stringstream msg_str_stream;
    msg_str_stream << "hello_world_" << ros::Time::now();
    std::string msg_str = msg_str_stream.str();

    zmq::message_t message(msg_str.length());
    memcpy(message.data(), msg_str.c_str(), msg_str.length());

    ROS_INFO_STREAM(msg_str);
    publisher.send(message);
    loop_rate.sleep();
  }
  // Clean up your socket and context here
  publisher.close();
  context.close();

  return 0;
}
