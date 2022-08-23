import cv2

img = cv2.imread('city.jpeg')

objectNames = 'coco.names'
with open(objectNames, 'rt') as f:
    objectNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

classIds, confs, bbox = net.detect(img, confThreshold=0.5)
print(classIds, bbox)

for classIds, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
    cv2.rectangle(img, box, color=(0,255,0), thickness=2)
    cv2.putText(img, objectNames[classIds-1],(box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)

cv2.imshow("Output", img)
cv2.waitKey(0)
