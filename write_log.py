import time
from datetime import datetime
import os
import ntplib
from time import ctime
import collections

global file_name

file_name = 'log_MINUK_210110.txt'

def write_log(action, obj, speed, catching_dir, pos, time_diff):
    log = open(file_name, 'a')

    ############################## ACTION ##############################
    if (action == 1):
        action_str = "catching"
    elif (action == 2):
        action_str = "giving"
    elif (action == 3):
        action_str = "resting"
    elif (action == 4):
        action_str = "end"
    elif (action == 5):
        action_str = "ADDING_NULL"
    else:
        action_str = None

    ############################## SPEED ##############################
    if (speed != 0):
        speed_str = str(speed)
    else:
        speed_str = None

    ############################## OBJECT ##############################
    if (obj == 0):
        obj_str = "train"
    if (obj == 1):
        obj_str = "bottle"
    elif (obj == 2):
        obj_str = "water"
    elif (obj == 3):
        obj_str = "plate"
    else:
         obj_str = None

    ############################## CATCHING DIRECTION ##############################
    if (catching_dir == 1):
        catching_dir_str = "top"
    elif (catching_dir == 2):
        catching_dir_str = "side"
    elif (catching_dir == 3):
        catching_dir_str = "front"
    else:
        catching_dir_str = None

    ############################## GIVING POSITION ##############################
    if (pos == 1):
        pos_str = "table"
    elif (pos == 2):
        pos_str = "hand"
    elif (pos == 3):
        pos_str = "push"
    else:
        pos_str = None

    log_str = "[%s, %s, %s, %s, %s], (%.4f) \n" % (action_str, speed_str, obj_str, catching_dir_str, pos_str, (time.time() + time_diff))
    log.write(log_str)
    log.close()
    print("##########[%s, %s, %s, %s, %s]########## \n" % (action_str, speed_str, obj_str, catching_dir_str, pos_str))

if __name__ == '__main__':
    # write_log(action, speed, obj, catching_dir, pos, time_diff)
    write_log(1, 1, 1, 1, 1, 1)