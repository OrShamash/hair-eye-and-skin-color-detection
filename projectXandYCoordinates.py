import mediapipe as mp
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

class XandYCoordinatesAndPoints:

    def findingPointNumberByXandYcoordinates(self,face_landmarks,x_coordinate,y_coordinate,new_image):      
          mone = 0 
          Number_Of_THE_Point = 0
          for landmark in face_landmarks.landmark:
              x_number = x_coordinate
              y_number = y_coordinate
              
              mone = mone + 1
              x = landmark.x
              y = landmark.y
              
              shape = new_image.shape 
              relative_x = int(x * shape[1])
              relative_y = int(y * shape[0])
              #print(relative_x,relative_y, "number of point:"+ str(mone))
              
              if relative_x == x_number and relative_y == y_number:
                  Number_Of_THE_Point = mone
                  break
              
          return Number_Of_THE_Point
    
    
    #Taking the number of points of each part of the face and return the x and y coordinates
    #Taking list of lists and return list of lists
    def valuesOfXandYPoints(self,face_landmarks,faceNumberOfPointsList,new_image):
        listOfFacePartsCoordinates=[]
        listOfPoints = []
        
        for partOfFaceIndex in faceNumberOfPointsList:
            for partsOfFace in partOfFaceIndex:
                
                number_Of_Points = partsOfFace
                #print(number_Of_Points)
                
                valuesOfPoints=[[],[],[]]
                mone = 0
                for landmark in face_landmarks.landmark:
                    mone = mone + 1
                    x = landmark.x
                    y = landmark.y
                    shape = new_image.shape 
                    relative_x = int(x * shape[1])
                    relative_y = int(y * shape[0])
                    
                    valuesOfPoints[0].append(relative_x)
                    valuesOfPoints[1].append(relative_y)
                    valuesOfPoints[2].append(mone)
                
                #print(valuesOfPoints)
                
                #row = len(valuesOfPoints[0]) 
                for i in range(1,len(valuesOfPoints[0]),1):
                    if number_Of_Points == valuesOfPoints[2][i]: 
                        valueOfpoint = valuesOfPoints[0][i], valuesOfPoints[1][i]
                        #print(valueOfpoint)
                        listOfPoints.append(valueOfpoint)
                        #print(listOfPoints)
    
            listOfFacePartsCoordinates.append(listOfPoints)
            #print(listOfPoints)
            listOfPoints = []
            #print(listOfFacePartsCoordinates)
        return listOfFacePartsCoordinates
