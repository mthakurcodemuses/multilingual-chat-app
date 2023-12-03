from datetime import datetime

from app.models.message import Message
from app.repository.message_dynamodb_repo import MessageDynamoDBRepo
from app.utils.random_id_generator import generate_message_id


class MessageService:

    def __init__(self, message_repo: MessageDynamoDBRepo):
        self.message_repo = message_repo

    def get_messages(self, chat_id):
        return self.message_repo.get_messages_by_chat_id(chat_id)

    def add_message(self, message: Message):
        # Setting default values
        message.message_id = generate_message_id()
        message.message_type = 'text' if message.text else 'audio'
        message.timestamp = str(datetime.now()) if not message.timestamp else message.timestamp
        return self.message_repo.add_message(message)

    def delete_message(self, user_id, message_id):
        user = self.user_repo.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        return self.message_repo.delete_message(user_id, message_id)


def get_message_service():
    return MessageService(MessageDynamoDBRepo())
