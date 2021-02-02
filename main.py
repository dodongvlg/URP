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

def input_work_empty(catching_speed, giving_speed):
    y.set_v(catching_speed)
    write_log.write_log(1, 1, catching_speed, 1, time_diff)
    robot_action.plate_catch(y)
    y.set_v(giving_speed)
    write_log.write_log(2, 1, giving_speed, 1, time_diff)
    robot_action.plate_drop(y)
    y.reset_home()
    y.right.open_gripper()
    # write_log.write_log(3, None, None, None, time_diff)
    # time.sleep(5)

def input_work_full(catching_speed, giving_speed):
    y.set_v(catching_speed)
    write_log.write_log(1, 2, catching_speed, 1, time_diff)
    robot_action.plate_catch(y)
    y.set_v(giving_speed)
    write_log.write_log(2, 2, giving_speed, 1, time_diff)
    robot_action.plate_drop(y)
    y.reset_home()
    y.right.open_gripper()
    # write_log.write_log(3, None, None, None, time_diff)
    # time.sleep(5)

def input_work_cookie(catching_speed, giving_speed):
    y.set_v(catching_speed)
    write_log.write_log(1, 3, catching_speed, 1, time_diff)
    robot_action.plate_catch(y)
    y.set_v(giving_speed)
    write_log.write_log(2, 3, giving_speed, 1, time_diff)
    robot_action.plate_slide(y)
    # y.reset_home()
    # y.right.open_gripper()
    # write_log.write_log(3, None, None, Non, time_diff)
    # time.sleep(5)

def input_work_cookie_2(catching_speed, giving_speed):
    y.set_v(catching_speed)
    robot_action.plate_slide_2(y)
    y.reset_home()
    y.right.open_gripper()

def input_work_push(catching_speed, giving_speed, obj):
    y.set_v(catching_speed)
    write_log.write_log(1, obj, catching_speed, 2, time_diff)
    robot_action.plate_push_catch(y)
    y.set_v(giving_speed)
    write_log.write_log(2, obj, giving_speed, 2, time_diff)
    robot_action.plate_push_give(y)
    y.reset_home()
    y.right.open_gripper()
    # write_log.write_log(3, None, None, None, time_diff)
    # time.sleep(5)


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
    print(1)
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
                input_work_empty(b_c, b_g)
                raw_input("Press Enter to continue...")
                input_work_full(w_c, w_g)
                raw_input("Press Enter to continue...")
                input_work_cookie(p_c, p_g)
                raw_input("Press Enter to continue...")
                y.reset_home()

    elif (choice == '2'):
        count = 0
        for i in range (2):
            count += 1
            print("Train count : %d" %count)
            [e_c, e_g, f_c, f_g, c_c, c_g] = [300, 300, 300, 300, 300, 300]
            [e_c_p, e_g_p, f_c_p, f_g_p, c_c_p, c_g_p] = [300, 300, 300, 300, 300, 300]
            raw_input("Press Enter to continue...")
            input_work_empty(e_c, e_g)
            raw_input("Press Enter to end task...")
            write_log.write_log(4, 0, 0, None, time_diff)
            raw_input("Press Enter to continue...")
            input_work_full(f_c, f_g)
            raw_input("Press Enter to end task...")
            write_log.write_log(4, 0, 0, None, time_diff)
            raw_input("Press Enter to continue...")
            input_work_cookie(c_c, c_g)
            raw_input("Press Enter to end task...")
            input_work_cookie_2(c_c, c_g)
            write_log.write_log(4, 0, 0, None, time_diff)

            raw_input("Press Enter to continue...")
            input_work_push(e_c_p, e_g_p, 1)
            raw_input("Press Enter to end task...")
            write_log.write_log(4, 0, 0, None, time_diff)
            raw_input("Press Enter to continue...")
            input_work_push(f_c_p, f_g_p, 2)
            raw_input("Press Enter to end task...")
            write_log.write_log(4, 0, 0, None, time_diff)
            raw_input("Press Enter to continue...")
            input_work_push(c_c_p, c_g_p, 3)
            raw_input("Press Enter to end task...")
            write_log.write_log(4, 0, 0, None, time_diff)
            
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

