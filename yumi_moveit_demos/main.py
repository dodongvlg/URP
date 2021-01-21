#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import yumi_moveit_utils as yumi
import moveit_msgs.msg
import geometry_msgs.msg
from std_srvs.srv import Empty

##### ADDED #####
# import pyrealsense2 as rs
# import numpy as np
# import cv2
# import os
# sys.path.append('/home/urp')
# # import realcamera
# import time
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge


def close_grippers(arm):
    """Closes the grippers.

    Closes the grippers with an effort of 15 and then relaxes the effort to 0.

    :param arm: The side to be closed (moveit_utils LEFT or RIGHT)
    :type arm: int
    :returns: Nothing
    :rtype: None
    """
    yumi.gripper_effort(arm, 15.0)
    yumi.gripper_effort(arm, 0.0)

def open_grippers(arm):
    """Opens the grippers.

    Opens the grippers with an effort of -15 and then relaxes the effort to 0.

    :param arm: The side to be opened (moveit_utils LEFT or RIGHT)
    :type arm: int
    :returns: Nothing
    :rtype: None
    """
    yumi.gripper_effort(arm, -15.0)
    yumi.gripper_effort(arm, 0.0)



def move_and_grasp(arm, pose_ee, grip_effort):
    try:
        yumi.traverse_path([pose_ee], arm, 10)
    except Exception:
        if (arm == yumi.LEFT):
            yumi.plan_and_move(yumi.group_l, yumi.create_pose_euler(pose_ee[0], pose_ee[1], pose_ee[2], pose_ee[3], pose_ee[4], pose_ee[5]))
        elif (arm == yumi.RIGHT):
            yumi.plan_and_move(yumi.group_r, yumi.create_pose_euler(pose_ee[0], pose_ee[1], pose_ee[2], pose_ee[3], pose_ee[4], pose_ee[5]))

    if (grip_effort <= 20 and grip_effort >= -20):
        yumi.gripper_effort(arm, grip_effort)
    else:
        print("The gripper effort values should be in the range [-20, 20]")




def run():
    """Starts the node

    Runs to start the node and initialize everthing. Runs forever via Spin()

    :returns: Nothing
    :rtype: None
    """

    rospy.init_node('yumi_moveit_demo')

    #Start by connecting to ROS and MoveIt!
    yumi.init_Moveit()


    # Print current joint angles
    yumi.print_current_joint_states(yumi.RIGHT)
    yumi.print_current_joint_states(yumi.LEFT)

    # Reset YuMi joints to "home" position
    yumi.reset_pose()


    # Drive YuMi end effectors to a desired position (pose_ee), and perform a grasping task with a given effort (grip_effort)
    # Gripper effort: opening if negative, closing if positive, static if zero
    pose_ee = [0.3, 0.15, 0.2, 0.0, 3.14, 3.14]
    grip_effort = -10.0
    move_and_grasp(yumi.LEFT, pose_ee, grip_effort)

    pose_ee = [0.3, -0.15, 0.2, 0.0, 3.14, 3.14]
    grip_effort = -10.0
    move_and_grasp(yumi.RIGHT, pose_ee, grip_effort)

    rospy.spin()

# def callback(msg, pub):
#     pub.publish(msg)

def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(3)

def callback(img_msg):
    cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
    show_image(cv_image)

def start_camera():
    #rospy.init_node('image_republisher')
    # stream_image_topic = "/camera/color/image_raw"
    # rospy.Subscriber(stream_image_topic, Image, callback)
    # rospy.spin()
    rospy.Subscriber('/camera/color/image_raw', Image, callback)
    rospy.spin()

def pick_up():
    yumi.gripper_effort(yumi.LEFT, -20)
    yumi.go_to_simple(0.5, 0.2, 0.08, 3.14, 0, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 20)
    yumi.go_to_simple(0.3, 0.2, 0.3, 1.57, 0, 0, yumi.LEFT)

def check_grip():
    yumi.go_to_simple(0.3, 0.3, 0.3, 0, 1.57, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -20)
    yumi.gripper_effort(yumi.LEFT, 10)

def grab():
    yumi.gripper_effort(yumi.LEFT, -10)
    #yumi.go_to_simple(0.4, 0.2, 0.03, 0, 3.14, 0, yumi.LEFT)
    #yumi.go_to_simple(0.4, 0.2, 0.03, 3.14, 0, 0, yumi.LEFT)
    yumi.go_to_simple(0.4, 0.2, 0.3, 0, 3, 0, yumi.LEFT)
    yumi.go_to_simple(0.4, 0.2, 0.03, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 20)

def give():
    #yumi.go_to_simple(0.65, 0.2, 0.2, 0, 1.57, 0, yumi.LEFT)
    yumi.go_to_simple(0.65, 0.2, 0.2, 0, 1.57, 0, yumi.LEFT)

def test_action_without_traverse():
    yumi.group_l.set_max_velocity_scaling_factor(1)

    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.25, 0.0, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.1, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.1, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.1, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.2, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.1, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.3, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.1, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)

