#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

rospy.init_node('move_robot_node') # Start node called 'move_robot_node'

# Create a Publisher object, that will publish on the /cmd_vel topic and 
# publish Twist messages to this topic.
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rate = rospy.Rate(2) # Set a publish rate of 2 Hz
move = Twist() # Create a var of type Twist
move.linear.x = 1.0
move.angular.z = 1.0

while not rospy.is_shutdown(): # Create a loop that will go until someone stops the program execution
    
    pub.publish(move)
    
    rate.sleep()