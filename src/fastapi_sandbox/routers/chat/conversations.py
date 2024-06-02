from typing import Any

from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/chat/conversations",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


class Conversation(BaseModel):
    id: str
    name: str
    section: str = Field(title="'today', 'yesterday', 'last_7_days', 'last_30_days', '2024_04', '2024_03', ...")
    inputs: dict = Field(
        default_factory=dict,
        title="User input parameters. Default {}.",
    )
    # TODO: introduction
    created_at: int


class ConversationList(BaseModel):
    data: list[Conversation] = Field(title="List of conversations.")
    has_more: bool
    limit: int = Field(
        title="Number of entries returned, if input exceeds system limit, system limit number is returned.",
    )


@router.get("/", response_model=ConversationList)
def read_conversations(
    username: str = Query(),
    user_token: str = Query(),
    last_id: str | None = Query(None),
    limit: int = Query(20, ge=1, le=100),
    pinned: bool = Query(False),
) -> Any:
    # TODO: Implement
    print(f"{username=}, {user_token=}, {last_id=}, {limit=}, {pinned=}")
    return ConversationList(
        data=[
            Conversation(
                id="1",
                name="Difyについて質問",
                section="last_7_days",
                inputs={"book": "book", "myName": "Lucy"},
                created_at=1679667915,
            ),
            Conversation(
                id="2",
                name="Difyについて質問",
                section="yesterday",
                inputs={"book": "book", "myName": "Lucy"},
                created_at=1679667915,
            ),
            Conversation(
                id="3",
                name="Difyについて質問",
                section="today",
                inputs={"book": "book", "myName": "Lucy"},
                created_at=1679667915,
            ),
        ],
        has_more=False,
        limit=3,
    )


@router.delete("/{conversation_id}")
def delete_conversation(conversation_id: str = Path(), username: str = Body(), user_token: str = Body()) -> Any:
    # TODO: Implement
    print(f"{username=}, {user_token=}, {conversation_id=}")
    return {"result": "success"}
