from fastapi import APIRouter, status

from app.models.user import User
from app.service.user_service import get_user_service
from app.utils.app_logger import app_logger as log

user_api_router = APIRouter()
user_service = get_user_service()

@user_api_router.post("/user", status_code=status.HTTP_200_OK)
def create_user(user: User):
    log.info(f"Received request to create {user}")
    return user_service.create_user(user)

@user_api_router.get("/user", status_code=status.HTTP_200_OK)
def get_user(user_id: str):
    log.info(f"Retrieving user from database")
    return user_service.get_user(user_id)
