import os
import tkinter as tk
import time
from random import shuffle
import pymysql
import PIL.Image as pimg
import PIL.ImageTk as pimgtk
import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox, filedialog
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from keras.preprocessing.image import ImageDataGenerator
import tk as tk
import tkinter as tk

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.models import model_from_json
import warnings
warnings.filterwarnings('ignore')

from PIL import Image, ImageTk
from glob import glob
from PIL.ImageFile import ImageFile
from keras.applications.vgg19 import VGG19
from keras.models import Model


class ViewData:
    def __init__(self):

        def dataupload():
            s1 = "C:/foodcalorie/Dataset/Train"
            messagebox.showinfo("Success", s1)

        def viewdata():
            workingDir = "C:/foodcalorie/Dataset"

            train_dir = os.path.join(workingDir, "Train")
            validation_dir = os.path.join(workingDir, "Train")

            folders = [
                "Biriyani", "Chappathi", "Dosa", "foxtail_millet_pongal",
                "Idly", "pongal", "ragi_dosa", "ragi_idly", "rice"
            ]

            total_train = 0
            for f in folders:
                total_train += len(os.listdir(os.path.join(train_dir, f)))

            print("Total Train Images:", total_train)
            messagebox.showinfo("Success", f"Total Train Images: {total_train}")

        def viewdata1():
            train_dir = "C:/foodcalorie/Dataset/Train"
            validation_dir = "C:/foodcalorie/Dataset/Train"

            IMG_HEIGHT = 98
            IMG_WIDTH = 98
            batch_size = 2000

            train_datagen = ImageDataGenerator(rescale=1.0/255, shear_range=0.2,
                                               zoom_range=0.2, horizontal_flip=True)

            _ = train_datagen.flow_from_directory(train_dir,
                                                  target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                  batch_size=batch_size,
                                                  class_mode='binary')

            val_datagen = ImageDataGenerator(rescale=1.0/255)

            _ = val_datagen.flow_from_directory(validation_dir,
                                                target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                batch_size=batch_size,
                                                class_mode='binary')

            messagebox.showinfo("Success", "Class Extraction Success")

        def build():
            ImageFile.LOAD_TRUNCATED_IMAGES = True

            IMAGE_SIZE = [128, 128]  # Reduced from 300x300

            vgg = VGG19(input_shape=IMAGE_SIZE + [3],
                        weights='imagenet', include_top=False)

            for layer in vgg.layers:
                layer.trainable = False

            folders = glob('C:/foodcalorie/Dataset/Train/*')

            x = Flatten()(vgg.output)
            prediction = Dense(len(folders), activation='softmax')(x)

            model = Model(inputs=vgg.input, outputs=prediction)

            model.compile(loss='categorical_crossentropy',
                          optimizer='adam', metrics=['accuracy'])

            train_datagen = ImageDataGenerator(rescale=1.0 / 255,
                                               shear_range=0.2,
                                               zoom_range=0.2,
                                               horizontal_flip=True)

            val_datagen = ImageDataGenerator(rescale=1.0 / 255)

            training_set = train_datagen.flow_from_directory(
                'C:/foodcalorie/Dataset/Train',
                target_size=(128, 128),
                batch_size=8,
                class_mode='categorical')

            val_set = val_datagen.flow_from_directory(
                'C:/foodcalorie/Dataset/Test',
                target_size=(128, 128),
                batch_size=8,
                class_mode='categorical')

            history = model.fit(
                training_set,
                validation_data=val_set,
                epochs=5)

            model.save('model_food.h5')
            messagebox.showinfo("Success", "Model Build Successfully")
        # GUI Window
        win = Tk()
        win.title("Food Calorie Estimation")
        win.maxsize(width=900, height=800)
        win.minsize(width=900, height=800)
        win.configure(bg='#99ddff')

        image1 = Image.open("calorie.jpg")
        img = image1.resize((900, 800))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(win, image=test)
        label1.image = test
        label1.place(x=1, y=1)

        # ❌ REMOVE TITLE HERE
        # Label(win, text='Food Calorie Estimation', bg="#34bfbb",
        #       font='verdana 15 bold').place(x=170, y=120)

        # BUTTONS
        btnbrowse = Button(win, text="Dataset source", font='Verdana 10 bold',
                           command=dataupload)
        btnbrowse.place(x=70, y=200)

        btncamera = Button(win, text="Trained Image Extraction", font='Verdana 10 bold',
                           command=viewdata)
        btncamera.place(x=220, y=200)

        btnsend = Button(win, text="Total Class Extraction", font='Verdana 10 bold',
                         command=viewdata1)
        btnsend.place(x=450, y=200)

        btnsend = Button(win, text="Build CNN Model", font='Verdana 10 bold',
                         command=build)
        btnsend.place(x=650, y=200)

        win.mainloop()
