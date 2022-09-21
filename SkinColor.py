import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

class SkinColor:

    def avgSkinColor(self, listOfXYPoints, im_pil):
        mask = Image.new("L", im_pil.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.polygon(listOfXYPoints[0], fill=255, outline=None)
        black =  Image.new("RGB", im_pil.size, 0)
        result = Image.composite(im_pil, black, mask)
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[1], fill="black")
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[2], fill="black")
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[3], fill="black")
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[4], fill="black")
        pixel_values = list(result.getdata())
        
        R_list = []
        G_list = []
        B_list = []
        for pixel in pixel_values:
            R,G,B = pixel
            if (max(0, R, 0-R) + max(0, G, 0-G) + max(0, B, 0-B)<=0): 
                    pass
            else:
                        
                R_list.append(R)
                G_list.append(G)
                B_list.append(B)
        sum_of_R = 0
        sum_of_G = 0
        sum_of_B = 0
        
        R_length_list = len(R_list)
        G_length_list = len(G_list)
        B_length_list = len(B_list)
        
        for R_number in R_list:
            sum_of_R = sum_of_R + R_number
            
        for G_number in G_list:
            sum_of_G = sum_of_G + G_number
            
        for B_number in B_list:
            sum_of_B = sum_of_B + B_number       
        
        avg_R = int(sum_of_R / R_length_list)
        avg_G = int(sum_of_G / G_length_list)
        avg_B = int(sum_of_B / B_length_list)
        print(avg_R, avg_G, avg_B)
        return avg_R, avg_G, avg_B         
        

    def img_estim(self, img, thrshld):
        is_light = np.mean(img) > thrshld
        print(np.mean(img))
        return 'light' if is_light else 'dark'
    
    
    def doesItNeedBrightnessChange(self, listOfXYPoints, im_pil):
        mask = Image.new("L", im_pil.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.polygon(listOfXYPoints[0], fill=255, outline=None)
        black =  Image.new("RGB", im_pil.size, 0)
        result = Image.composite(im_pil, black, mask)
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[1], fill="black")
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[2], fill="black")
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[3], fill="black")
        
        draw = ImageDraw.Draw(result)
        draw.polygon(listOfXYPoints[4], fill="black")
        
        g = result.convert('L')
        dark_or_light = self.img_estim(g, 9.6)
        print(dark_or_light)
        
        return dark_or_light