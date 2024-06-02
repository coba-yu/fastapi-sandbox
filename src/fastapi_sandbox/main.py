from fastapi import FastAPI

from .routers import accounts
from .routers.chat import chat_messages

app = FastAPI()
app.include_router(accounts.router)
app.include_router(chat_messages.router)
