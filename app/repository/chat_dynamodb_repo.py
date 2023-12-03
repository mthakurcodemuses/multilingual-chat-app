import boto3
from botocore.exceptions import ClientError

from app.utils.app_logger import app_logger as log
from app.models.chat import Chat


class ChatDynamoDBRepo:

    def __init__(self):
        session = boto3.Session()
        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table("chats")

    def create_chat(self, chat: Chat):
        try:
            log.info(f"Saving {chat} into table %s", self.table.name)
            self.table.put_item(Item=chat.dict())
        except ClientError as err:
            log.error(
                "Couldn't save chat into table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_chat_details(self, chat_id):
        try:
            log.info(f"Retrieving chat details for chat_id {chat_id}")
            response = self.table.get_item(Key={"chat_id": chat_id})
            return response.get("Item")
        except ClientError as err:
            log.error(
                "Couldn't retrieve chat details for chat_id %s. Here's why: %s: %s",
                chat_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
