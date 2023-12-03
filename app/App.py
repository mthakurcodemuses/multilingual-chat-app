import uvicorn
from fastapi import FastAPI

from app.api.chat_api import chat_api_router
from app.api.message_api import message_api_router
from app.api.user_api import user_api_router

fast_api_app = FastAPI()
fast_api_app.include_router(user_api_router)
fast_api_app.include_router(message_api_router)
fast_api_app.include_router(chat_api_router)

if __name__ == "__main__":
    uvicorn.run(app="app.App:fast_api_app", host="127.0.0.1", port=8000, debug=True, reload=True)
