import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

image = cv.imread("kill.jpg") 
fig, ax = plt.subplots(1, 3, figsize=(16, 8)) 
# image size being 0.15 times of it's original size 
image_scaled = cv.resize(image, None, fx=0.15, fy=0.15) 
ax[0].imshow(cv.cvtColor(image_scaled, cv.COLOR_BGR2RGB)) 
ax[0].set_title("Linear Interpolation Scale") 
