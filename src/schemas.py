from datetime import datetime
from pydantic import BaseModel
from typing import List
from enum import Enum


class SexDegree(str, Enum):
    MEN = "MEN"
    WOMEN = "WOMEN"


class InsightData(BaseModel):
    embedding: List[float]
    gender: SexDegree
    age: int
    det_score: float
    pose: List[float]


class PredictImage(BaseModel):
    device_id: int
    time: datetime
    insight_data: InsightData


