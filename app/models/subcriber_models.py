from pydantic import BaseModel


class SubscriberRequest(BaseModel):
    user_name: str
    email_address: str
