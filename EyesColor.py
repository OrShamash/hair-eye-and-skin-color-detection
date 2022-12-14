from PIL import Image, ImageDraw

class EyesColor:
    
    def avgEyeColor(self,result):
    
        pixel_values = list(result.getdata())
        
        R_list = []
        G_list = []
        B_list = []
        for pixel in pixel_values:
            R,G,B = pixel
            if ((max(0, R-0, 0-R) + max(0, G-0, 0-G) + max(0, B-0, 0-B)<=0) #pupil color
                or (max(0, R-255, 140-R) + max(0, G-255, 140-G) + max(0, B-255, 140-B)<=0)): #white lighting
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
        return avg_R, avg_G, avg_B
    
    def dominantColors(self, avg_R, avg_G, avg_B):
        
        colors = [('R',avg_R), ('G',avg_G), ('B',avg_B)]
        sorted_colors = sorted(colors, key=lambda x: x[1])
        
        max_color , max_value = sorted_colors[2]
        mid_color , mid_value = sorted_colors[1]
        min_color , min_value = sorted_colors[0]

        b1 = max_value - min_value
        b2 = mid_value - min_value
        color_combination = b2/b1
        
        if color_combination*100 <= 33:
            return max_color
        else:
            return max_color ,mid_color
    
    
    def rightEyeColor(self, listOfXYPoints,im_pil): 
        original = im_pil
        xy = listOfXYPoints[0] 
        mask = Image.new("L", original.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.polygon(xy, fill=255, outline=None)
        black =  Image.new("RGB", original.size, 0)
        result = Image.composite(original, black, mask)   
        
        avg_R, avg_G, avg_B = self.avgEyeColor(result)
        dominant_colors = self.dominantColors(avg_R, avg_G, avg_B)
        
        if len(dominant_colors) == 1:
            if dominant_colors == 'R':
                return 'brown right'
            elif dominant_colors == 'G':
                return 'green right'
            elif dominant_colors == 'B':
                return 'blue right'
        elif len(dominant_colors) == 2:
            max_dominant_color = dominant_colors[0]
            min_dominant_color = dominant_colors[1] 
            if max_dominant_color =='R' and min_dominant_color =='G' :
                return 'hazel right'
            elif max_dominant_color =='G' and min_dominant_color =='R':
                return 'hazel right' 
            elif max_dominant_color =='G' and min_dominant_color =='B':
                return 'green bright right' 
            elif max_dominant_color =='B' and min_dominant_color =='G':
                return 'green bright right'  
            elif max_dominant_color =='B' and min_dominant_color =='R':
                return 'blue bright right'
            elif max_dominant_color =='R' and min_dominant_color =='B':
                return 'blue bright right' 
            else:
                return 'right color not found'
            
        
    def leftEyeColor(self, listOfXYPoints,im_pil): 
        original = im_pil
        xy = listOfXYPoints[0] 
        mask = Image.new("L", original.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.polygon(xy, fill=255, outline=None)
        black =  Image.new("RGB", original.size, 0)
        result = Image.composite(original, black, mask)
        avg_R, avg_G, avg_B = self.avgEyeColor(result)
        dominant_colors = self.dominantColors(avg_R, avg_G, avg_B)
        if len(dominant_colors) == 1:
            if dominant_colors == 'R':
                return 'brown left'
            elif dominant_colors == 'G':
                return 'green left'
            elif dominant_colors == 'B':
                return 'blue left'
        elif len(dominant_colors) == 2:
            max_dominant_color = dominant_colors[0]
            min_dominant_color = dominant_colors[1] 
            if max_dominant_color =='R' and min_dominant_color =='G' :
                return 'hazel left'
            elif max_dominant_color =='G' and min_dominant_color =='R':
                return 'hazel left' 
            elif max_dominant_color =='G' and min_dominant_color =='B':
                return 'green bright left' 
            elif max_dominant_color =='B' and min_dominant_color =='G':
                return 'green bright  left'  
            elif max_dominant_color =='B' and min_dominant_color =='R':
                return 'blue bright left'
            elif max_dominant_color =='R' and min_dominant_color =='B':
                return 'blue bright  left' 
            else:
                return 'left color not found'
            
