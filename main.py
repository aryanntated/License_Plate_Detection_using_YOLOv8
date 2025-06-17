from ultralytics import YOLO
import cv2

# load models
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('Models/license_plate_detector.pt')

# load video
cap = cv2.VideoCapture('test_video.mp4')

# read frames
ret = True
frame_no = -1

while ret:
    ret, frame = cap.read()
    if ret and frame_no < 10:
        # detect vehicles
        detections = coco_model(frame)[0]
        print(detections)
        # track vehicles
        

        # detect license plates
            

        # assign license plate to car

        # crop license plate


        # process license plate

        # read license plate number


        # write results
