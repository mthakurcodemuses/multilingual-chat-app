from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from app.models.message import Message
from fastapi import Form, status
def form_data_message_parser(data: str = Form(...)):
    try:
        return Message.parse_raw(data)
    except ValidationError as e:
        raise HTTPException(
            detail=jsonable_encoder(e.errors()),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )