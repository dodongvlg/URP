import time
from datetime import datetime
import os
import ntplib 
from time import ctime
import collections

global file_name

file_name = '/home/urp/experiment/log_MINUK_210110.txt'

def write_log(action, speed, obj, catching_dir, pos, time_diff):
    log = open(file_name, 'a')
    
    if (action == 2):
        action_str = "resting"
        log_str = "[%s], (%.4f) \n" %(action_str, (time.time() + time_diff))
        log.write(log_str)
        log.close()
        print("##########[%s]########## \n" %(action_str))
        return
    
    elif (action == 3):
        action_str = "end"
        if (obj == 1):
            obj_str = "bottle"
        elif (obj == 2):
            obj_str = "yogurt"
        elif (obj == 3):
            obj_str = "plate"
        elif (obj == 4):
            obj_str = "fullbottle"
        else:
            obj_str = "train"
        
        log_str = "[%s, %s], (%.4f) \n" %(action_str, obj_str, (time.time() + time_diff))
        log.write(log_str)
        log.close()
        print("##########%s %s########## \n" %(action_str, obj_str))
        return

    elif (action == 5) or (action == 6):
        if (speed == 1):
            speed_str = "150"
        elif (speed == 2):
            speed_str = "300"
        elif (speed == 3):
            speed_str = "700"
        else:
            speed_str = "1200"

        if (catching_dir == 1):
            catching_dir_str = "top"
        elif (catching_dir == 2):
            catching_dir_str = "side"
        else:
            catching_dir_str = "front"

        if (pos == 1):
            pos_str = "table"
        elif (pos == 2):
            pos_str = "hand"
        else:
            pos_str = "push"

        if (action == 5):
            action_str = "catching_train"
        else:
            action_str = "giving_train"

        obj_str = "train"
        
        log_str = "[%s, %s, %s, %s, %s], (%.4f) \n" %(action_str, speed_str, obj_str, catching_dir_str, pos_str, (time.time() + time_diff))
        log.write(log_str)
        log.close()
        print("##########[%s, %s, %s, %s, %s]########## \n" %(action_str, speed_str, obj_str, catching_dir_str, pos_str))
        return

    
    if (action == 4):
        action_str = "ADDING NULL"
        log_str = "[%s], (%.4f) \n" %(action_str, (time.time() + time_diff))
        log.write(log_str)
        log.close()
        return
        
    else:
        if (action == 1):
            action_str = "catching"
        if (action == 7):
            action_str = "giving"
    
    if (speed == 1):
        speed_str = "150"
    elif (speed == 2):
        speed_str = "300"
    elif (speed == 3):
        speed_str = "700"
    else:
        speed_str = "1200"

    if (obj == 1):
        obj_str = "bottle"
    elif (obj == 2):
        obj_str = "yogurt"
    elif (obj == 3):
        obj_str = "plate"
    else:
        obj_str = "fullbottle"
    
    if (catching_dir == 1):
        catching_dir_str = "top"
    elif (catching_dir == 2):
        catching_dir_str = "side"
    else:
        catching_dir_str = "front"

    if (pos == 1):
        pos_str = "table"
    elif (pos == 2):
        pos_str = "hand"
    else:
        pos_str = "push"
    
    log_str = "[%s, %s, %s, %s, %s], (%.4f) \n" %(action_str, speed_str, obj_str, catching_dir_str, pos_str, (time.time() + time_diff))
    log.write(log_str)
    log.close()
    print("##########[%s, %s, %s, %s, %s]########## \n" %(action_str, speed_str, obj_str, catching_dir_str, pos_str))