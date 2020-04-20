# 2020, 4/20, pm 3:40, by Vivy (Queen)
# detect letter in Image
# CV2 usage: pip install opencv-python

import numpy as np
import pytesseract as ptct # call its fun called img_to_string
from opencv import cv2  # to do resize image
import anObject # to have an image resorce

# method called img_to_string from object of pytesseract
def ocr_captcha(image):
    # return OCR result 
    # format: ( list of ocr digit text, list of digit image)
    # detail_img = defactor(image)
    img = image
    array = set_rect(img)

    text_list = []
    img_list = []

    for id, (x,y,w,h) in enumerate(array):

        result = img[y:y+h, x:x+w]
        thresh = result.copy()

        return_img = cv2.resize(thresh, (50,50))
        boarder_add = np.pad(return_img, pad_width=10, mode='constant', constant_values=0)

        text = ptct.image_to_string(boarder_add, lang='eng', config="--psm 8 --oem 4")
        if len(text)>1:
            text = ptct.image_to_string(boarder_add, lang='eng', config="--psm 8 --oem 4")
        text_list.append(text)
        
        ori = image[y:y+h, x:x+w]
        img_list.append(ori)
        
    return text_list, img_list


def set_rect(image):
    img, contours, hierarchy = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x: x[1])

    # find contours 等高線
    array = []
    for (c, _) in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if w>15 and h>15:
            array.append((x,y,w,h))
    
    return array

# to modify the image
# def defactor(image):
    
#     kernel = np.ones((3,3), np.uint8)
#     erosion = cv2.erode(image, kernel, iterations=1)
#     blurred = cv2.GaussianBlur(erosion, (6,6), 0)
#     edged = cv2.Canny(blurred, 40, 160)
#     detail_img = cv2.dilate(edged, kernel, iterations=1)
    
#     return detail_img

if __name__ == '__main__':
    img_resorce = anObject()
    # modified_img = defactor(img_resorce) 
    ocr_result = ocr_captcha(img_resorce)
