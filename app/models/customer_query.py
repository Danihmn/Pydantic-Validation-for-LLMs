from typing import Literal

from pydantic import Field

from app.models.user_input import UserInput


class CustomerQuery(UserInput):
    priority: str = Field(description="priority of the customer")
    category: Literal[
        "refund_request", "information_request", "other"
    ] = Field(description="category of the customer")
    is_complaint: bool = Field(description="is complaint")
    tags: list[str] = Field(description="tags of the customer")
