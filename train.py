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

def input_work_train(speed, catching_dir, pos, job):
    if (speed == 1):
        spd = 150
        y.set_v(spd)
    elif (speed == 2):
        spd = 500
        y.set_v(spd)
    elif (speed == 3):
        spd = 1500
        y.set_v(spd)

    y.reset_home()

    if (job == 1):
        write_log.write_log(1, 0, spd, catching_dir, pos, time_diff)
        robot_action.bottle_catch(y, catching_dir, pos)
    elif (job == 2):
        write_log.write_log(1, 0, spd, catching_dir, pos, time_diff)
        robot_action.bottle_catch(y, catching_dir, pos)
        write_log.write_log(2, 0, spd, catching_dir, pos, time_diff)
        robot_action.bottle_give(y, catching_dir, pos)
    
    time.sleep(1)
    os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
    time.sleep(5)

    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(3, 0, spd, catching_dir, pos, time_diff)
    time.sleep(5)
    os.system('play -nq -t alsa synth {} sine {}'.format(1, 880))
    write_log.write_log(4, 0, spd, catching_dir, pos, time_diff)

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
    y.reset_home()
    y.open_grippers()
    
    if os.path.isfile(write_log.file_name):
        pass
    else:
        f = open(write_log.file_name, 'w')
        f.close()

    if os.path.isfile('random_train.txt'):
        pass
    else:
        f = open('random_train.txt', 'w')

        rand_list = [(1, 1, 1, 1), (1, 2, 1, 1), (1, 3, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1), (2, 3, 1, 1), (3, 1, 1, 1), (3, 2, 1, 1), (3, 3, 1, 1),
                     (1, 1, 1, 2), (1, 1, 2, 2), (1, 1, 3, 2), (1, 2, 1, 2), (1, 2, 2, 2), (1, 2, 3, 2), (1, 3, 1, 2), (1, 3, 2, 2), (1, 3, 3, 2),
                     (2, 1, 1, 2), (2, 1, 2, 2), (2, 1, 3, 2), (2, 2, 1, 2), (2, 2, 2, 2), (2, 2, 3, 2), (2, 3, 1, 2), (2, 3, 2, 2), (2, 3, 3, 2),
                     (3, 1, 1, 2), (3, 1, 2, 2), (3, 1, 3, 2), (3, 2, 1, 2), (3, 2, 2, 2), (3, 2, 3, 2), (3, 3, 1, 2), (3, 3, 2, 2), (3, 3, 3, 2)]
        used_list = []

        for i in range (len(rand_list)):
            used_list.append(rand_list.pop(rand_list.index(random.choice(rand_list))))
            ran_str = str(used_list[i])
            f.writelines(ran_str + os.linesep)
        f.close()
    
    f = open(write_log.file_name, 'r')
    lines = f.readlines()
    f.close()
    case_num = 1

    for line in lines:
        if 'catching' in line:
            case_num += 1

    while (case_num <= 36):
        f = open(write_log.file_name, 'r')
        lines = f.readlines()
        f.close()
        case_num = 1

        for line in lines:
            if 'catching' in line:
                case_num += 1

        f = open('random_train.txt', 'r')
        cnt = 0

        for x in f:
            cnt += 1
            if (cnt == case_num):
                speed = int(x[1])
                catching_dir = int(x[4])
                pos = int(x[7])
                job = int(x[10])
        f.close()

        print(case_num)
        input_work_train(speed, catching_dir, pos, job)

        raw_input("Press Enter to continue...")
    
    print("End of training")
    y.reset_home()
    y.open_grippers()
    y.stop()