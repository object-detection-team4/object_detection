import yaml
import numpy as np

def read_yaml_file(path):
    with open(path, "r",) as f:
        calibration_json = yaml.safe_load(f)

    intrinsic = np.array(calibration_json["camera_matrix"]['data'])
    # print("camera_matrix\n", intrinsic)
    extrinsic = np.array(calibration_json["distortion_coefficients"]['data'])
    # print("extrinsic\n", extrinsic)
    homography = np.array(calibration_json["homography_matrix"]['data'])
    # print("homography\n", homography)

    return intrinsic, extrinsic, homography

"""
    [
        [fx, 0, cx = u0],
        [0, fy, cy = v0],
        [0,  0,  1]
    ]
"""

def parse_intrinsic_calibration(intrinsic):
    fx = intrinsic["fx"]
    fy = intrinsic["fy"]
    cx = intrinsic["u0"]
    cy = intrinsic["v0"]
    camera_matrix = np.zeros([3, 3], dtype=np.float32)
    camera_matrix[0][0] = fx
    camera_matrix[0][2] = cx
    camera_matrix[1][1] = fy
    camera_matrix[1][2] = cy
    camera_matrix[2][2] = 0.0

    return camera_matrix
