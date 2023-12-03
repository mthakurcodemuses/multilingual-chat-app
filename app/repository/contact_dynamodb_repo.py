import boto3
from botocore.exceptions import ClientError

from app.utils.app_logger import app_logger as log
from app.models.contact import Contact


class ContactDynamoDBRepo:

    def __init__(self):
        session = boto3.Session()
        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table("contacts")

    def persist(self, contact: Contact):
        try:
            log.info(f"Saving {contact} into table %s", self.table.name)
            self.table.put_item(Item=contact)
        except ClientError as err:
            log.error(
                "Couldn't save contact into table %s. Here's why: %s: %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
