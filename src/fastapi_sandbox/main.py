from fastapi import FastAPI

from .routers import accounts
from .routers.chat import chat_messages, conversations, files, messages

app = FastAPI()
app.include_router(accounts.router)

# chat
app.include_router(chat_messages.router)
app.include_router(conversations.router)
app.include_router(files.router)
app.include_router(messages.router)
