#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import zmq

def talker():
    # pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker_zmq', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:6666")

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        socket.send(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass