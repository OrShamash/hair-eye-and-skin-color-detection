import tensorflow as tf
import os
import numpy as np
from tqdm import tqdm
from skimage.io import imread,imshow
from skimage.transform import resize
from skimage import data
import matplotlib.pyplot as plt
import h5py
import cv2
import PIL
from PIL import Image

IMG_WIDTH = 224
IMG_HEIGHT = 224
IMG_CHANNELS = 3
dim = (IMG_HEIGHT, IMG_WIDTH)
a=10000
pathImage ="C:\\Users\\orish\\Desktop\\content - Copy\\All_data\\train\\image" 
#"C:\\Users\\orish\\Desktop\\content - Copy\\All_data\\train\\image"
pathSeg = "C:\\Users\\orish\\Desktop\\content - Copy\\All_data\\train\\seg"
#"C:\\Users\\orish\\Desktop\\content - Copy\\All_data\\train\\seg"
amountOfFileInImage = len([f for f in os.listdir(pathImage)if os.path.isfile(os.path.join(pathImage, f))])
amountOfFileInMask = len([f for f in os.listdir(pathSeg)if os.path.isfile(os.path.join(pathSeg, f))])


if amountOfFileInImage == amountOfFileInMask:
    print("number of files are OK!!!"+str(amountOfFileInImage))
    X_train = np.zeros((a, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
    Y_train = np.zeros((a, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
    print('resizing training images and mask')
    #amountOfFileInImage-1
    with h5py.File('C:\\Users\\orish\\Desktop\\DataSetTrain10000Normalizedh5.h5', 'w') as hf:
        for n in tqdm(range(0,a,1)):
            path2 = pathImage+"/"+"1 ("+str(n+1)+")"+'.jpg'
            image = Image.open(path2)
            image = image.resize(dim)
            image = image.convert('RGB')
            #image.show()
            final_image_tensor = tf.convert_to_tensor(image, dtype=tf.float32) /255.0
            X_train[n] = final_image_tensor


            path3 = pathSeg+"/"+"2 ("+str(n+1)+")"+'.png'

            seg_mask = Image.open(path3)
            seg_mask = seg_mask.resize(dim)
            seg_mask = seg_mask.convert('RGB')
            
            pixels = seg_mask.load() 
            height, width = seg_mask.size
            for x in range(width):
                for y in range(height):
                    if pixels[x,y] == (10, 10, 10):            
                        pixels[x,y] = (1, 1, 1)
                    else:
                        pixels[x,y] = (0, 0, 0)

            #seg_mask.show()
            final_mask_tensor = tf.convert_to_tensor(seg_mask, dtype=tf.float32)
            #final_mask_tensor.show()
            Y_train[n] = final_mask_tensor
            
        Xset = hf.create_dataset(
                name= 'x',
                data= X_train)
        
        Yset = hf.create_dataset(
            name='y',
            data = Y_train)

    hf.close()
else:
    print("number of files are WRONG!!!"+str(amountOfFileInImage-amountOfFileInMask))

