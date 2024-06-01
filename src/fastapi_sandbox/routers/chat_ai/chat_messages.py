from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/chat-ai/chat-messages",
    tags=["chat-ai"],
    responses={404: {"description": "Not found"}},
)


class File(BaseModel):
    # Required
    transfer_method: str = Field(title="Transfer method, remote_url for image URL / local_file for file upload.")

    # Optional
    type: str = Field(default="image", title="Supported type: image (currently only supports image type).")
    url: str | None = Field(default=None, title="Image URL, required when transfer_method is remote_url.")
    upload_file_id: str | None = Field(
        default=None,
        title=(
            "Uploaded file ID, which must be obtained by uploading through the File Upload API in advance "
            "(when the transfer method is local_file)."
        ),
    )


class ChatMessageIn(BaseModel):
    # Required
    query: str = Field(title="User Input/Question content.")
    username: str = Field(
        title=(
            "User identifier, used to define the identity of the end-user for retrieval and statistics. "
            "Should be uniquely defined by the developer within the application."
        )
    )
    user_token: str

    # Optional
    inputs: dict = Field(
        default_factory=dict,
        title=(
            "Allows the entry of various variable values defined by the App. "
            "The inputs parameter contains multiple key/value pairs, with each key corresponding to a specific "
            "variable and each value being the specific value for that variable. Default {}."
        ),
    )
    response_mode: str = Field(
        default="streaming",
        title=(
            "`streaming` Streaming mode (recommended), implements a typewriter-like output through SSE "
            "(Server-Sent Events). `blocking` Blocking mode, returns result after execution is complete. "
            "(Requests may be interrupted if the process is long) Due to Cloudflare restrictions, the request will be "
            "interrupted without a return after 100 seconds."
        ),
    )
    conversation_id: str = Field(
        default="",
        title=(
            "Conversation ID, to continue the conversation based on previous chat records, it is necessary to pass "
            "the previous message's conversation_id."
        ),
    )
    files: list[File] = Field(
        default=[], title="File information to be sent to the chatbot. Currently, only one file can be sent at a time."
    )
    # TODO: auto_generate_name


class MessageEvent(BaseModel):
    message_id: str
    conversation_id: str
    mode: str = "chat"
    answer: str
    created_at: int


class ChatCompletionResponse(MessageEvent):
    pass


class ChunkChatCompletionResponse(BaseModel):
    # TODO
    pass


@router.post("/", response_model=ChatCompletionResponse)
def create_chat_message(chat_message: ChatMessageIn) -> Any:
    # TODO
    return {
        "message_id": "72ead2e0-99dc-43e0-a779-352f1700b484",
        "conversation_id": "969d4eb2-21e1-476b-8398-7158ec28844b",
        "mode": "chat",
        "answer": f"This is a dummy answer: {chat_message.query}",
        "created_at": 1705407629,
    }
