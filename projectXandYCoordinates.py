import mediapipe as mp
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

class XandYCoordinatesAndPoints:
    #This function returns the point number in the list of the points Mesh. 
    #It gets the X,Y of a point compare it with the item's list time the shape of the pic and returns the number of the point in the Mesh
    #If it didnt find. returns zero.
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
              
              if relative_x == x_number and relative_y == y_number:
                  Number_Of_THE_Point = mone
                  break
              
          return Number_Of_THE_Point
    
    
    #Taking point number list of each part of the face and return the x and y coordinates
    def valuesOfXandYPoints(self,face_landmarks,faceNumberOfPointsList,new_image):
        listOfFacePartsCoordinates=[]
        listOfPoints = []
        
        for partOfFaceIndex in faceNumberOfPointsList:
            for partsOfFace in partOfFaceIndex:
                
                number_Of_Points = partsOfFace
                
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
                
                for i in range(1,len(valuesOfPoints[0]),1):
                    if number_Of_Points == valuesOfPoints[2][i]: 
                        valueOfpoint = valuesOfPoints[0][i], valuesOfPoints[1][i]
                        listOfPoints.append(valueOfpoint)
    
            listOfFacePartsCoordinates.append(listOfPoints)
            listOfPoints = []
        return listOfFacePartsCoordinates
