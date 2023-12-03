import boto3
from botocore.exceptions import ClientError

from app.utils.app_logger import app_logger as log
from app.models.user import User


class UserDynamoDBRepo:

    def __init__(self):
        session = boto3.Session()
        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table("users")

    def create_user(self, user: User):
        try:
            log.info(f"Saving {user} into table %s", self.table.name)
            self.table.put_item(Item=user.dict())
        except ClientError as err:
            log.error(
                "Couldn't save user into table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_user(self, user_id):
        try:
            log.info(f"Getting user with id {user_id} from table %s", self.table.name)
            response = self.table.get_item(Key={'id': user_id})
            return response['Item']
        except ClientError as err:
            log.error(
                "Couldn't get user from table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
