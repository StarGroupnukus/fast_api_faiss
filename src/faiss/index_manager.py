import faiss
import numpy as np

from .util import update_database, new_create_indexes
from src.insightface.insight import FaceProcessor
from ..database.db_utils import Database


class IndexManager:
    def __init__(self, org_name):
        self.org_name = org_name
        self.client_index, self.client_indices = new_create_indexes(Database().clients)
        self.employee_index, self.employee_indices = update_database(org_name, FaceProcessor().app)

    def update_client_index(self, new_clients):
        embeddings = [np.array(client["embedding"]) for client in new_clients]
        client_ids = [client["person_id"] for client in new_clients]

        vectors = np.array(embeddings).astype('float32')
        faiss.normalize_L2(vectors)
        self.client_index.add(vectors)
        self.client_indices.extend(client_ids)

    def search_employee(self, embedding):
        query = np.array(embedding).astype(np.float32).reshape(1, -1)
        faiss.normalize_L2(query)
        scores, ids = self.employee_index.search(query, 1)
        if len(scores) == 0 or len(ids) == 0 or len(ids[0]) == 0:
            return 0, 0
        person_id = int(self.employee_indices[ids[0][0]])
        return abs(round(scores[0][0] * 100, 3)), person_id

    def search_client(self, embedding):
        query = np.array(embedding).astype(np.float32).reshape(1, -1)
        faiss.normalize_L2(query)
        scores, ids = self.client_index.search(query, 1)
        if len(scores) == 0 or len(ids) == 0 or len(ids[0]) == 0:
            return 0, 0
        person_id = int(self.client_indices[ids[0][0]])
        return abs(round(scores[0][0] * 100, 3)), person_id