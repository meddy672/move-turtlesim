#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def poseCallback(pose_message):
    print "pose callback"
    print ('x = {}'.format(pose_message.x))
    print ('y = %f' %pose_message.y)
    print ('yaw = {}'.format(pose_message.theta))

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        position_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
        