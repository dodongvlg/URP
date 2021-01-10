from autolab_core import RigidTransform
import numpy as np

from yumipy import YuMiRobot, YuMiState
from yumipy import YuMiConstants as YMC

from scipy.spatial.transform import Rotation
import time
from datetime import datetime
import os
import ntplib
import write_log
import random
from pathlib import Path

def calibrate_grippers(): # Calibrate grippers
    y.calibrate_grippers()
    y.open_grippers()

def reset_pose(): # Go to home pose : Make sure to run this function before turning off the robot, for faster calibration next time
    y.reset_home()
    y.open_grippers()

def stop_robot():
    y.stop()

def rpy_to_wxyz(r, p, y): # Change euler angle to quaternion
    rot = Rotation.from_euler('xyz', [r, p, y], degrees = True)
    return rot.as_quat()

def wxyz_to_rpy (w, x, y, z): # Change quaternion to euler angle
    rot = Rotation.from_quat([w, x, y, z])
    return rot.as_euler('xyz', degrees = True)

def catch(catching_dir, pos):
    if (pos == 3):
        if (catching_dir == 1):
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.close_gripper()
            return
        elif (catching_dir == 2):
            y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))
            time.sleep(3)
            return
        elif (catching_dir == 3):
            y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            return
        
    if (catching_dir == 1): # top 
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.06], rotation = right_top_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.2], rotation = right_side_rotation))
    else: # front
        y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.07], rotation = right_front_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))

def give(catching_dir, pos):
    if (catching_dir == 1): # top
        if (pos == 1):
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.07], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
        elif (pos == 2):
            y.right.goto_pose(RigidTransform(translation = [0.63, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
        else: # push
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        if (pos == 1):
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.2], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
        elif (pos == 2):
            y.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            y.right.open_gripper()
        else: # push
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
    else: # front
        if (pos == 1):
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.07], rotation = right_front_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
        elif (pos == 2):
            y.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            y.right.open_gripper()
        else: # push
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))


def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results

def file_len(fname):
    length = sum(1 for line in open(fname))
    return length

def main_work():
    y.reset_home()
    y.calibrate_grippers()
    y.open_grippers()
    count = 1

    for speed in [1, 3]:
        if (speed == 1):
            y.set_v(150)
        elif (speed == 2):
            y.set_v(300)
        elif (speed == 3):
            y.set_v(1000)
        
        for catching_dir in [1, 2, 3]:
            for pos in [1, 2, 3]:
                print(count)
                count += 1
                write_log.write_log(1, speed, 2, catching_dir, pos, time_diff)
                catch(catching_dir, pos)
                give(catching_dir, pos)
                y.reset_home()
                y.right.open_gripper()
                write_log.write_log(2, None, None, None, None, time_diff)
                time.sleep(5)
        
    write_log.write_log(3, None, 2, None, None, time_diff)

def input_work(speed, catching_dir, pos):
    if (speed == 1):
        y.set_v(150)
    elif (speed == 2):
        y.set_v(300)
    elif (speed == 3):
        y.set_v(700)
    elif (speed == 4):
        y.set_v(1200)

    y.reset_home()
    write_log.write_log(1, speed, 2, catching_dir, pos, time_diff)
    catch(catching_dir, pos)
    write_log.write_log(7, speed, 2, catching_dir, pos, time_diff)
    give(catching_dir, pos)
    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(2, None, None, None, None, time_diff)
    time.sleep(5)

if __name__ == '__main__':
    ######################################################################
    global time_diff
    y = YuMiRobot()
    y.set_z('z50')
    
    # example of rigid transform: RigidTransform(translation = [x_pos(back to front), y_pos(right to left), z_pos], rotation=[w, x, y, z])
    # To use rpy rotation, function rpy_to_wxyz(r, p, y) is implemented above
    left_top_rotation = rpy_to_wxyz(-90, 0, 180)
    left_front_rotation = rpy_to_wxyz(-90, 0, -90)
    left_side_rotation = rpy_to_wxyz(0, 0, -90)
    right_top_rotation = rpy_to_wxyz(90, 0, 180)
    right_side_rotation = rpy_to_wxyz(0, 0, 90)
    right_front_rotation = rpy_to_wxyz(90, 0, 90)
    ######################################################################
    
    timeServer = 'time.windows.com' 
    c = ntplib.NTPClient() 
    response = c.request(timeServer, version=3)
    time_diff = response.offset
    ######################################################################
    # main_work()

    y.reset_home()
    # y.calibrate_grippers()
    y.open_grippers()
    
    if os.path.isfile(write_log.file_name):
        pass
    else:
        f = open(write_log.file_name, 'w')
        f.close()

    if os.path.isfile('random_test2.txt'):
        pass
    else:
        f = open('random_test2.txt', 'w')
        rand_list = [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3),
                     (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3),
                     (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1), (3, 3, 2), (3, 3, 3),
                     (4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 2), (4, 2, 3), (4, 3, 1), (4, 3, 2), (4, 3, 3)]
        used_list = []

        for i in range (len(rand_list)):
            used_list.append(rand_list.pop(rand_list.index(random.choice(rand_list))))
            ran_str = str(used_list[i])
            f.writelines(ran_str + os.linesep)
        f.close()
    
    if (file_len(write_log.file_name) != 0):
        with open(write_log.file_name, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            if ("catching" in last_line):
                write_log.write_log(4, None, None, None, None, time_diff)
                write_log.write_log(4, None, None, None, None, time_diff)
            if ("giving" in last_line):
                write_log.write_log(4, None, None, None, None, time_diff)

    while (True):
        zero_line = (search_string_in_file(write_log.file_name, 'end, train'))[0][0]
        total_line = file_len(write_log.file_name)
        case_num = - (- (total_line - zero_line) / 3) + 1

        if (case_num > 24):
            break

        f = open('random_test2.txt', 'r')
        cnt = 0
        for x in f:
            cnt += 1
            if (cnt == case_num):
                speed = int(x[1])
                catching_dir = int(x[4])
                pos = int(x[7])
        f.close()

        print(case_num)
        input_work(speed, catching_dir, pos)

        raw_input("Press Enter to continue...")

    write_log.write_log(3, None, 2, None, None, time_diff)
    y.reset_home()
    y.stop()