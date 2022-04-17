from retinaface import RetinaFace
import cv2
import numpy as np

def check_valid(image, model):
    try:
        faces = RetinaFace.detect_faces(img_path = image, threshold=0.999)
    except:
        return "Can't detect face in your  frame", False
    print(faces)
    if len(faces) >1:
        return "Over 1 face in your frame", False
    if type(faces) != dict:
        
        return "Can't detect face in your frame", False
    x1,y1,x2,y2 = faces['face_1']["facial_area"]
    
    im_crop = image[y1:y2, x1:x2]
    img_quality = cv2.resize(im_crop,(224,224))/255.0
    img_quality = np.expand_dims(img_quality, axis = 0)
    
    rs = model.predict(img_quality)
    
    if np.argmax(rs[0]) !=2:
        return "Your face is not True", False
    
    return im_crop, True

