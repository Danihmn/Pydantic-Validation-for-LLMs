from pydantic import BaseModel


class OrderDetails(BaseModel):
    status: str
    estimated_delivery: str
    note: str
