from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
import os
import uuid
from random import randint

app = FastAPI()

IMAGEDIR = "./Images/"
os.makedirs(IMAGEDIR, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        # Use the original filename
        file.filename = f"{uuid.uuid4()}.jpg"
        contents = await file.read()

        with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
            f.write(contents)

        return {"filename": file.filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@app.get("/show/")
async def read_random_file():
    # get random file from the image directory
    files = os.listdir(IMAGEDIR)

    if not files:
        raise HTTPException(status_code=404, detail="No images found")

    random_index = randint(0, len(files) - 1)

    path = f"{IMAGEDIR}{files[random_index]}"

    return FileResponse(path)
