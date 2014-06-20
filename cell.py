import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageChops

source = 'cell.jpg'
output = ''

img = cv2.imread(source)
blur = cv2.GaussianBlur(img,(25,25),0)
#cv2.imwrite('blur.jpeg', blur)


sourcePIL = Image.open(source).convert('RGB')
blurPIL = Image.fromarray(blur).convert('RGB')
# Subtract blur from source
# Dependent on scale/offset
scale = .2
offset = 10
diff = ImageChops.subtract(sourcePIL, blurPIL,scale,offset)
diff.save("s"+str(scale)+"-o"+str(offset)+".jpeg")






# Different blurs to try
''''
median_blur = cv2.medianBlur(img,15)
median_string = 'median_blur'
cv2.putText(median_blur,median_string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
cv2.imshow('Blur',median_blur)
cv2.waitKey(3000)
sub_median = cv2.absdiff(img, median_blur)
cv2.imshow('Blur',sub_median)
cv2.waitKey(3000)

bilateral_blur = cv2.bilateralFilter(img,25, 25*2,25/2)
bilateral_string = 'bilateral_blur'
cv2.putText(bilateral_blur,bilateral_string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
cv2.imshow('Blur',bilateral_blur)
cv2.waitKey(3000)
sub_bilateral = cv2.absdiff(img, bilateral_blur)
cv2.imshow('Blur',sub_bilateral)
cv2.waitKey(3000)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) //grayscale
//cv2.imshow('image',gray)
contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
rgb_filtered = cv2.inRange(img, (124, 124, 124), (255, 255, 255))
'''