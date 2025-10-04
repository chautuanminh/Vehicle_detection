# Vehicle Detection
Report:
https://docs.google.com/document/d/1q6Qe5KUNlzFd0eYJKmHpl4wKMUVWYbNi4aoqlcjNl60/edit?usp=sharing
The dataset :
https://universe.roboflow.com/stubbornstrawsberries/fisheye8k/dataset/7
1. Concept:
- double pipeline including Object Detecton and Object Classifcation
- Model used: YOLOV11m (Object Detection), Resnet50/EfficientNetB0/YOLOV11m (Object Classification)
2. Process:
- YOLO model to detect --> strip out the images
- preprocessing
- Object Classification
