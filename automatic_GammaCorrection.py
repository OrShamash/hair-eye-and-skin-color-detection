import cv2
import numpy as np
import math


class Automatic_gamma_correction:
    
    def gammaCorrection(self, filePic):
            # read image
        img = cv2.imread(filePic)
        
        # METHOD 1: RGB
        
        # convert img to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # compute gamma = log(mid*255)/log(mean)
        mid = 0.5
        mean = np.mean(gray)
        gamma = math.log(mid*255)/math.log(mean)
        #print(gamma)
        
        # do gamma correction
        img_gamma1 = np.power(img, gamma).clip(0,255).astype(np.uint8)
        
        
        
        # METHOD 2: HSV (or other color spaces)
        
        # convert img to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hue, sat, val = cv2.split(hsv)
        
        # compute gamma = log(mid*255)/log(mean)
        mid = 0.555
        mean = np.mean(val)
        gamma = math.log(mid*255)/math.log(mean)
        #print(gamma)
        
        # do gamma correction on value channel
        val_gamma = np.power(val, gamma).clip(0,255).astype(np.uint8)
        
        # combine new value channel with original hue and sat channels
        hsv_gamma = cv2.merge([hue, sat, val_gamma])
        img_gamma2 = cv2.cvtColor(hsv_gamma, cv2.COLOR_HSV2BGR)
        #cv2.imshow('auto_result', img_gamma2)
        
        return img_gamma2
    

        
