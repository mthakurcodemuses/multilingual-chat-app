from app.models.chat import Chat
from app.models.user import User
from app.repository.chat_dynamodb_repo import ChatDynamoDBRepo
from app.repository.user_dynamodb_repo import UserDynamoDBRepo
from app.utils.random_id_generator import generate_chat_id, generate_unique_user_id


class UserService:

    def __init__(self, user_repository: UserDynamoDBRepo, chat_repository: ChatDynamoDBRepo):
        self.user_repository = user_repository
        self.chat_repository = chat_repository

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    def get_users(self):
        return self.user_repository.get_users()

    def create_user(self, user: User):
        # Generate a unique user id
        user.id = generate_unique_user_id()
        # Save the user into the database
        self.user_repository.create_user(user)
        # Create a self chat for the user
        self_chat = self.create_self_chat(user.id)
        # Return the self chat id
        return self_chat.chat_id

    def create_self_chat(self, user_id):
        self_chat = Chat(
            chat_id=generate_chat_id(user_id, None),
            chat_participant_ids=[user_id],
            is_self_chat=True,
        )
        self.chat_repository.create_chat(self_chat)
        return self_chat

    def update_user(self, user):
        return self.user_repository.update_user(user)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)


def get_user_service():
    return UserService(UserDynamoDBRepo(), ChatDynamoDBRepo())
