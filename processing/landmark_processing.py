import os
import mediapipe as mp
from flask import Flask, Response, render_template, session
from pathlib import Path
import time
import cv2
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions


class pose_detection:
   
   def __init__(self, static_image_mode = False, model_complexity = 1, smooth_landmarks = True, enable_segmentation = False, smooth_segmentation = True, num_poses = 1, min_pose_detection_confidence = 0.5, min_pose_presence_confidence = 0.5, min_tracking_confidence = 0.7):
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.num_poses = num_poses
        self.min_pose_detection_confidence = min_pose_detection_confidence
        self.min_pose_presence_confidence = min_pose_presence_confidence
        self.min_tracking_confidence = min_tracking_confidence
        
        
        #To detect landmarks 
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.model_complexity, self.smooth_landmarks, self.enable_segmentation, self.smooth_segmentation, self.min_tracking_confidence)
        
        self.pose_draw = mp.solutions.drawing_utils
        
    def generate_frames(self):
        
        while True: 
            
            success, frame = .read()
            
            if not success:
                break 
    
    # def drawPose(self, frames, draw=True):
    #     self.FLIPiMG = 
    #     self.RGBimg =
    
    
    
if __name__ == "__main__":
    #Geting the logged-in user
    user_id = session["user_id"]
    
    cap = cv2.VideoCapture("data/videos/user_%s/recording_%s")