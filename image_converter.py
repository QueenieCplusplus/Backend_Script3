# 2020.4/20, pm 10:30, by Vivy Chen (Queen)
    """
    A function to resize an image to fit within a given size
    :param image: image to resize
    :param width: in pixels
    :param height: in pixels
    :return: the resized image
    """
import imutils
import cv2
# CV2 usage: pip install opencv-python

def resize_img(image, width, height):

    (h, w) = image.shape[:2]

    # if the width is greater than the height then resize along
    # the width
    if w > h:
        img = imutils.resize(image, width=width)

    # otherwise, the height is greater than the width so resize
    # along the height
    else:
        img = imutils.resize(image, height=height)

    # determine the padding val for the w & h to obtain the target dimensions
    pad_W = int((width - img.shape[1]) / 2.0)
    pad_H = int((height - img.shape[0]) / 2.0)

    # pad the image then apply one more resizing to handle any rounding issues
    image = cv2.copyMakeBorder(image, pad_H, pad_H, pad_W, pad_W, cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))

    # return the pre-processed image
    return image

if __name__ == "__main__":
    image = ''
    width = 100
    height = 100
    resize_img(image, width, height)