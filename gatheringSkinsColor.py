#import mediapipe as mp
import cv2
#import numpy as np
#from PIL import Image, ImageDraw, ImageEnhance
#import math
#from projectXandYCoordinates import XandYCoordinatesAndPoints
##from projectEyesColor import EyesColor
from projectSkinColor import SkinColor
from projectCheckingFaceParts import FacePartsChecking
#from ast import literal_eval as make_tuple
from automatic_GammaCorrection import Automatic_gamma_correction
from does_it_need_brightness_change import DoesItNeedBrightnessChange
import os

R_list = []
G_list = []
B_list = []

for i in range(112,205,1):
    
    filePic = "F:\\face like project\\face like project\\ppl\\black ppl\\" +str(i)+'.jpg' 
    #filePic2 = r"F:\face like project\face like project\ppl\white ppl\11.jpg"
    print(i)
    image_no_change = cv2.imread(filePic)
    #cv2.imshow('image',image_no_change)
    #cv2.waitKey()

    faceChecking = FacePartsChecking()
    normal_R, normal_G, normal_B = faceChecking.facePartsChecking(image_no_change)
    
    R_list.append(normal_R)
    G_list.append(normal_G)  
    B_list.append(normal_B)




name_of_file = 'blackppl'
completeName = os.path.join(name_of_file+".txt")
with open(os.path.join('D:\\גיבוי כושל וואן דרייב\\Desktop',completeName), "w") as f:
    for R, G, B in zip(R_list, G_list, B_list):
        f.write("{0},{1},{2}\n".format(R, G, B))