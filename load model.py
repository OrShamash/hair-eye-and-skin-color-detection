import tensorflow as tf
import cv2
import PIL
from PIL import Image
import numpy as np
from matplotlib import cm
from skimage.io import imread,imshow
import os
import PIL
from PIL import Image
import numpy as np


model = tf.keras.models.load_model('C:\\Users\\orish\\Desktop\\HairSegmentationBESTONE.h5')

test_path = "F:\\face like project\\face like project\\4.jpg"
IMG_WIDTH = 224
IMG_HEIGHT = 224
IMG_CHANNELS = 3
dim = (IMG_HEIGHT, IMG_WIDTH)
image2 = Image.open(test_path)
image2 = image2.resize(dim)
image2 = image2.convert('RGB')
tf_image = np.array(image2)/ 255.0
final_image_tensor = tf.convert_to_tensor(tf_image, dtype=tf.float32)
test_predict = model.predict(tf.expand_dims(final_image_tensor ,axis=0))


percentage_min = 20.0
percentage_max = 70.0

img_np = test_predict
img_np = img_np.reshape(224, 224)

max_value = np.max(img_np)
print(max_value)

want_val_min = max_value*(percentage_min/100)
want_val_max = max_value*(percentage_max/100)

counter = 0
for i in range(224):
    for j in range(224):
      if img_np[i][j] >= want_val_min and img_np[i][j] <= want_val_max:
          counter = counter +1
          img_np[i][j] = 1
      else:
          img_np[i][j] = 0

print(counter)

imshow(img_np)

# Open the input image as numpy array
npImage=np.array(image2)
# Open the mask image as numpy array
npMask=np.array(cv2.cvtColor(img_np, cv2.COLOR_GRAY2BGR))
cond = npMask == 1
pixels=np.where(cond, npImage, npMask)

pixels = pixels.astype(np.uint8)
result = Image.fromarray(pixels)
result