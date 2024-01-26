#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Step A. homography distance estimation
import cv2
import numpy as np

import matplotlib.pyplot as plt

# import calibration_parser


def findHomography():
    # calibration_filepath = '../xycar_device/usb_cam/calibration/ost.yaml'
    # camera_matrix, _, _ = calibration_parser.read_yaml_file(calibration_filepath)

    image_points = np.array([
        [192, 190],
        [420, 189],
        [201, 205],
        [309, 205],
        [411, 203],
        [122, 231],
        [309, 232],
        [487, 227]
    ], dtype=np.float32)

    # X Y Z, X -> down, Z -> forward, Y -> Right
    object_points = np.array([
        [0.0, 180.0, 90.0],
        [0.0, 180.0, 450.0],
        [0.0, 360.0, 180.0],
        [0.0, 360.0, 270.0],
        [0.0, 360.0, 360.0],
        [0.0, 450.0, 180.0],
        [0.0, 450.0, 270.0],
        [0.0, 450.0, 360.0]
    ], dtype=np.float32) # z, y, x

    object_position = []

    DATA_SIZE = 8

    # object point
    # X: forward, Y: left, Z: 1
    homo_object_point = np.append(object_points[:,2:3], object_points[:,1:2], axis=1)
    homo_object_point = np.append(homo_object_point, np.ones([1, DATA_SIZE]).T, axis=1)

    # print("object_point : ", homo_object_point)

    homography, _ = cv2.findHomography(image_points, homo_object_point)
    print("homography matrix : ", homography)

    # (u, v) -> (u, v, 1)
    append_image_points = np.append(image_points.reshape(8, 2), np.ones([1, DATA_SIZE]).T, axis=1)
    # print(homography.shape)

    for image_point in append_image_points:
        # estimation point(object_point) -> homography * src(image_point)
        estimation_distance = np.dot(homography, image_point)

        x = estimation_distance[0]
        y = estimation_distance[1]
        z = estimation_distance[2]

        object_position.append(x/z, y/z, z/z)

    return homography, object_position
