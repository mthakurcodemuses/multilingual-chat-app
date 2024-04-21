from typing import List

from fastapi import APIRouter, status, UploadFile, File, Depends, Request, Response

from app.models.message import Message
from app.service.message_service import get_message_service
from app.utils.api_request_util import form_data_message_parser
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


@message_api_router.post("/voice/message", status_code=status.HTTP_200_OK)
async def add_voice_message(request: Request, message: Message = Depends(form_data_message_parser), file: UploadFile = File(...)):
    log.info(f"Received voice message with details {message}")
    file_content = await file.read()
    file_content_type = file.content_type
    return message_service.add_message(message, file_content, file_content_type)

@message_api_router.get("/voice/message", status_code=status.HTTP_200_OK)
async def get_voice_message(chat_id: str, message_id: str):
    log.info(f"Received request to get voice message for message_id {message_id} in chat_id {chat_id}")
    audio_message_file = message_service.get_voice_message(chat_id, message_id)
    return Response(audio_message_file['Body'].read(), media_type=audio_message_file['ContentType'])
