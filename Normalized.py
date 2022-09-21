import numpy as np
import math


class Normalized:
    
    def meanAndVarNormalized(self, avg_of_avg_normalized_R, avg_of_avg_normalized_G, avg_of_avg_normalized_B):
        the_mean_of_AVG_of_AVG_normalized_R = np.mean(avg_of_avg_normalized_R)            
        the_mean_of_AVG_of_AVG_normalized_G = np.mean(avg_of_avg_normalized_G)            
        the_mean_of_AVG_of_AVG_normalized_B = np.mean(avg_of_avg_normalized_B) 
    
        the_std_of_AVG_of_AVG_normalized_R = np.std(avg_of_avg_normalized_R)
        the_std_of_AVG_of_AVG_normalized_G = np.std(avg_of_avg_normalized_G)
        the_std_of_AVG_of_AVG_normalized_B = np.std(avg_of_avg_normalized_B)
        
        return the_mean_of_AVG_of_AVG_normalized_R ,the_mean_of_AVG_of_AVG_normalized_G ,the_mean_of_AVG_of_AVG_normalized_B ,the_std_of_AVG_of_AVG_normalized_R, the_std_of_AVG_of_AVG_normalized_G, the_std_of_AVG_of_AVG_normalized_B

    def normalized(self, avg_R, avg_G, avg_B):
        normal_R = avg_R/math.sqrt((avg_R)**2+(avg_G)**2+(avg_B)**2)
        normal_G = avg_G/math.sqrt((avg_R)**2+(avg_G)**2+(avg_B)**2)
        normal_B = avg_B/math.sqrt((avg_R)**2+(avg_G)**2+(avg_B)**2)
        return normal_R, normal_G, normal_B

    def sqrtSizeNormalized(self, the_std_of_AVG_of_AVG_normalized_R, the_std_of_AVG_of_AVG_normalized_G, the_std_of_AVG_of_AVG_normalized_B):
        sqrt_size_normalized = math.sqrt(the_std_of_AVG_of_AVG_normalized_R**2 + the_std_of_AVG_of_AVG_normalized_G**2 + the_std_of_AVG_of_AVG_normalized_B**2)   
        return sqrt_size_normalized
    
    def distanceFromMean(self, normal_R, the_mean_of_AVG_of_AVG_normalized_R, normal_G, the_mean_of_AVG_of_AVG_normalized_G, normal_B, the_mean_of_AVG_of_AVG_normalized_B):
        D = math.sqrt((normal_R-the_mean_of_AVG_of_AVG_normalized_R)**2 + (normal_G-the_mean_of_AVG_of_AVG_normalized_G)**2 + (normal_B-the_mean_of_AVG_of_AVG_normalized_B)**2)
        return D