#----------------------------------------------#
# Assignment 2                                 #
# Group 3 | Section 1                          #
# - Bilkis Musa A20EC0233                      #
# - Fatin Aimi Ayuni Binti Affindy A20EC0190   #
#----------------------------------------------#

import sys
import cv2 as cv
import numpy as np

# Default values
BORDER_SIZE = 15
CAPTION_SIZE = 50

def imageManipulate(img):
    kernel1 = np.ones((3,3),np.float32)/9 #mean filter
    kernel2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) #high boost filter c = 9

    img1 = cv.bilateralFilter(img, 100, 20, 120) #using bilateral filter
    img2 = cv.medianBlur(img1, 3) #using median blur filter
    img3 = cv.filter2D(img2, -1, kernel1) #using mean filter

    img4 = cv.bilateralFilter(img3, 31, 20, 10) #using bilateral filter
    img5 = cv.filter2D(img4, -1, kernel2) #using high boost filter
    dst = cv.medianBlur(img5, 7) #using median blur filter

    return dst

def display(image1, image2):
    height, width, channel = image1.shape

    border = np.ones((height, BORDER_SIZE, channel), np.uint8)*255
    caption = np.ones((CAPTION_SIZE, 2*width+BORDER_SIZE,channel), np.uint8)*255

    image = np.concatenate((image1, border, image2), axis=1)
    image = np.concatenate((image, caption), axis=0,)

    cv.imshow('Image Restoration', image)

def processCommandLine():

    file1 = sys.argv[1]
    image1 = cv.imread(file1)
    image2 = imageManipulate(image1)
    cv.imwrite(sys.argv[2], image2)
    return image1, image2

def main():
    images = [None, None]

    images[0], images[1], = processCommandLine()

    display(images[0], images[1])

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

#Solution2.py Noise/ImgA13.jpg Restored/ImgA13_Solution2.jpg
#Solution2.py Noise/ImgB13.jpg Restored/ImgB13_Solution2.jpg
#Solution2.py Noise/ImgC13.jpg Restored/ImgC13_Solution2.jpg
#similarity.py Original/ImgA13.jpg Restored/ImgA13_Solution2.jpg
#similarity.py Original/ImgB13.jpg Restored/ImgB13_Solution2.jpg
#similarity.py Original/ImgC13.jpg Restored/ImgC13_Solution2.jpg