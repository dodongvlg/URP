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

def input_work(obj, catching_speed, giving_speed, catching_dir, pos):
    # write_log(action, obj, speed, catching_dir, pos, time_diff)
    y.set_v(catching_speed) # Set catching speed
    write_log.write_log(1, obj, catching_speed, catching_dir, pos, time_diff) # Write 'catching'
    ##### Catch #####
    if (obj == 1):
        robot_action.bottle_catch(catching_dir, pos)
    elif (obj == 2):
        robot_action.fullbottle_catch(catching_dir, pos)
    elif (obj == 3):
        robot_action.plate_catch(catching_dir, pos)
    y.set_v(giving_speed)  # Set giving speed
    write_log.write_log(2, obj, giving_speed, catching_dir, pos, time_diff) # Write 'giving'
    ##### Give #####
    if (obj == 1):
        robot_action.bottle_give(catching_dir, pos)
    elif (obj == 2):
        robot_action.fullbottle_give(catching_dir, pos)
    elif (obj == 3):
        robot_action.plate_give(catching_dir, pos)
    y.reset_home()
    y.right.open_gripper()
    write_log.write_log(3, None, None, None, None, time_diff)
    time.sleep(5)
    write_log.write_log(4, obj, catching_speed, catching_dir, pos, time_diff)

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


