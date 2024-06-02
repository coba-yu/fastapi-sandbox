import os
from typing import Any

from fastapi import APIRouter, File, Form, UploadFile
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/chat/files",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


class FileResponse(BaseModel):
    # Required
    id: str
    name: str
    size: int = Field(title="File size (bytes)")
    extension: str
    mime_type: str
    created_by: str
    created_at: int


@router.post("/upload", response_model=FileResponse)
def upload_file(fileb: UploadFile = File(), username: str = Form(), user_token: str = Form()) -> Any:
    # TODO: Implement
    print(f"{username=}, {user_token=}")
    os.makedirs(os.path.join("/tmp", username), exist_ok=True)
    with open(os.path.join("/tmp", username, fileb.filename), "wb") as fp:
        fp.write(fileb.file.read())
    return {
        "id": "72fa9618-8f89-4a37-9b33-7e1178a24a67",
        "name": f"{fileb.filename}",
        "size": fileb.size,
        "extension": "png",
        "mime_type": "image/png",
        "created_by": "6ad1ab0a-73ff-4ac1-b9e4-cdb312f71f13",
        "created_at": 1577836800,
    }
