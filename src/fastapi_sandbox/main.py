from fastapi import FastAPI

from .routers import accounts
from .routers.chat import chat_messages, conversations, files

app = FastAPI()
app.include_router(accounts.router)
app.include_router(chat_messages.router)
app.include_router(conversations.router)
app.include_router(files.router)
