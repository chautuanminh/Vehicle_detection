# Vehicle Detection
Final report for the project:
https://docs.google.com/document/d/19Ib9A4XOq_6IN2JGbrgpHPudohw_DFvPdNU3EqPUUoE/edit?usp=sharing
The dataset :
https://universe.roboflow.com/stubbornstrawsberries/fisheye8k/dataset/7
1. Concept:
- double pipeline including Object Detecton and Object Classifcation
- Model used: YOLOV11m (Object Detection), Resnet50/EfficientNetB0/YOLOV11m (Object Classification)
2. Process:
- YOLO model to detect --> strip out the images
- preprocessing
- Object Classification
