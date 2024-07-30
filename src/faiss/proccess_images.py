import faiss
import numpy as np

from src.faiss.index_manager import IndexManager
index_manager = IndexManager('organization_name')

def proccess_images(doc, index_manager=index_manager):
    embedding = doc['insight_data']['embedding']
    query = np.array(embedding).astype(np.float32).reshape(1, -1)
    faiss.normalize_L2(query)
    scores, ids = index_manager.search_employee(query)
    if scores < 0.6:
        send_report(doc, scores, ids)
    else:
        scores, ids = index_manager.search_client(query)
        if scores < 0.6:
            send_report(doc, scores, ids)
        else:
            print('Unknown person')
