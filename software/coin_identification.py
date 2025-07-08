
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os
from PIL import Image, ImageEnhance
import  crop_coin_and_update####
from PIL import Image


def crop_and_remove_coins(image_path):
    image = cv2.imread(image_path)
    #cv2.imshow('coin', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    original_image = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 3)

    # Detect edges
    edges = cv2.Canny(blurred, 30, 150)
    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        #coin = image[y:y + h, x:x + w]
        # Crop the coin from the image

    cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), -1)

    #cv2.imshow('Coins Removed', original_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    image = image[y:y + h, x:x + w]
    #cv2.imshow('Cropped Image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return image, original_image





#print(crop_and_remove_coins('/Users/USER/Desktop/photos for project/coin_temp.png'))














def color_of_center(image):
    #image = cv2.imread(image_path)

    # Ensure the image is loaded successfully
    if image is None:
        print("Error: Unable to load image!")
    else:
        if len(image.shape) == 2:  # Grayscale image
            height, width = image.shape
            center_x = width // 2
            center_y = height // 2
            gray_value = image[center_y, center_x]
            #print(f"The grayscale value of the center pixel is: {gray_value}")
        else:  # Color image
            height, width, _ = image.shape
            center_x = width // 2
            center_y = height // 2
            bgr_value = image[center_y, center_x]
            rgb_value = (bgr_value[2], bgr_value[1], bgr_value[0])  # Convert BGR to RGB
            #print(f"The RGB value of the center pixel is: {rgb_value}")
            return rgb_value


def identification(image_path):
    image, coins_img = crop_and_remove_coins(image_path)
    #cv2.imshow('coin', image)
    #cv2.waitKey(0)

    #cv2.destroyAllWindows()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, 51)
    hsv_brightened = cv2.merge((h, s, v))
    image = cv2.cvtColor(hsv_brightened, cv2.COLOR_HSV2BGR)


    #cv2.imshow('coin', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    center_pixel = color_of_center(image)


    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    #v2.imshow('test', coins_img)
    #cv2.imshow('coin', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    image = cv2.resize(image, (10, 10))



    # Define RGB ranges for silver and gold
    silver_rgb = (183, 189, 183)
    gold_rgb = (212,175,55)

    # Calculate the distance between the center pixel and the color references
    silver_distance = np.linalg.norm(np.array(center_pixel) - np.array(silver_rgb))
    gold_distance = np.linalg.norm(np.array(center_pixel) - np.array(gold_rgb))
    #print("silver_distance",silver_distance)
    #print("gold_distance",gold_distance)
    if silver_distance < gold_distance:
        reference_folder = '/Users/USER/Pictures/project/coins/bank/silver'
        best_ssim_coin, high = identify_coin(image, reference_folder)
        print(best_ssim_coin, " ", high)
        if high > 0.50:
            print("coin", best_ssim_coin)
            return best_ssim_coin, coins_img

        else:
            return "The coin was not found.",coins_img

    else:
        reference_folder = '/Users/USER/Pictures/project/coins/bank/gold'
        best_ssim_coin, high = identify_coin(image, reference_folder)
        print(best_ssim_coin, " ", high)
        if high > 0.50:
            print(best_ssim_coin)
            return best_ssim_coin, coins_img

        else:
            return "The coin was not found.",coins_img


#### coin recogition  ###

# Function to compute SSIM for a pair of images
def compare_images(imageA, imageB):
    # Compute SSIM
    ssim_value, _ = ssim(imageA, imageB, full=True)
    return ssim_value


# Function to find the best matching coin
def identify_coin(image, reference_folder):
    test_image = image

    best_match = None
    lowest_mse = float('inf')
    highest_ssim = -1
    best_coin_mse = ""
    best_coin_ssim = ""

    # Loop through all reference coin images in the folder
    for reference_image_name in os.listdir(reference_folder):
        reference_image_path = os.path.join(reference_folder, reference_image_name)
        reference_image = cv2.imread(reference_image_path)
        reference_image = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
        reference_image = cv2.resize(reference_image, (10, 10))

        # Compare the test image with the reference image
        ssim_value = compare_images(test_image, reference_image)

        # print(f"Comparing with {reference_image_name}:  SSIM={ssim_value}")

        # Find the image with the highest SSIM (most structurally similar)
        if ssim_value > highest_ssim:
            highest_ssim = ssim_value
            best_coin_ssim = reference_image_name
    #print(highest_ssim)

    return best_coin_ssim, highest_ssim


if __name__ == '__main__':
    pass
    #best_coin_ssim,_ =identification('/Users/USER/Pictures/project/coins/bank/silver/1 shekel drawing side5.png')
    #print(best_coin_ssim)