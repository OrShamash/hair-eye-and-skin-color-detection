 #main
import mediapipe as mp
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
import math
from projectXandYCoordinates import XandYCoordinatesAndPoints
from projectEyesColor import EyesColor
from projectSkinColor import SkinColor
from projectCheckingFaceParts import FacePartsChecking
from ast import literal_eval as make_tuple
from automatic_GammaCorrection import Automatic_gamma_correction
from does_it_need_brightness_change import DoesItNeedBrightnessChange


fileInfo = r'C:\Users\orish\Desktop\project\blackPplDataNotNormalized.txt'
fileData = open(fileInfo, 'r')
lines = fileData.readlines() 
for line in lines:
    the_mean_of_AVG_of_AVG_normalized_R_black ,the_mean_of_AVG_of_AVG_normalized_G_black ,the_mean_of_AVG_of_AVG_normalized_B_black ,the_std_of_AVG_of_AVG_normalized_R_black, the_std_of_AVG_of_AVG_normalized_G_black, the_std_of_AVG_of_AVG_normalized_B_black = make_tuple(line)


fileInfo = r'C:\Users\orish\Desktop\project\whitePplDataNotNormalized.txt'
fileData = open(fileInfo, 'r')
lines = fileData.readlines() 
for line in lines:
    the_mean_of_AVG_of_AVG_normalized_R_white ,the_mean_of_AVG_of_AVG_normalized_G_white ,the_mean_of_AVG_of_AVG_normalized_B_white ,the_std_of_AVG_of_AVG_normalized_R_white ,the_std_of_AVG_of_AVG_normalized_G_white ,the_std_of_AVG_of_AVG_normalized_B_white = make_tuple(line)

###CHOOSE YOUR PIC NUMBER###########
i=1

filePic = 'C:\\Users\\orish\\Desktop\\'+str(i)+'.jpg'    ##### <============ PIC PATH

does_it_need_brightness_change = DoesItNeedBrightnessChange()
does_it_need = does_it_need_brightness_change.doesItNeed(filePic)

if does_it_need == 'dark':
    auto_bright_cont = Automatic_gamma_correction()
    image_after_gamma_change = auto_bright_cont.gammaCorrection(filePic)
        
    faceChecking = FacePartsChecking()
    a, b, c, d, color_of_right_eye, color_of_left_eye = faceChecking.facePartsChecking(the_mean_of_AVG_of_AVG_normalized_R_white ,the_mean_of_AVG_of_AVG_normalized_G_white ,the_mean_of_AVG_of_AVG_normalized_B_white ,the_std_of_AVG_of_AVG_normalized_R_white, the_std_of_AVG_of_AVG_normalized_G_white, the_std_of_AVG_of_AVG_normalized_B_white, the_mean_of_AVG_of_AVG_normalized_R_black ,the_mean_of_AVG_of_AVG_normalized_G_black ,the_mean_of_AVG_of_AVG_normalized_B_black ,the_std_of_AVG_of_AVG_normalized_R_black, the_std_of_AVG_of_AVG_normalized_G_black, the_std_of_AVG_of_AVG_normalized_B_black, image_after_gamma_change, i)
    
    if a==1 and b==0:
        print('White Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))
    elif a==0 and b==1:
        print('Black Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))
        
    if a == b:
        if c > d: 
            print('White Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))
        elif c < d: 
            print('Black Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))          
        elif a == 1 and  b == 0:
            print('White Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))
        elif a == 0 and b == 1:
            print('Black Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))    
    
if does_it_need == 'light':
    faceChecking = FacePartsChecking()
    image_no_change = cv2.imread(filePic)
    a, b, c, d, color_of_right_eye, color_of_left_eye = faceChecking.facePartsChecking(the_mean_of_AVG_of_AVG_normalized_R_white ,the_mean_of_AVG_of_AVG_normalized_G_white ,the_mean_of_AVG_of_AVG_normalized_B_white ,the_std_of_AVG_of_AVG_normalized_R_white, the_std_of_AVG_of_AVG_normalized_G_white, the_std_of_AVG_of_AVG_normalized_B_white, the_mean_of_AVG_of_AVG_normalized_R_black ,the_mean_of_AVG_of_AVG_normalized_G_black ,the_mean_of_AVG_of_AVG_normalized_B_black ,the_std_of_AVG_of_AVG_normalized_R_black, the_std_of_AVG_of_AVG_normalized_G_black, the_std_of_AVG_of_AVG_normalized_B_black, image_no_change, i)
    
    if a==1 and b==0:
        print('White Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))
    elif a==0 and b==1:
        print('Black Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))
    
    if a == b:
        if c > d: 
            print('White Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))                
        elif c < d: 
            print('Black Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))                        
        elif a == 1 and  b == 0:
            print('White Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))            
        elif a == 0 and b == 1:   
            print('Black Skin, '+str(color_of_right_eye)+', '+str(color_of_left_eye))        