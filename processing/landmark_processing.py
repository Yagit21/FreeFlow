import os
import mediapipe as mp
from website.routes import video #Replace with actucal video variable

video = "comp_vision/data/videos/%s" % (video) #Replace with actucal video varibale

class pose_detection(self, static_image_mode = False, model_complexity = 1, smooth_landmarks = True, enable_segmentation = False, smooth_segmentation = True, min_tracking_confidence = 0.7, min_detection_confidence = 0.6 ):
   
    self.model_complexity = model_complexity
    self.smooth_landmarks = smooth_landmarks
    self.enable_segmentation = enable_segmentation
    self.smooth_segmentation = smooth_segmentation
    self.min_tracking_confidence = min_tracking_confidence
    self.min_detection_confidence = min_detection_confidence
    
    #To detect landmarks 
    self.mp_pose = mp.solutions.pose
    self.pose = self.mp_pose.Pose(self.model_complexity, self.smooth_landmarks, self.enable_segmentation, self.smooth_segmentation, self.min_tracking_confidence)
    
    #To visually see the detected landmarks "self.pose_draw = mp.solutions.drawing_utils"
    