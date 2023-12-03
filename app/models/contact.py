from pydantic import BaseModel

class Contact(BaseModel):
    contact_id: str
    linked_user_id_1: str
    linked_user_id_2: str
