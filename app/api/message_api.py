from fastapi import APIRouter, status

from app.models.message import Message
from app.service.message_service import get_message_service
from app.utils.app_logger import app_logger as log

message_api_router = APIRouter()
message_service = get_message_service()

@message_api_router.post("/message", status_code=status.HTTP_200_OK)
def add_message(message: Message):
    log.info(f"Received message with details {message}")
    return message_service.add_message(message)

@message_api_router.get("/message", status_code=status.HTTP_200_OK)
def get_messages(chat_id: str):
    log.info(f"Received request to get messages for chat_id {chat_id}")
    return message_service.get_messages(chat_id)