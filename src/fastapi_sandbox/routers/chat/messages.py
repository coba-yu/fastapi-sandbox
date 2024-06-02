from typing import Any

from fastapi import APIRouter, Body, Path
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/chat/messages",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


class MessageFile(BaseModel):
    id: str
    type: str
    url: str
    belongs_to: str


class MessageFeedback(BaseModel):
    rating: str = Field(default=None, title="Upvote as `like`, downvote as `dislike`, revoke upvote as `null`.")


class RetrieverResource(BaseModel):
    position: int
    dataset_id: str
    dataset_name: str
    document_id: str
    document_name: str
    segment_id: str
    score: float
    content: str


class Message(BaseModel):
    id: str = Field(title="Message ID.")
    conversation_id: str = Field(title="Conversation ID.")
    query: str = Field(title="User input / question content.")
    answer: str = Field(title="Response message content.")
    created_at: int = Field(title="Creation timestamp, e.g., 1705395332.")

    inputs: dict = Field(default_factory=dict, title="User input parameters.")
    message_files: list[MessageFile] = Field(
        default_factory=list,
        title="Message files.",
    )
    feedback: MessageFeedback = Field(None, title="Feedback information.")
    retriever_resource: list[RetrieverResource] = Field(
        default_factory=list,
        title="Citation and Attribution List.",
    )


class MessageList(BaseModel):
    data: list[Message] = Field(title="Message list.")
    has_more: bool = Field(title="Whether there is a next page.")
    limit: int = Field(
        title="Number of returned items, if input exceeds system limit, returns system limit amount.",
    )


@router.get("/", response_model=MessageList)
def list_messages(username: str, user_token: str) -> Any:
    # TODO: Implement
    print(f"{username=}, {user_token=}")
    return MessageList(
        data=[
            Message(
                id="a076a87f-31e5-48dc-b452-0061adbbc922",
                conversation_id="cd78daf6-f9e4-4463-9ff2-54257230a0ce",
                query="iphone 13 pro",
                answer=(
                    "The iPhone 13 Pro, released on September 24, 2021, features a 6.1-inch display with a resolution "
                    "of 1170 x 2532. It is equipped with a Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard) "
                    "processor, 6 GB of RAM, and offers storage options of 128 GB, 256 GB, 512 GB, and 1 TB. The "
                    "camera is 12 MP, the battery capacity is 3095 mAh, and it runs on iOS 15."
                ),
                created_at=1705569239,
            )
        ],
        has_more=False,
        limit=1,
    )


@router.post("/{message_id}/feedbacks")
def feedback_message(
    message_id: str = Path(),
    rating: str = Body(),
    username: str = Body(),
    user_token: str = Body(),
) -> Any:
    # TODO: Implement
    print(f"{username=}, {user_token=}, {message_id=}, {rating=}")
    return {"status": "success"}
