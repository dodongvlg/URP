from autolab_core import RigidTransform
import numpy as np

from yumipy import YuMiRobot, YuMiState
from yumipy import YuMiConstants as YMC

if __name__ == '__main__':
    y = YuMiRobot()
    y.set_z('z50')
    y.set_v(300)

    y.reset_home()
    y.calibrate_grippers()
    y.open_grippers()
    y.stop()