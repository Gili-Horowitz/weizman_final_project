import cv2
import numpy as np
import os
from PIL import Image, ImageEnhance
from skimage.metrics import structural_similarity as ssim





def crop_and_remove_coins(image_path):
   # Read the image
   image = cv2.imread(image_path)

   original_image = image.copy()
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   #cv2.imshow('Cropped Image', gray)  #

   #cv2.waitKey(0)  #
   #cv2.destroyAllWindows()  #
   blurred = cv2.GaussianBlur(gray, (9, 9), 5)
   #cv2.imshow('Cropped Image',blurred)  #
   #cv2.waitKey(0)  #
   #cv2.destroyAllWindows()  #


   # Detect edges
   edges = cv2.Canny(blurred, 30, 150)
   # Find contours
   contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


   # Loop through contours and save each coin as a separate image
   for i, contour in enumerate(contours):
       # Get bounding box of the contour
       x, y, w, h = cv2.boundingRect(contour)

       # Crop the coin from the image
       #coin = image[y:y + h, x:x + w]
      # Remove the coin from the original image by setting the ROI to white
   cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), -1)




   image = image[y:y + h, x:x + w]

   #cv2.imshow('Cropped Image', image)
   #cv2.waitKey(0)

   #cv2.destroyAllWindows()
   return  image, original_image


#image_path = '/Users/USER/Pictures/project/coins/all_coins/coin_1.png'
#image, new_image = crop_and_remove_coins(image_path)

#cv2.imshow('Cropped Image', image)#
#cv2.waitKey(0)#
#cv2.destroyAllWindows()#

#cv2.imshow('new Image', new_image)#
#cv2.waitKey(0)#
#cv2.destroyAllWindows()#










