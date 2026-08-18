from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str = Field(description="query string to search for", min_length=6)
    order_id: Optional[int] = Field(None, description="id of the order", ge=10000)
