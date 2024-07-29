import json
import os
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from src.schemas import PredictImage
from aiofiles import open as aio_open

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = "mydatabase"

# Connect to MongoDB
client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]


async def create_document(data, img_path1, img_path2):
    now = datetime.now()
    image_directory = os.path.join("files/images", now.strftime('%Y-%m-%d'))
    os.makedirs(image_directory, exist_ok=True)

    data_dict = json.loads(data)
    predict_image = PredictImage(**data_dict)

    timestamp = predict_image.time.strftime('%H-%M-%S-%f')
    image_path = os.path.join(image_directory, f"{timestamp}_image.jpg")
    orig_image_path = os.path.join(image_directory, f"{timestamp}_orig.jpg")

    for path, img_path in zip([image_path, orig_image_path], [img_path1, img_path2]):
        async with aio_open(path, "wb") as f:
            await f.write(await img_path.read())

    insight_data_dict = {**predict_image.model_dump(), "image_path": image_path, "orig_image_path": orig_image_path}

    insight_data_result = await database["insight_data"].insert_one(insight_data_dict)
    document = await database["insight_data"].find_one({"_id": insight_data_result.inserted_id})

    response_data = {
        "image_path": image_path,
        "orig_image_path": orig_image_path,
        "insight_data": document.get("insight_data", {}),
        "device_id": document.get("device_id", ""),
        "time": document.get("time", "")
    }

    return response_data

