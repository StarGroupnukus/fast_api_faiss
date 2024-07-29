import os
from src.config.config import Config
from src.insightface.singleton import FaceAnalysisSingleton
import cv2
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGODB_LOCAL'))
        self.db = self.client.biz_count
        self.employees = self.db.employees
        self.clients = self.db.clients
        self.counters = self.db.counters
        self.initialize_counter('client_id')

    def init_clients_db(self):
        image = cv2.imread(Config.INIT_IMAGE_PATH)
        face_data = FaceAnalysisSingleton().get_app().get(image)[0]
        client_data = {
            "person_id": 0,
            "embedding": face_data.embedding.tolist(),
        }
        self.clients.insert_one(client_data)

    def initialize_counter(self, counter_id):
        if self.counters.find_one({'_id': counter_id}) is None:
            self.counters.insert_one({'_id': counter_id, 'seq': 0})
            self.init_clients_db()

    def increment_counter(self, counter_id):
        return self.counters.find_one_and_update(
            {'_id': counter_id},
            {'$inc': {'seq': 1}},
            upsert=True,
            return_document=True
        )['seq']
