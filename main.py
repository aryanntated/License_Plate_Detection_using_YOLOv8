from ultralytics import YOLO
import cv2

from sort.sort import *
from util import get_car

mot_tracker = Sort()

# load models
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('Models/license_plate_detector.pt')

# load video
cap = cv2.VideoCapture('C:/Projects/License_Plate_Detection_using_YOLOv8/test_video.mp4')

vehicles= [2, 3, 5, 7]

# read frames
ret = True
frame_no = -1

while ret:
    frame_no += 1
    ret, frame = cap.read()
    if ret and frame_no < 10:

        # detect vehicles
        detections = coco_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, score])


        # track vehicles
        track_ids = mot_tracker.update(np.asarray(detections_))


        # detect license plates
        license_plates = license_plate_detector(frame)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate


        # assign license plate to car
        xcar1,  ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)


        # crop license plate
        license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]

        # process license plate

        # read license plate number


        # write results
