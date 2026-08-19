from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, field_validator


class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str = Field(description="query string to search for", min_length=6)
    order_id: Optional[str] = Field(None, description="order id if available (format: ABC-12345)")

    @field_validator("order_id")
    def validate_order_id(cls, order_id):
        if order_id is None:
            return order_id
        pattern = r"^[A-Z]{3}-\d{5}$"
        if not re.match(pattern, order_id):
            raise ValueError(
                "order_id must be in format ABC-12345 "
                "(3 uppercase letters, dash, 5 digits)"
            )
        return order_id
