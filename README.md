# yolov3_trt_ros
yolov3 TensorRT ROS


====
- **Object detection (Detection Result / BEV result)**

[![Object detection](http://img.youtube.com/vi/CmKZm0-LfUw/0.jpg)](https://youtu.be/CmKZm0-LfUw)
[![Object detection](http://img.youtube.com/vi/-DNyKI_qmKc/0.jpg)](https://youtu.be/-DNyKI_qmKc)
</br>
</br>

객체 인식 및 depth 추정 프로젝트
===
> **프로그래머스 K-Digital Training 자율주행 데브코스 15주차 프로젝트**  
> 1:10 스케일 모형 차(Xycar)를 활용한 객체 인식 및 depth 추정 프로젝트 (Object Detection & Depth Estimation project using 1:10 scale model car(Xycar))  
> 개발기간 (Development period): 2024.01.16 ~ 2024.01.26
</br>

## 팀 소개
| 팀원 | 팀원 | 팀원 | 멘토 |
|:------:|:------:|:------:|:---:|
| 김윤지 | 박성준 | 허동욱 |이치현|
|[@younji524](https://github.com/younji524)|[@jagbum](https://github.com/jagbum)|[@dongwookheo](https://github.com/dongwookheo)|[@hyunny223](https://github.com/hyuny223)|
</br>

## 프로젝트 소개
![경진대회 전체맵](https://github.com/object-detection-team4/lane_detection_project/assets/76142194/bc6ea7c9-e11b-4bb4-a4da-591648dc6bc9)

- 카메라 센서로 주어진 표지판과 신호등을 인식하여, 코스를 벗어나지 않으며 해당 표지판과 일치하는 주행을 할 수 있도록 한다.
  - 신호등에 맞추어 전진 혹은 정지 주행하도록 한다. 
  - 정지 표지판, 횡단보도 앞에서는 정지선 직전 45cm 이내에서 정지하도록 한다.
  - 코스 내 정적 장애물은 피해서 주행하고, 동적 장애물 등장 시 정지하도록 한다.
</br>

## Depth Estimation
- Camera Calibration using Homography

  : 블럭을 이용하여 이미지 좌표계 상의 블럭 좌표와 실제 그리드 상에서의 블럭 좌표를 이용하여 Homography를 구하고,

  Homography 를 이용하여 이미지 상의 좌표를 그리드 상 좌표로 변환하여 나타낸다.
<img src = "https://github.com/object-detection-team4/yolov3_trt_ros/assets/76142194/124f9681-6188-4ef5-812d-16e547ca861a" width="791.2" height="627.25"/>
</br>
</br>

- Calibration Result

<img src = "https://github.com/object-detection-team4/yolov3_trt_ros/assets/76142194/f537c7b5-1f9a-4b42-92f0-c9e04bedce07" width="560" height="634"/>
<img src = "https://github.com/object-detection-team4/yolov3_trt_ros/assets/76142194/3b2f9e62-b8ad-4dc7-b8fa-8f2f14fce722" width="560" height="634"/>
</br>
</br>

- 객체의 위치(거리) 추정 방법

  : xycar 좌표(0, 0)로부터 Homography를 통해 Grid에 표현한 포인트 (x, y)까지의 거리를 구한다.
</br>

## 환경 설정
### Requirements
- OpenCV 4.5.5
- ROS melodic
- Ubuntu 18.04 LTS

## Stacks
### Environment
<img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"> <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
<img src="https://img.shields.io/badge/git-F04032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> 

### Config
<img src="https://img.shields.io/badge/yaml-CB171E?style=for-the-badge&logo=yaml&logoColor=white">

### Development
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/ros-22314E?style=for-the-badge&logo=ros&logoColor=white"> 
<img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">

### Communication
<img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
<img src="https://img.shields.io/badge/jira-0052CC?style=for-the-badge&logo=jira&logoColor=white">


