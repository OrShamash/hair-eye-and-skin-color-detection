import mediapipe as mp
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
import math
from projectXandYCoordinates import XandYCoordinatesAndPoints
from projectEyesColor import EyesColor
from projectSkinColor import SkinColor
from ast import literal_eval as make_tuple




class DoesItNeedBrightnessChange:
    
    def doesItNeed(self, filePic):
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_face_mesh = mp.solutions.face_mesh
            
        drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.5) as face_mesh:
          #for idx, file in enumerate(IMAGE_FILES):
            
            #resize the imge  
            image = cv2.imread(filePic)

            #image = filePic
            assert not isinstance(image,type(None)), 'image not found'
            scale_percent = 100 # percent of original size
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)
            new_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            
            #convert from cv2 to PIL
            img = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(img)
            
            # Convert the BGR image to RGB before processing.
            results = face_mesh.process(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
            # Print and draw face mesh landmarks on the image.
            #if not results.multi_face_landmarks:
                #break
            annotated_image = new_image.copy()
            for face_landmarks in results.multi_face_landmarks:
                
                facePoints = [11,110,68,104,55,22,163,128,228,124,94,206,204,3,424,426,353,265,369,302,285,333,298,339]
                rightEyePoints = [34,247,162,161,160,159,158,174,134,156,155,154,146,145,164,8]
                leftEyePoints = [363,399,385,386,387,388,389,467,264,250,391,374,375,381,382,383]
                rightEyeBrowPoints = [71,64,106,67,108,56,66,53,54,47]
                leftEyeBrowPoints = [286,337,297,335,294,301,277,284,283,296]
                
                faceNumberOfPointsList = [facePoints,rightEyePoints,leftEyePoints,rightEyeBrowPoints,leftEyeBrowPoints]
                
                XandYskin = XandYCoordinatesAndPoints()
                listSkin = XandYskin.valuesOfXandYPoints(face_landmarks, faceNumberOfPointsList, new_image)
                skin_color = SkinColor()
                
                
                does_it = skin_color.doesItNeedBrightnessChange(listSkin, im_pil)
                
            return does_it   
                    
                    
                    
                    
                    