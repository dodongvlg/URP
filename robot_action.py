from autolab_core import RigidTransform
from yumipy import YuMiRobot, YuMiState
from yumipy import YuMiConstants as YMC
from scipy.spatial.transform import Rotation
import time

def calibrate_grippers(self):  # Calibrate grippers
    self.calibrate_grippers()
    self.open_grippers()

def reset_pose(self):  # Go to home pose : Make sure to run this function before turning off the robot, for faster calibration next time
    self.reset_home()
    self.open_grippers()

def stop_robot(self):
    self.stop()

def rpy_to_wxyz(r, p, y):  # Change euler angle to quaternion
    rot = Rotation.from_euler('xyz', [r, p, y], degrees=True)
    return rot.as_quat()

def wxyz_to_rpy(w, x, y, z):  # Change quaternion to euler angle
    rot = Rotation.from_quat([w, x, y, z])
    return rot.as_euler('xyz', degrees=True)

def bottle_catch(self, catching_dir, pos):
    if (pos == 3):
        if (catching_dir == 1):
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            self.right.close_gripper()
            return
        elif (catching_dir == 2):
            self.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))
            time.sleep(3)
            return
        elif (catching_dir == 3):
            self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            return

    if (catching_dir == 1): # top
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.06], rotation = right_top_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        self.right.goto_pose(RigidTransform(translation = [0.28, -0.1 , 0.07], rotation = right_side_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.07], rotation = right_side_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.2], rotation = right_side_rotation))
    else: # front
        self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.07], rotation = right_front_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))

def bottle_give(self, catching_dir, pos):
    if (catching_dir == 1): # top
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.065], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.63, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.2], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            self.right.open_gripper()
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
    else: # front
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.07], rotation = right_front_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            self.right.open_gripper()
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))

def water_catch(self, catching_dir, pos):
    if (pos == 3):
        if (catching_dir == 1):
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            self.right.close_gripper()
            return
        elif (catching_dir == 2):
            self.right.goto_pose(RigidTransform(translation = [0.28, -0.1, 0.07], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            return
        elif (catching_dir == 3):
            self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            return

    if (catching_dir == 1):  # top
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.06], rotation = right_top_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    elif (catching_dir == 2):  # side
        self.right.goto_pose(RigidTransform(translation = [0.28, -0.1, 0.07], rotation = right_side_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.07], rotation = right_side_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.2], rotation = right_side_rotation))
    else:  # front
        self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.07], rotation = right_front_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))

def water_give(self, catching_dir, pos):
    if (catching_dir == 1): # top
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.065], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.63, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.2], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            self.right.open_gripper()
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.07], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
    else: # front
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.07], rotation = right_front_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            self.right.open_gripper()
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.065], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))

def plate_catch(self, catching_dir, pos):
    if (pos == 3):
        if (catching_dir == 1):
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.22, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            self.right.close_gripper()
            return
        elif (catching_dir == 2):
            self.right.goto_pose(RigidTransform(translation = [0.22, -0.1, 0.06], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.22, 0.04, 0.06], rotation = right_side_rotation))
            time.sleep(3)
            return
        elif (catching_dir == 3):
            self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.32, 0, 0.063], rotation = right_front_rotation))
            time.sleep(3)
            return

    if (catching_dir == 1):  # top
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.01], rotation = right_top_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
    elif (catching_dir == 2):  # side
        self.right.goto_pose(RigidTransform(translation = [0.28, -0.1, 0.06], rotation = right_side_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.06], rotation = right_side_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.28, 0.04, 0.2], rotation = right_side_rotation))
    else:  # front
        self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
        self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.058], rotation = right_front_rotation))
        time.sleep(3)
        self.right.close_gripper()
        self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))

def plate_give(self, catching_dir, pos):
    if (catching_dir == 1): # top
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.05], rotation = right_top_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.07], rotation = right_top_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.01], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.58, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.58, 0, 0.3], rotation = right_top_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.01], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.28, 0, 0.2], rotation = right_top_rotation))
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.0], rotation = right_top_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.53, 0, 0.3], rotation = right_top_rotation))
    elif (catching_dir == 2): # side
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.2], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.1], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.1], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.06], rotation = right_side_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.2], rotation = right_side_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.57, 0.04, 0.3], rotation = right_side_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.06], rotation = right_side_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.28, 0.04 , 0.2], rotation = right_side_rotation))
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.06], rotation = right_side_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.47, 0.04, 0.3], rotation = right_side_rotation))
    else: # front
        if (pos == 1):
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.1], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.1], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.1], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.058], rotation = right_front_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
        elif (pos == 2):
            self.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.7, 0, 0.3], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
            self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.058], rotation = right_front_rotation))
            time.sleep(3)
            self.right.open_gripper()
            self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))
        else: # push
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.063], rotation = right_front_rotation))
            time.sleep(3)
            self.right.goto_pose(RigidTransform(translation = [0.6, 0, 0.2], rotation = right_front_rotation))

# example of rigid transform: RigidTransform(translation = [x_pos(back to front), y_pos(right to left), z_pos], rotation=[w, x, y, z])
# To use rpy rotation, function rpy_to_wxyz(r, p, y) is implemented above
left_top_rotation = rpy_to_wxyz(-90, 0, 180)
left_front_rotation = rpy_to_wxyz(-90, 0, -90)
left_side_rotation = rpy_to_wxyz(0, 0, -90)
right_top_rotation = rpy_to_wxyz(90, 0, 180)
right_side_rotation = rpy_to_wxyz(0, 0, 90)
right_front_rotation = rpy_to_wxyz(90, 0, 90)