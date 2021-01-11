from autolab_core import RigidTransform
from yumipy import YuMiRobot, YuMiState
from yumipy import YuMiConstants as YMC
from scipy.spatial.transform import Rotation
import time

def calibrate_grippers():  # Calibrate grippers
    y.calibrate_grippers()
    y.open_grippers()

def reset_pose():  # Go to home pose : Make sure to run this function before turning off the robot, for faster calibration next time
    y.reset_home()
    y.open_grippers()

def stop_robot():
    y.stop()

def rpy_to_wxyz(r, p, y):  # Change euler angle to quaternion
    rot = Rotation.from_euler('xyz', [r, p, y], degrees=True)
    return rot.as_quat()

def wxyz_to_rpy(w, x, y, z):  # Change quaternion to euler angle
    rot = Rotation.from_quat([w, x, y, z])
    return rot.as_euler('xyz', degrees=True)

def bottle_catch(catching_dir, pos):
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

def bottle_give(catching_dir, pos):
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

def fullbottle_catch(catching_dir, pos):
    if (pos == 3):
        if (catching_dir == 1):
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.close_gripper()
            return
        elif (catching_dir == 2):
            y.right.goto_pose(RigidTransform(translation = [0.28, -0.1, 0.07], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            return
        elif (catching_dir == 3):
            y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            return

    if (catching_dir == 1):  # top
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.06], rotation = right_top_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    elif (catching_dir == 2):  # side
        y.right.goto_pose(RigidTransform(translation = [0.28, -0.1, 0.07], rotation = right_side_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.07], rotation = right_side_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.2], rotation = right_side_rotation))
    else:  # front
        y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.07], rotation = right_front_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))

def fullbottle_give(catching_dir, pos):
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

def plate_catch(catching_dir, pos):
    if (pos == 3):
        if (catching_dir == 1):
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.close_gripper()
            return
        elif (catching_dir == 2):
            y.right.goto_pose(RigidTransform(translation = [0.22, -0.1, 0.06], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.22, 0.04, 0.06], rotation = right_side_rotation))
            time.sleep(3)
            return
        elif (catching_dir == 3):
            y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.063], rotation = right_front_rotation))
            time.sleep(3)
            return

    if (catching_dir == 1):  # top
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.01], rotation = right_top_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    elif (catching_dir == 2):  # side
        y.right.goto_pose(RigidTransform(translation = [0.28, -0.1, 0.06], rotation = right_side_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.06], rotation = right_side_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.2], rotation = right_side_rotation))
    else:  # front
        y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
        y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.058], rotation = right_front_rotation))
        time.sleep(3)
        y.right.close_gripper()
        y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))

def plate_give(catching_dir, pos):
    if (catching_dir == 1): # top
        if (pos == 1):
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.05], rotation = right_top_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.07], rotation = right_top_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.01], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        elif (pos == 2):
            y.right.goto_pose(RigidTransform(translation = [0.58, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.58, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.01], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        else: # push
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        if (pos == 1):
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.2], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.1], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.1], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.06], rotation = right_side_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.2], rotation = right_side_rotation))
        elif (pos == 2):
            y.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.06], rotation = right_side_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.2], rotation = right_side_rotation))
        else: # push
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.06], rotation = right_side_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
    else: # front
        if (pos == 1):
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.1], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.1], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.1], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.058], rotation = right_front_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
        elif (pos == 2):
            y.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
            y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.058], rotation = right_front_rotation))
            time.sleep(3)
            y.right.open_gripper()
            y.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
        else: # push
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.063], rotation = right_front_rotation))
            time.sleep(3)
            y.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))

# example of rigid transform: RigidTransform(translation = [x_pos(back to front), y_pos(right to left), z_pos], rotation=[w, x, y, z])
# To use rpy rotation, function rpy_to_wxyz(r, p, y) is implemented above
left_top_rotation = rpy_to_wxyz(-90, 0, 180)
left_front_rotation = rpy_to_wxyz(-90, 0, -90)
left_side_rotation = rpy_to_wxyz(0, 0, -90)
right_top_rotation = rpy_to_wxyz(90, 0, 180)
right_side_rotation = rpy_to_wxyz(0, 0, 90)
right_front_rotation = rpy_to_wxyz(90, 0, 90)