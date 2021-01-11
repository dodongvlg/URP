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
    train_num = input("Enter number for traning : ")

    for i in range (train_num):
        catching_speed = random.randint(150, 1500)
        giving_speed = random.randint(150, 1500)
        catching_dir = random.randint(1, 3)
        pos = random.randint(1, 3)
        job = random.randint(1, 2)

        if (job == 1):
            y.set_v(catching_speed)
            write_log.write_log(1, 0, catching_speed, catching_dir, pos, time_diff)
            robot_action.bottle_catch(y, catching_dir, pos)
        else:
            y.set_v(catching_speed)
            write_log.write_log(1, 0, catching_speed, catching_dir, pos, time_diff)
            robot_action.bottle_catch(y, catching_dir, pos)
            y.set_v(giving_speed)
            write_log.write_log(2, 0, giving_speed, catching_dir, pos, time_diff)
            robot_action.bottle_give(y, catching_dir, pos)

        time.sleep(1)
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
        time.sleep(5)

        y.reset_home()
        y.right.open_gripper()
        write_log.write_log(3, 0, catching_speed, catching_dir, pos, time_diff)
        time.sleep(5)
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 880))
        write_log.write_log(4, 0, catching_speed, catching_dir, pos, time_diff)

        raw_input("Press Enter to continue...")
    
    print("End of training")
    y.reset_home()
    y.open_grippers()
    y.stop()