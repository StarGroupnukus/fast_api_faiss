import cv2
import numpy as np
import urllib.request
from singleton import FaceAnalysisSingleton
from util import get_faces_data

class FaceProcessor:
    def __init__(self):
        self.app = FaceAnalysisSingleton().get_app()

    def get_faces(self, image):
        return self.app.get(image)

    @staticmethod
    def process_image(self, image_path):
        image = cv2.imread(image_path)
        return self.get_faces(image)
    
    @staticmethod
    def get_face(req):
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        app = FaceAnalysisSingleton().get_app()
        faces = app.get(img)
        return get_faces_data(faces)


