#!/usr/bin/env python

import zmq
import rospy


def listener():
    rospy.init_node("listener_zmq", anonymous=True)

    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    TOPIC = b""
    socket.setsockopt(zmq.SUBSCRIBE, TOPIC)

    linger = 0
    socket.setsockopt(zmq.LINGER, linger)
    socket.connect("tcp://localhost:6666")

    while not rospy.is_shutdown():
        string = socket.recv()
        # topic, messagedata = string.split()
        rospy.loginfo("I heard %s", string)

    socket.close()
    context.close()


if __name__ == "__main__":
    listener()
