from typing import Any

from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/chat/apps",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def boot_app(app: str = Body(), username: str = Body(), user_token: str = Body()) -> Any:
    # TODO: Implement
    print(f"{app=}, {username=}, {user_token=}")
    return {
        "app": app,
        "message_id": "72ead2e0-99dc-43e0-a779-352f1700b484",
        "conversation_id": "969d4eb2-21e1-476b-8398-7158ec28844b",
        "query": "引き継ぎ書の作成方法について教えてください。",
        "answer": "引き継ぎ書の作成方法については、以下の手順で行います。",
        "created_at": 1679667915,
    }
