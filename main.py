import json
import os
from typing import Annotated

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse



from src.database.database import create_document

IMAGE_DIRECTORY = 'files/images'
os.makedirs(IMAGE_DIRECTORY, exist_ok=True)

# Create FastAPI instance
app = FastAPI(
    title="FastAPI Tutorial",
    description="A simple REST API using FastAPI",
    version="1.0.0",
    author="Star Group Nokis",
    license_info={
        "name": "MIT License",
        "url": "https://spdx.org/licenses/MIT.html",
        "description": "License for FastAPI Tutorial"
    },
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/data")
async def create_data(
    data: Annotated[str, Form()],
    image_file: Annotated[UploadFile, File()],
    orig_image_file: Annotated[UploadFile, File()]
):

    response_data = await create_document(data, image_file, orig_image_file)

    return response_data

@app.get('/images/{file_path}')
async def get_image(file_path: str):
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not "}

