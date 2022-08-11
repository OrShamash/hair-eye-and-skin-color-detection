import h5py
import tensorflow as tf
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose, concatenate, BatchNormalization, Dropout
from keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import regularizers

#to load it
with h5py.File('C:\\Users\\orish\\Desktop\\DataSet.h5', 'r') as hf:
    x_train = hf['x'][...]
    y_train = hf['y'][...]
           
inputs = Input((224, 224, 3))
c1 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu',padding='same')(inputs) #222X222
c1 = tf.keras.layers.Dropout(0.1)(c1)
c1 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu',padding='same')(c1) #220X220
p1 = tf.keras.layers.MaxPool2D((2,2))(c1) 

c2 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu',padding='same')(p1) #108X108
c2 = tf.keras.layers.Dropout(0.1)(c2)
c2 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu',padding='same')(c2) #106X106
p2 = tf.keras.layers.MaxPool2D((2,2))(c2)

c3 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu',padding='same')(p2) #51X51
c3 = tf.keras.layers.Dropout(0.2)(c3)
c3 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu',padding='same')(c3) #49X49
p3 = tf.keras.layers.MaxPool2D((2,2))(c3) 

c4 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu',padding='same')(p3) #22X22
c4 = tf.keras.layers.Dropout(0.2)(c4)
c4 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu',padding='same')(c4) #20X20
p4 = tf.keras.layers.MaxPool2D((2,2))(c4) 

c5 = tf.keras.layers.Conv2D(512, (3, 3), activation='relu',padding='same')(p4) #5X5
c5 = tf.keras.layers.Dropout(0.3)(c5)
c5 = tf.keras.layers.Conv2D(512, (3, 3), activation='relu',padding='same')(c5) #3X3
p5 = tf.keras.layers.MaxPool2D((2,2))(c5)

c5a = tf.keras.layers.Conv2D(1024, (3, 3), activation='relu',padding='same')(p5) #5X5
c5a = tf.keras.layers.Dropout(0.3)(c5a)
c5a = tf.keras.layers.Conv2D(1024, (3, 3), activation='relu',padding='same')(c5a)

#expansive path

u5b = tf.keras.layers.Conv2DTranspose(512, (2,2), (2,2))(c5a) # 
u5b = tf.keras.layers.concatenate([u5b, c5], axis=3)
c5b = tf.keras.layers.Conv2D(512, (3, 3),activation='relu',padding='same')(u5b)
c5b = tf.keras.layers.Dropout(0.2)(c5b)
c5b = tf.keras.layers.Conv2D(512, (3, 3), activation='relu',padding='same')(c5b)

u6 = tf.keras.layers.Conv2DTranspose(256, (2,2), (2,2))(c5)
u6 = tf.keras.layers.concatenate([u6,c4], axis=3)
c6 = tf.keras.layers.Conv2D(256, (3, 3),activation='relu',padding='same')(u6)
c6 = tf.keras.layers.Dropout(0.2)(c6)
c6 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu',padding='same')(c6)

u7 = tf.keras.layers.Conv2DTranspose(128, (2,2), (2,2))(c6)
u7 = tf.keras.layers.concatenate([u7,c3], axis=3)
c7 = tf.keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same')(u7)
c7 = tf.keras.layers.Dropout(0.1)(c7)
c7 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')(c7)

u8 = tf.keras.layers.Conv2DTranspose(64, (2,2), (2,2))(c7)
u8 = tf.keras.layers.concatenate([u8,c2], axis=3)
c8 = tf.keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same')(u8)
c8 = tf.keras.layers.Dropout(0.1)(c8)
c8 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu',padding='same')(c8)

u9 = tf.keras.layers.Conv2DTranspose(32, (2,2), (2,2))(c8)
u9 = tf.keras.layers.concatenate([u9,c1], axis=3)
c9 = tf.keras.layers.Conv2D(32, (3, 3),activation='relu',padding='same')(u9)
c9 = tf.keras.layers.Dropout(0.1)(c9)
c9 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu',padding='same')(c9)

outputs = tf.keras.layers.Conv2D(1, (3, 3), activation='relu',padding='same')(c9)

model = tf.keras.Model(inputs=[inputs] ,outputs=[outputs])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),loss=tf.keras.losses.mean_squared_error, metrics=['accuracy'])
model.summary()

epochs = 25
history = model.fit(x_train,y_train,epochs=epochs,batch_size=32,shuffle=False)
model.save('C:\\Users\\orish\\Desktop\\HairSegmentationUnet.h5')