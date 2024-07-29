from insightface.app import FaceAnalysis

class FaceAnalysisSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FaceAnalysisSingleton, cls).__new__(cls)
            cls._instance.app = FaceAnalysis()
            cls._instance.app.prepare(ctx_id=0)
        return cls._instance

    def get_app(self):
        return self.app