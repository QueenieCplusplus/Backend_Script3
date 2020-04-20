# 2020, 4/20, pm10:00, by Vivy Chen (Queen)

from keras.models import load_model
import os, cv2
# CV2 usage: pip install opencv-python==1.18.0
from pytesseract import defactor, set_rect
# https://github.com/QueenieCplusplus/Backend_Script3/blob/master/pytesseract.py
import numpy as np

# import tensorflow as tf
# from keras.backend import set_session
# num_cores = 4
# config = tf.ConfigProto(intra_op_parallelism_threads = num_cores,
#                         allow_soft_placement = True,
#                         device_count = {'CPU' : 1, 'GPU' : 0})
# session = tf.Session(config=config)
# set_session(session)

os.environ["CUDA_VISIBLE_DEVICES"] = '-1'

MODEL_FILENAME = "captcha_digits.h5"
CLASS_INDICES = {0: '2', 1: '3', 2: '4', 3: '6', 4: '7', 5: '8', 
                 6: '9', 7: 'A', 8: 'C', 9: 'D', 10: 'E',
                 11: 'F', 12: 'G', 13: 'H', 14: 'J', 15: 'K', 
                 16: 'L', 17: 'N', 18: 'P', 19: 'Q', 20: 'R',
                 21: 'T', 22: 'U', 23: 'V', 24: 'X', 25: 'Y', 
                 26: 'Z'}
captcha_model = None

def predict_text(image_path):
    global captcha_model
    dir_path = os.path.dirname(os.path.abspath(__file__))
              
    # Load the trained neural network
    if not captcha_model:
        captcha_model = load_model(os.path.join(dir_path, MODEL_FILENAME))

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = defactor(image)
    array = set_rect(img)
    
    # declair an empty array
    letter_images = []
    for id, (x,y,w,h) in enumerate(array):
        return_result = image[y:y+h, x:x+w]
                
        # Resize the letter so it fits in a 32 x 32 pixel box
        resize_img = cv2.resize(return_result , (32,32))
        # set colour
        x = cv2.cvtColor(resize_img, cv2.COLOR_GRAY2RGB)

        # to array
        x = np.asarray(x)

        # to int type
        x = x.astype('float32')

        # divide by 255
        x /= 255.

        # to append an array
        letter_images.append(x)

    letter_images = np.array(letter_images)

    # Ask the neural network to make a prediction
    pred = np.argmax(captcha_model.predict(letter_images), axis=1)

    # Convert the one-hot-encoded prediction back to a normal letter
    predictions = np.vectorize(CLASS_INDICES.get)(pred)
          
    return predictions

def save_char(predictions):

    letter = predictions[0]
    letter_folder = os.path.join(dir_path, "extracted_letter_img", letter)
    num = max(map(lambda x: int(x.replace('.png','')), os.listdir(letter_folder))) if os.listdir(letter_folder) else 0
    filename = os.path.join(letter_folder, '{:06}.png'.format(num+1))
    
    # image_path
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = defactor(image)
    array = set_rect(img)
    
    for id, (x,y,w,h) in enumerate(array):
        return_result = image[y:y+h, x:x+w]
        cv2.imwrite(filename, return_result)
        print(filename)

if __name__ == "__main__":
    image_path=''
    pred = predict_text(image_path)
    save_char(pred)
    
        
