from fastapi import APIRouter, status

from app.service.chat_service import get_chat_service
from app.utils.app_logger import app_logger as log

chat_api_router = APIRouter()
chat_service = get_chat_service()

@chat_api_router.post("/chat", status_code=status.HTTP_200_OK)
def create_chat(user_id: str, contact_id: str):
    log.info(f"Received request to create chat between {user_id} and {contact_id}")
    return chat_service.create_chat(user_id, contact_id)

@chat_api_router.get("/chat", status_code=status.HTTP_200_OK)
def get_chat_details(chat_id: str):
    log.info(f"Retrieving chat details for chat_id {chat_id}")
    return chat_service.get_chat_details(chat_id)
