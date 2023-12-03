from app.models.chat import Chat
from app.repository.chat_dynamodb_repo import ChatDynamoDBRepo
from app.repository.user_dynamodb_repo import UserDynamoDBRepo
from app.utils.random_id_generator import generate_chat_id

class ChatService:

    def __init__(self, chat_repository: ChatDynamoDBRepo, user_repository: UserDynamoDBRepo):
        self.chat_repository = chat_repository
        self.user_repository = user_repository

    def create_chat(self, user_id, contact_id):
        chat = Chat(
            chat_id=generate_chat_id(user_id, contact_id),
            chat_participant_ids=[user_id, contact_id],
            is_self_chat=False,
        )
        return self.chat_repository.create_chat(chat)

    def get_chat_details(self, chat_id):
        return self.chat_repository.get_chat_details(chat_id)

def get_chat_service():
    return ChatService(ChatDynamoDBRepo(), UserDynamoDBRepo())