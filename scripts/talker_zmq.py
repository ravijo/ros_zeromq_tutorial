#!/usr/bin/env python

import rospy
import zmq


def talker():
    rospy.init_node("talker_zmq", anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:6666")

    while not rospy.is_shutdown():
        msg_str = "hello_world_%s" % rospy.get_time()
        rospy.loginfo(msg_str)
        socket.send_string(msg_str)
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
