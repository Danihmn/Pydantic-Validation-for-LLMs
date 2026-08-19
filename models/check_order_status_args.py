from pydantic import BaseModel, Field, EmailStr, field_validator
import re


class CheckOrderStatusArgs(BaseModel):
    order_id: str = Field(description="Customer's order ID (format: ABC-12345)")
    email: EmailStr = Field(description="Customer's email address")

    @field_validator("order_id")
    def validate_order_id(cls, order_id):
        pattern = r"^[A-Z]{3}-\d{5}$"
        if not re.match(pattern, order_id):
            raise ValueError(
                "order_id must be in format ABC-12345 "
                "(3 uppercase letters, dash, 5 digits)"
            )
        return order_id
