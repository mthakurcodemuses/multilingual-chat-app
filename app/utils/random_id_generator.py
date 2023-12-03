import random
import string
import time
import uuid


def generate_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_unique_user_id():
    timestamp = int(time.time() * 1000)  # Current time in milliseconds
    random_part = random.randint(1000, 9999)  # Random 4-digit number
    return f"{timestamp}{random_part}"

def generate_chat_id(user_id, contact_id):
    chat_id_random_part = generate_random_string(6)
    return f"{user_id}_{chat_id_random_part}_{contact_id}" if contact_id else f"{user_id}_{chat_id_random_part}_self_chat"

def generate_message_id():
    return str(uuid.uuid4())