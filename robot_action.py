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

def plate_catch(self):
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.2], rotation = right_front_rotation))
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.07], rotation = right_front_rotation))
    time.sleep(3)
    self.right.close_gripper()
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.2], rotation = right_front_rotation))

def plate_drop(self):
    self.right.goto_pose(RigidTransform(translation = [0.72, 0, 0.35], rotation = right_front_rotation))
    time.sleep(3)
    self.right.open_gripper()
    self.right.goto_pose(RigidTransform(translation = [0.4, 0, 0.3], rotation = right_front_rotation))

def plate_slide(self):
    self.right.goto_pose(RigidTransform(translation = [0.72, 0, 0.35], rotation = right_front_rotation))
    time.sleep(3)
    self.right.goto_pose(RigidTransform(translation = [0.75, 0, 0.35], rotation = right_front_give_rotation))
    
def plate_slide_2(self):    
    # self.right.goto_pose(RigidTransform(translation = [0.72, 0, 0.35], rotation = right_front_rotation))
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.25], rotation = right_front_rotation))
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.07], rotation = right_front_rotation))
    time.sleep(3)
    self.right.open_gripper()
    self.right.goto_pose(RigidTransform(translation = [0.33, 0, 0.2], rotation = right_front_rotation))

def plate_push_catch(self):
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.2], rotation = right_front_rotation))
    self.right.goto_pose(RigidTransform(translation = [0.3, 0, 0.07], rotation = right_front_rotation))
    time.sleep(3)

def plate_push_give(self):
    self.right.goto_pose(RigidTransform(translation = [0.65, 0, 0.07], rotation = right_front_rotation))

def plate_push_give_2(self):
    self.right.goto_pose(RigidTransform(translation = [0.65, 0, 0.2], rotation = right_front_rotation))


# example of rigid transform: RigidTransform(translation = [x_pos(back to front), y_pos(right to left), z_pos], rotation=[w, x, y, z])
# To use rpy rotation, function rpy_to_wxyz(r, p, y) is implemented above
left_top_rotation = rpy_to_wxyz(-90, 0, 180)
left_front_rotation = rpy_to_wxyz(-90, 0, -90)
left_side_rotation = rpy_to_wxyz(0, 0, -90)
right_top_rotation = rpy_to_wxyz(90, 0, 180)
right_side_rotation = rpy_to_wxyz(0, 0, 90)
right_front_rotation = rpy_to_wxyz(90, 0, 90)
right_top_give_rotation = rpy_to_wxyz(90, 0, 210)
right_side_give_rotation = rpy_to_wxyz(0, 30, 90)
right_front_give_rotation = rpy_to_wxyz(90, 0, 120)

if __name__ == '__main__':
    y = YuMiRobot()
    y.set_z('z50')
    y.set_v(450)

    print('robot_action.py')
    y.open_grippers()
    y.reset_home()    
    
    plate_catch(y)
    plate_drop(y)

    y.reset_home()
    y.open_grippers()
    y.stop()
