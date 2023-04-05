#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def joy_callback(data):
    twist = Twist()
    twist.linear.x = data.axes[1] * 0.5 # Scale joystick input to half of maximum linear speed
    twist.angular.z = data.axes[0] * 0.5 # Scale joystick input to half of maximum angular speed
    pub.publish(twist)

rospy.init_node('joystick_controller')
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rospy.Subscriber('joy', Joy, joy_callback)
rospy.spin()
