import mediapipe as mp
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
import math
from projectXandYCoordinates import XandYCoordinatesAndPoints
from projectEyesColor import EyesColor
from projectSkinColor import SkinColor
from ast import literal_eval as make_tuple
from normalized import Normalized



class FacePartsChecking:
    
    def facePartsChecking(self, the_mean_of_AVG_of_AVG_normalized_R_white ,the_mean_of_AVG_of_AVG_normalized_G_white ,the_mean_of_AVG_of_AVG_normalized_B_white ,the_std_of_AVG_of_AVG_normalized_R_white, the_std_of_AVG_of_AVG_normalized_G_white, the_std_of_AVG_of_AVG_normalized_B_white, the_mean_of_AVG_of_AVG_normalized_R_black ,the_mean_of_AVG_of_AVG_normalized_G_black ,the_mean_of_AVG_of_AVG_normalized_B_black ,the_std_of_AVG_of_AVG_normalized_R_black, the_std_of_AVG_of_AVG_normalized_G_black, the_std_of_AVG_of_AVG_normalized_B_black, image_after_change, i):

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
            image = image_after_change
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
                
                rightIrisPoints = [161,145,146,154,158,159,160]
                leftIrisPoints = [385,381,375,374,388,387,386]
                facePoints = [11,110,68,104,55,22,163,128,228,124,94,206,204,3,424,426,353,265,369,302,285,333,298,339]
                rightEyePoints = [34,247,162,161,160,159,158,174,134,156,155,154,146,145,164,8]
                leftEyePoints = [363,399,385,386,387,388,389,467,264,250,391,374,375,381,382,383]
                rightEyeBrowPoints = [71,64,106,67,108,56,66,53,54,47]
                leftEyeBrowPoints = [286,337,297,335,294,301,277,284,283,296]
                
                faceNumberOfPointsList = [facePoints,rightEyePoints,leftEyePoints,rightEyeBrowPoints,leftEyeBrowPoints]
                rightIrisEyeNumberOfPointsList = [rightIrisPoints]
                leftIrisEyeNumberOfPointsList = [leftIrisPoints]
                

                XandYright = XandYCoordinatesAndPoints()
                listRight = XandYright.valuesOfXandYPoints(face_landmarks, rightIrisEyeNumberOfPointsList, new_image)
                right_eye_color = EyesColor()
                color_of_right_eye = right_eye_color.rightEyeColor(listRight, im_pil)
        
                XandYleft = XandYCoordinatesAndPoints()
                listLeft = XandYleft.valuesOfXandYPoints(face_landmarks, leftIrisEyeNumberOfPointsList, new_image)
                left_eye_color = EyesColor()
                color_of_left_eye = left_eye_color.leftEyeColor(listLeft, im_pil)            


                XandYskin = XandYCoordinatesAndPoints()
                listSkin = XandYskin.valuesOfXandYPoints(face_landmarks, faceNumberOfPointsList, new_image)
                skin_color = SkinColor()

                normal_R, normal_G, normal_B = skin_color.avgSkinColor(listSkin, im_pil)

                sqrt = Normalized()
                size_of_sqrt = 2
                ######calculating for white###############
                sqrt_size_white = sqrt.sqrtSizeNormalized(the_std_of_AVG_of_AVG_normalized_R_white, the_std_of_AVG_of_AVG_normalized_G_white, the_std_of_AVG_of_AVG_normalized_B_white)
                variance_white = sqrt_size_white**2
                distance = Normalized()
                distance_size_white = distance.distanceFromMean(normal_R, the_mean_of_AVG_of_AVG_normalized_R_white, normal_G, the_mean_of_AVG_of_AVG_normalized_G_white, normal_B, the_mean_of_AVG_of_AVG_normalized_B_white)

                
                ######calculating for black##########
                sqrt_size_black = sqrt.sqrtSizeNormalized(the_std_of_AVG_of_AVG_normalized_R_black, the_std_of_AVG_of_AVG_normalized_G_black, the_std_of_AVG_of_AVG_normalized_B_black)
                variance_black = sqrt_size_black**2
                distance = Normalized()
                distance_size_black = distance.distanceFromMean(normal_R, the_mean_of_AVG_of_AVG_normalized_R_black, normal_G, the_mean_of_AVG_of_AVG_normalized_G_black, normal_B, the_mean_of_AVG_of_AVG_normalized_B_black)

                
                ############################################################
                c = distance_size_black/(sqrt_size_black*(size_of_sqrt))*100
                d = distance_size_white/(sqrt_size_white*(size_of_sqrt))*100
                
                if sqrt_size_white*(size_of_sqrt) > distance_size_white:
                    print('white skin' + str(i))
                    a = 1
                else:
                    print('not white skin'+ str(i))
                    a = 0
                if sqrt_size_black*(size_of_sqrt) > distance_size_black:
                    print('black skin'+ str(i))
                    b = 1
                else:
                    print('not black skin'+ str(i))
                    b = 0
                if c < d:
                    print('shorter distance to black')   
                if c > d:
                    print('shorter distance to white')
                    
                return a ,b ,c ,d, color_of_right_eye, color_of_left_eye
                 
                    
                    
                    
                    
                    