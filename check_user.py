from deepface import DeepFace
import os
from distance import findCosineDistance
import cv2

def check_user(image, user_name):
    user_img = cv2.imread(os.path.join("./users",user_name, user_name +".jpg"))
    user_img = user_img[:,:,::-1]
    embedding_img = DeepFace.represent(image, model_name = "Facenet512", enforce_detection =False)
    embedding_user = DeepFace.represent(user_img, model_name = "Facenet512", enforce_detection =False)
    if findCosineDistance(embedding_img, embedding_user) < 0.2:
        return True
    else:
        return False