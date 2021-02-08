from autolab_core import RigidTransform
from yumipy import YuMiRobot, YuMiState
from yumipy import YuMiConstants as YMC

import numpy as np
from scipy.spatial.transform import Rotation
import time
from datetime import datetime
import os
import ntplib
import random
from pathlib import Path
import random

import write_log
import robot_action
import speed_optimization

def rpy_to_wxyz(r, p, y):  # Change euler angle to quaternion
    rot = Rotation.from_euler('xyz', [r, p, y], degrees=True)
    return rot.as_quat()

def input_work_train(num):
    print("Train num: %d" %num)
    write_log.write_log(1, 0, 0, 0, time_diff)

    if (num == 1):
        y.set_v(1500)
        y.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.2], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.8, -0.1, 0.35], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.8, 0.1, 0.35], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.8, -0.1, 0.35], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.8, 0.0, 0.35], rotation = right_front_rotation))

    elif (num == 2):
        y.set_v(1500)
        y.left.goto_pose(RigidTransform(translation = [0.3, 0, 0.2], rotation = left_front_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.8, 0, 0.35], rotation = left_front_rotation))

    elif (num == 3):
        y.set_v(700)
        radius = 0.1
        angle = np.pi / 8
        delta_T = RigidTransform(translation=[0,0,-radius], from_frame='gripper', to_frame='gripper')
        R_shake = np.array([[1, 0, 0],
                            [0, np.cos(angle), -np.sin(angle)],
                            [0, np.sin(angle), np.cos(angle)]])
        delta_T_up = RigidTransform(rotation=R_shake, translation=[0,0,radius], from_frame='gripper', to_frame='gripper')
        delta_T_down = RigidTransform(rotation=R_shake.T, translation=[0,0,radius], from_frame='gripper', to_frame='gripper')
        T_shake_up = YMC.L_PREGRASP_POSE.as_frames('gripper', 'world') * delta_T_up * delta_T
        T_shake_down = YMC.L_PREGRASP_POSE.as_frames('gripper', 'world') * delta_T_down * delta_T

        for i in range(5):
            y.left.goto_pose(T_shake_up, wait_for_res=False)
            y.left.goto_pose(YMC.L_PREGRASP_POSE, wait_for_res=True)
            y.left.goto_pose(T_shake_down, wait_for_res=False)
            y.left.goto_pose(YMC.L_PREGRASP_POSE, wait_for_res=True)


    elif (num == 4):
        y.set_v(500)
        radius = 0.2
        angle = np.pi / 64
        delta_T = RigidTransform(translation=[0,0,radius], from_frame='gripper', to_frame='gripper')
        R_shake = np.array([[1, 0, 0],
                            [0, np.cos(angle), -np.sin(angle)],
                            [0, np.sin(angle), np.cos(angle)]])
        delta_T_up = RigidTransform(rotation=R_shake, translation=[0,0,-radius], from_frame='gripper', to_frame='gripper')
        delta_T_down = RigidTransform(rotation=R_shake.T, translation=[0,0,-radius], from_frame='gripper', to_frame='gripper')
        T_shake_up = YMC.L_PREGRASP_POSE.as_frames('gripper', 'world') * delta_T_up * delta_T
        T_shake_down = YMC.L_PREGRASP_POSE.as_frames('gripper', 'world') * delta_T_down * delta_T

        for i in range(10):
            y.left.goto_pose(T_shake_up, wait_for_res=False)
            y.left.goto_pose(YMC.L_PREGRASP_POSE, wait_for_res=True)
            y.left.goto_pose(T_shake_down, wait_for_res=False)
            y.left.goto_pose(YMC.L_PREGRASP_POSE, wait_for_res=True)

    elif (num == 5):
        y.set_v(300)
        robot_action.plate_catch(y)
        robot_action.plate_drop(y)

    elif (num == 6):
        y.set_v(500)
        y.right.goto_pose(RigidTransform(translation = [0.32, -0.2, 0.1], rotation = right_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, 0.2, 0.2], rotation = left_side_rotation))
        time.sleep(1)
        y.right.close_gripper()
        y.left.close_gripper()
        time.sleep(1)
        y.right.goto_pose(RigidTransform(translation = [0.32, 0.1, 0.1], rotation = right_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, -0.1, 0.2], rotation = left_side_rotation))
        time.sleep(1)
        y.right.open_gripper()
        y.left.open_gripper()

    elif (num == 7):
        y.set_v(300)
        y.left.goto_pose(RigidTransform(translation = [0.32, 0.1, 0.1], rotation = left_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, -0.1, 0.1], rotation = left_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.52, -0.1, 0.1], rotation = left_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.52, -0.1, 0.3], rotation = left_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, -0.1, 0.3], rotation = left_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, -0.1, 0.1], rotation = left_side_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, 0.1, 0.1], rotation = left_side_rotation))

    elif (num == 8):
        y.set_v(200)
        y.left.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = left_front_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.32, 0, 0.07], rotation = left_front_rotation))
        time.sleep(3)
        y.left.close_gripper()
        y.left.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = left_front_rotation))
        y.left.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = left_front_rotation))
        time.sleep(3)
        y.left.open_gripper()

    elif (num == 9):
        y.set_v(150)
        y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.065], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.1], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))

    elif num == 10:
        y.set_v(150)
        robot_action.plate_push_catch(y)
        robot_action.plate_push_give(y)
        robot_action.plate_push_give_2(y)

    time.sleep(1)
    os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
    time.sleep(5)

    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(3, 0, 0, 0, time_diff)
    time.sleep(5)
    write_log.write_log(4, 0, 0, 0, time_diff)
    os.system('play -nq -t alsa synth {} sine {}'.format(1, 880))

if __name__ == '__main__':
    ######################################################################
    global time_diff
    timeServer = 'time.windows.com'
    c = ntplib.NTPClient()
    response = c.request(timeServer, version=3)
    time_diff = response.offset
    ######################################################################
    y = YuMiRobot()
    y.set_z('z50')
    ######################################################################
    left_top_rotation = rpy_to_wxyz(-90, 0, 180)
    left_front_rotation = rpy_to_wxyz(-90, 0, -90)
    left_side_rotation = rpy_to_wxyz(0, 0, -90)
    right_top_rotation = rpy_to_wxyz(90, 0, 180)
    right_side_rotation = rpy_to_wxyz(0, 0, 90)
    right_front_rotation = rpy_to_wxyz(90, 0, 90)
    right_top_give_rotation = rpy_to_wxyz(90, 0, 210)
    right_side_give_rotation = rpy_to_wxyz(0, 30, 90)
    right_front_give_rotation = rpy_to_wxyz(90, 0, 120)
    ######################################################################
    y.reset_home()
    y.open_grippers()

    for i in range (10):
        input_work_train(i + 1)
        raw_input("Press Enter to continue...")
    
    print("End of training")
    y.reset_home()
    y.open_grippers()
    y.stop()