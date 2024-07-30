import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    CHECK_NEW_CLIENT = 0.5
    THRESHOLD_IS_DB = 60
    POSE_THRESHOLD = 40
    DET_SCORE_THRESH = 0.65
    IMAGE_COUNT = 10
    THRESHOLD_ADD_DB = 65
    DIMENSIONS = 512
    INDEX_UPDATE_THRESHOLD = 5
    INIT_IMAGE_PATH = './pavel.png'
    MONGODB_URL = os.getenv('MONGODB_LOCAL')
    DATABASE_NAME = 'my_database'

class ApiConfig:
    API_HOST = 'test'
    API_PORT = 5000