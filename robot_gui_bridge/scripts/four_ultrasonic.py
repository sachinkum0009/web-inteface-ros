#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node('four_ultrasonic')
    pub1 = rospy.Publisher('/ultrasonic1', Int32, queue_size=1)
    pub2 = rospy.Publisher('/ultrasonic2', Int32, queue_size=1)
    pub3 = rospy.Publisher('/ultrasonic3', Int32, queue_size=1)
    pub4 = rospy.Publisher('/ultrasonic4', Int32, queue_size=1)

    rate = rospy.Rate(10) # 10 hz

    value1 = 24
    value2 = 34
    value3 = 44
    value4 = 54

    while not rospy.is_shutdown():
        pub1.publish(value1)
        pub2.publish(value2)
        pub3.publish(value3)
        pub4.publish(value4)

        rate.sleep()

if __name__ == '__main__':
    main()

