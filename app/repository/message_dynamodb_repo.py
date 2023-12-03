import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from app.models.message import Message
from app.utils.app_logger import app_logger as log


class MessageDynamoDBRepo:

    def __init__(self):
        session = boto3.Session()
        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table("messages")

    def add_message(self, message: Message):
        try:
            log.info(f"Saving {message} into table %s", self.table.name)
            self.table.put_item(Item=message.dict())
        except ClientError as err:
            log.error(
                "Couldn't save message into table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_messages_by_chat_id(self, chat_id: str):
        try:
            log.info(f"Getting messages with chat_id {chat_id} from table %s", self.table.name)
            filtering_exp = Key('chat_id').eq(chat_id)
            response = self.table.query(
                KeyConditionExpression=filtering_exp
            )
            return response['Items']
        except ClientError as err:
            log.error(
                "Couldn't get messages from table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_message_by_message_id(self, message_id: str):
        try:
            log.info(f"Getting message with id {message_id} from table %s", self.table.name)
            response = self.table.query(
                IndexName='MessageIdIndex',
                KeyConditionExpression=Key('message_id').eq(message_id)
            )
            return response['Item']
        except ClientError as err:
            log.error(
                "Couldn't get message from table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
