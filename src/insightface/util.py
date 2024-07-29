import numpy as np
from numpy.linalg import norm


def compute_sim(feat1, feat2, ):
    try:
        feat1 = feat1.ravel()
        feat2 = feat2.ravel()
        sim = np.dot(feat1, feat2) / (norm(feat1) * norm(feat2))
        return sim
    except Exception as e:
        return None


def calculate_rectangle_area(bbox):
    # Вычисляет площадь прямоугольника
    if len(bbox) != 4:
        raise ValueError("bbox должен содержать четыре координаты: x_min, y_min, x_max, y_max")
    return (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])


def get_faces_data(faces):
    # Возвращает данные о лице с максимальной площадью прямоугольника
    if not faces:
        return False
    return max(faces, key=lambda face: calculate_rectangle_area(face["bbox"]))
