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

def choose_speed():
    global speed
    speed = input("Choose robot speed (slow: 1, medium: 2, fast: 3) : ")
    if (speed == 1):
        print("Slow Speed!")
        y.set_v(150)
    elif (speed == 2):
        print("Medium Speed!")
        y.set_v(300)
    elif (speed == 3):
        print("Fast Speed!")
        y.set_v(1000)
    else:
        print("Wrong Input!")
        choose_speed()

def choose_object():
    global obj
    obj= input("Choose what to pick up (cookie: 1, bottle: 2, yogurt: 3, dish: 4, can: 5) : ")
    if (obj == 1):
        print("Chose to pick up cookie!")
    elif (obj == 2):
        print("Chose to pick up bottle!")
    elif (obj == 3):
        print("Chose to pick up yogurt!")
    elif (obj == 4):
        print("Chose to pick up dish!")
    elif (obj == 5):
        print("Chose to pick up can!")
    else:
        print("Wrong Input!")
        choose_object()

def choose_catching_direction():
    global catching_dir
    catching_dir = input("Choose catching direction (top: 1, side: 2, front: 3) : ")
    if (catching_dir == 1):
        print("Catch from top!")
    elif (catching_dir == 2):
        print("Catch from side!")
    elif (catching_dir == 3):
        print("Catch from front!")
    else:
        print("Wrong Input!")
        choose_catching_direction()

def choose_giving_position():
    global pos
    pos = input("Choose giving position (on table: 1, to hand: 2, push: 3) : ")
    if (pos == 1):
        print("Leave object on table!") 
    elif (pos == 2):
        print("Give object to hand!")
    elif (pos == 3):
        print("Push to table!")
    else:
        print("Wrong Input!")
        choose_giving_position()

def catch():
    if (pos == 3):
        return None
        
    if (obj == 1): # cookie
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
    elif (obj == 1): # bottle
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
    else: # yogurt
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

def give():
    if (obj == 1): # cookie
        if (catching_dir == 1): # top
            if (pos == 1): # desk
                y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.06], rotation = right_top_rotation))
                time.sleep(3)
                y.right.open_gripper()
                y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
            elif (pos == 2): # hand
                y.right.goto_pose(RigidTransform(translation = [0.63, 0, 0.3], rotation = right_top_rotation))
                time.sleep(3)
                y.right.open_gripper()
            else: # push
                y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
                time.sleep(3)
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
                y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.28, 0.02 , 0.07], rotation = right_side_rotation))
                time.sleep(3)
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
                y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_front_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.065], rotation = right_front_rotation))
                time.sleep(3)
                y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.065], rotation = right_front_rotation))
                time.sleep(3)
                y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
    elif (obj == 2): # bottle
        if (catching_dir == 1): # top
            if (pos == 1):
                y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.065], rotation = right_top_rotation))
                time.sleep(3)
                y.right.open_gripper()
                y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
            elif (pos == 2):
                y.right.goto_pose(RigidTransform(translation = [0.63, 0, 0.3], rotation = right_top_rotation))
                time.sleep(3)
                y.right.open_gripper()
            else: # push
                y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
                time.sleep(3)
                y.right.close_gripper()
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
                y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))
                time.sleep(3)
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
                y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.065], rotation = right_front_rotation))
                time.sleep(3)
                y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.065], rotation = right_front_rotation))
                time.sleep(3)
                y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
    elif (obj == 3): # yogurt
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
                y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
                time.sleep(3)
                y.right.close_gripper()
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
                y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))
                time.sleep(3)
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
                y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
                y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.065], rotation = right_front_rotation))
                time.sleep(3)
                y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.065], rotation = right_front_rotation))
                time.sleep(3)
                y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
    elif (obj == 4): # dish
        if (catching_dir == 1): # top
            if (pos == 1):
                pass
            elif (pos == 2):
                pass
            else: # push
                pass
        elif (catching_dir == 2): # side
            if (pos == 1):
                pass
            elif (pos == 2):
                pass
            else: # push
                pass
        else: # front
            if (pos == 1):
                pass
            elif (pos == 2):
                pass
            else: # push
                pass
    else: # can
        if (catching_dir == 1): # top
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.close_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
        elif (catching_dir == 2): # side
            y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.01, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.01, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
        else: # front
            y.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.29, 0, 0.07], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.07], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))

# def write_log():
#     speed, obj, catching_dir, pos
#     if (speed == 1):
#         speed_str = "150"
#     elif (speed == 2):
#         speed_str = "300"
#     else:
#         speed_str = "1000"

#     if (obj == 1):
#         obj_str = "cookie"
#     elif (obj == 2):
#         obj_str = "bottle"
#     elif (obj == 3):
#         obj_str = "yogurt"
#     elif (obj == 4):
#         obj_str = "dish"
#     else:
#         obj_str = "can"
    
#     if (catching_dir == 1):
#         catching_dir_str = "top"
#     elif (catching_dir == 2):
#         catching_dir_str = "side"
#     else:
#         catching_dir_str = "front"

#     if (pos == 1):
#         pos_str = "table"
#     elif (pos == 2):
#         pos_str = "hand"
#     else:
#         pos_str = "push"

#     log = open('/home/urp/experiment/bbb.txt', 'a')
#     log_str = "[%s, %s, %s, %s], (%.4f) \n" %(speed_str, obj_str, catching_dir_str, pos_str, (time.time() + time_diff))
#     log.write(log_str)
#     log.close()
#     print("##########[%s, %s, %s, %s]########## \n" %(speed_str, obj_str, catching_dir_str, pos_str))

def main_work():
    y.reset_home()
    y.calibrate_grippers()
    y.open_grippers()

    while (True):
        choose_speed() # 3
        choose_object() # 3
        choose_catching_direction() # 3
        choose_giving_position() # 2

        write_log()

        catch()
        give()
        y.reset_home()
        y.open_grippers()

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
    

    time_str = "2020-11-10 16:33:00"
    timestamp = time.mktime(datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").timetuple())
    
    # log = open('/home/urp/experiment/robotlog.txt', 'a')
    timeServer = 'time.windows.com' 
    c = ntplib.NTPClient() 
    response = c.request(timeServer, version=3) 
    # log_str = "Time difference(Server time - Local time): %.4fs \n" %response.offset
    # log.write(log_str)
    # log.close()
    time_diff = response.offset
    ######################################################################
    # y.reset_home()
    y.set_v(300)
    # y.calibrate_grippers()
    # y.open_grippers()
    
    # while (time.time() < timestamp):
    #     continue

    # main_work()
    # y.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
    # y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))

    y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    # y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.06], rotation = right_top_rotation))

    y.reset_home()
    # write_log.write_log(3, None, 3, None, None, time_diff)
    y.stop()