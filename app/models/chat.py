from pydantic import BaseModel
from typing import List

class Chat(BaseModel):
    chat_id: str
    chat_participant_ids: List[str]
    language_preference: str = ''
    last_message_id: str = ''
    last_message_timestamp: str = ''
    is_self_chat: bool = False
