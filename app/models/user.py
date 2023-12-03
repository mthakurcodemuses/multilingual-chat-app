from pydantic import BaseModel

class User(BaseModel):
    id: str = None
    username: str
    email: str = ''
    language_preference: str = 'en'
