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

import write_log
import robot_action
import speed_optimization

def input_work_bottle(catching_speed, giving_speed, catching_dir, pos):
    y.set_v(catching_speed)
    write_log.write_log(1, 1, catching_speed, catching_dir, pos, time_diff)
    robot_action.bottle_catch(y, catching_dir, pos)
    y.set_v(giving_speed)
    write_log.write_log(2, 1, giving_speed, catching_dir, pos, time_diff)
    robot_action.bottle_give(y, catching_dir, pos)
    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(3, None, None, None, None, time_diff)
    time.sleep(5)
    write_log.write_log(4, 0, 0, 0, 0, time_diff)

def input_work_water(catching_speed, giving_speed, catching_dir, pos):
    y.set_v(catching_speed)
    write_log.write_log(1, 2, catching_speed, catching_dir, pos, time_diff)
    robot_action.water_catch(y, catching_dir, pos)
    y.set_v(giving_speed)
    write_log.write_log(2, 2, giving_speed, catching_dir, pos, time_diff)
    robot_action.water_give(y, catching_dir, pos)
    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(3, None, None, None, None, time_diff)
    time.sleep(5)
    write_log.write_log(4, 0, 0, 0, 0, time_diff)

def input_work_plate(catching_speed, giving_speed, catching_dir, pos):
    y.set_v(catching_speed)
    write_log.write_log(1, 3, catching_speed, catching_dir, pos, time_diff)
    robot_action.plate_catch(y, catching_dir, pos)
    y.set_v(giving_speed)
    write_log.write_log(2, 3, giving_speed, catching_dir, pos, time_diff)
    robot_action.plate_give(y, catching_dir, pos)
    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(3, None, None, None, None, time_diff)
    time.sleep(5)
    write_log.write_log(4, 0, 0, 0, 0, time_diff)

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
    ####################################################
    # input_work_bottle(c_s, g_s, 2, 2)
    # input_work_water(c_s, g_s, 2, 2)
    # input_work_plate(c_s, g_s, 3, 2)

    choice = raw_input("Choose task to do (1: speed with feedback, 2: speed without feedback, 3: position) : ")

    if (choice == '1'):
        count = 0
        temp = 1
        while (True):
            if (count >= 10):
                break
            f = open(write_log.file_name.split('.')[0] + '_score.txt')
            num_lines = sum(1 for line in f)
            f.close()
            if ((temp == 1) or ((num_lines % 6 == 0) and (num_lines > temp))):
                count += 1
                print("Test count : %d" %count)
                temp = num_lines
                [b_c, b_g, w_c, w_g, p_c, p_g] = speed_optimization.speed_optimizer()
                input_work_bottle(b_c, b_g, 2, 2)
                raw_input("Press Enter to continue...")
                input_work_water(w_c, w_g, 2, 2)
                raw_input("Press Enter to continue...")
                input_work_plate(p_c, p_g, 3, 2)
                raw_input("Press Enter to continue...")
                y.reset_home()

    if (choice == '2'):
        count = 0
        for i in range (10):
            count += 1
            print("Train count : %d" %count)
            [b_c, b_g, w_c, w_g, p_c, p_g] = [300, 300, 300, 300, 300, 300]
            input_work_bottle(b_c, b_g, 2, 2)
            raw_input("Press Enter to continue...")
            input_work_water(w_c, w_g, 2, 2)
            raw_input("Press Enter to continue...")
            input_work_plate(p_c, p_g, 3, 2)
            raw_input("Press Enter to continue...")
            y.reset_home()
    
    elif (choice == '3'):
        [b_c, b_g, w_c, w_g, p_c, p_g] = speed_optimization.speed_optimizer()
        input_work_bottle(b_c, b_g, 2, 1)
        raw_input("Press Enter to continue...")
        input_work_water(w_c, w_g, 2, 1)
        raw_input("Press Enter to continue...")
        input_work_plate(p_c, p_g, 3, 1)
        raw_input("Press Enter to continue...")
        input_work_bottle(b_c, b_g, 2, 2)
        raw_input("Press Enter to continue...")
        input_work_water(w_c, w_g, 2, 2)
        raw_input("Press Enter to continue...")
        input_work_plate(p_c, p_g, 3, 2)
        raw_input("Press Enter to continue...")
        input_work_bottle(b_c, b_g, 2, 3)
        raw_input("Press Enter to continue...")
        input_work_water(w_c, w_g, 2, 3)
        raw_input("Press Enter to continue...")
        input_work_plate(p_c, p_g, 3, 3)
        raw_input("Press Enter to continue...")
        y.reset_home()

    y.reset_home()
    y.stop()

