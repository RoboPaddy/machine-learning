import cv2

import time
from gpiozero import AngularServo
servo =AngularServo(18, initial_angle=0, min_pulse_width=0.0006, max_pulse_width=0.0023)

#thres = 0.45 # Threshold to detect object

classNames = []
classFile = "/home/robopaddy/code/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/robopaddy/code/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/robopaddy/code/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects: 
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    
                    servo.angle = -90
                    time.sleep = 2
                    servo.angle = 90
    
    return img,objectInfo


def detect():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    
    detect_times = 0
    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img,0.45,0.2, objects=['bird'])
        if objectInfo:
            return objectInfo
        else:
            time.sleep = 1
            
        detect_times += 1
        if detect_times == 500:
            return []
        cv2.imshow("Output",img)
        cv2.waitKey(1)



if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #cap.set(10,70)
    
    
    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img,0.45,0.2, objects=['bird'])
        if objectInfo:
            print(objectInfo)
        else:
            time.sleep = 1
        cv2.imshow("Output",img)
        cv2.waitKey(1)
        
    