def test_action_with_traverse():
    yumi.group_l.set_max_velocity_scaling_factor(1)
    yumi.go_to_simple(0.3, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.gripper_effort(yumi.LEFT, -10)
    
    yumi.traverse_path([[0.3, 0.1, 0.3, 0, 3.14, 0], [0.25, 0.0, 0.15, 0, 3.14, 0]], yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.traverse_path([[0.6, 0.1, 0.2, 0, 3.14, 0]], yumi.LEFT)

left_base_angle = [-0.005721145309507847, -2.256985902786255, 2.395789861679077, 0.5422261357307434, -0.02853975258767605, 0.70625239610672, 0.01869707554578781]
right_base_angle = [-0.015401790849864483, -2.251002550125122, -2.355128049850464, 0.5348764061927795, -0.0030396634247153997, 0.677087128162384, 0.01322004571557045]
giving_point_angle = [-2.7146573066711426, -1.814459204673767, 0.1805383712053299, -0.37618154287338257, 2.0579378604888916, -0.027682604268193245, -0.12345307320356369]

def test_200513():
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)

    yumi.go_to_simple(0.25, 0.0, 0.2, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.2, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.1, 0.2, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.2, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.2, 0.2, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_simple(0.6, 0.0, 0.2, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def test_200513_v2():
    # yumi.go_to_joints(left_base_angle, yumi.LEFT)
    # yumi.gripper_effort(yumi.LEFT, -10)

    yumi.go_to_simple(0.25, 0.2, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.1, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.0, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def test_200518():
    yumi.go_to_simple(0.25, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.25, 0.2, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.25, 0.1, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)
    
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def test_200518_v2():
    yumi.go_to_simple(0.25, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.25, 0.2, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

    yumi.go_to_simple(0.25, 0.1, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.25, 0.1, 0.15, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_joints(giving_point_angle, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)


def box_from_top():
    yumi.go_to_simple(0.37, 0.0, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.37, 0.0, 0.22, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.67, 0.2, 0.22, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def cup_from_left():
    yumi.go_to_simple(0.37, 0.38, 0.11, 1.57, 0, 0, yumi.LEFT)
    yumi.go_to_simple(0.37, 0.33, 0.11, 1.57, 0, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.55, 0.2, 0.11, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def cup_from_top():
    yumi.go_to_simple(0.37, 0.2, 0.3, 0, 3.14, 0, yumi.LEFT)
    yumi.go_to_simple(0.37, 0.2, 0.25, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.67, 0.2, 0.25, 0, 3.14, 0, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def cup_from_front():
    yumi.go_to_simple(0.2, 0.2, 0.11, 1.57, 0, 1.57, yumi.LEFT)
    yumi.go_to_simple(0.25, 0.2, 0.11, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, 10)
    yumi.go_to_simple(0.55, 0.2, 0.11, 1.57, 0, 1.57, yumi.LEFT)
    yumi.gripper_effort(yumi.LEFT, -10)
    yumi.go_to_joints(left_base_angle, yumi.LEFT)

def main_test():
    global speed, fast, slow
    global motion_is_big

    p = yumi.PoseStamped()
    p.header.frame_id = yumi.robot.get_planning_frame()

    speed = 1.0
    fast = False
    slow = False
    motion_is_high = False
    motion_is_wide = False

    while True:
        yumi.scene.remove_world_object("height_restraint")
        yumi.scene.remove_world_object("width_restraint")

        ########### Speed ###########
        if (fast):
            speed -= 0.1
        elif (slow):
            speed += 0.1
        yumi.group_l.set_max_velocity_scaling_factor(speed)

        ########### Hight & Width ###########
        if (motion_is_high):
            p.pose.position.x = 0.25
            p.pose.position.y = 0.0
            p.pose.position.z = 0.7
            yumi.scene.add_box("height_restraint", p, (2, 2, 0.005))

        if (motion_is_wide):
            p.pose.position.x = 0.0
            p.pose.position.y = 0.55
            p.pose.position.z = 0.3
            scene.add_box("width_restraint", p, (1, 0.005, 1))


        ###########
        mode = input("Choose what to pick up (box: 1, cup: 2) : ")
        
        if (mode == 1):
            print("Pick up box")
            box_from_top()
        elif (mode == 2):
            print("Pick up cup")
            direction = input("Choose direction (left: 1, top: 2, front: 3) : ")
            if (direction == 1):
                cup_from_left()
            elif (direction == 2):
                cup_from_top()
            elif (direction == 3):
                cup_from_front()
            else:
                continue
        else:
            continue
    
if __name__ == '__main__':
    try:
        # run()
        rospy.init_node('yumi_moveit_demo')
        
        #Start by connecting to ROS and MoveIt!
        yumi.init_Moveit()
        # yumi.go_to_simple(0.55, 0.2, 0.11, 1.57, 0, 1.57, yumi.LEFT)
        yumi.go_to_simple(0.2, 0.2, 0.11, 1.57, 0, 1.57, yumi.LEFT)
        yumi.go_to_joints(left_base_angle, yumi.LEFT)

        # Giving joints: (0.67, 0.2, 0.3, 1.57, 0, 1.57, yumi.LEFT)
        # yumi.go_to_joints(left_base_angle, yumi.LEFT)
        # main_test()
        # test_action_with_traverse()

    	print "####################################     Program finished     ####################################"
    except rospy.ROSInterruptException:
        pass
