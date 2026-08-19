import datetime
from typing import Literal, Optional

from pydantic import Field

from models.customer_query import CustomerQuery
from models.order_details import OrderDetails


class SupportTicket(CustomerQuery):
    recommended_next_action: Literal[
        'escalate_to_agent', 'send_faq_response',
        'send_order_status', 'no_action_needed'
    ] = Field(
        ..., description="LLM's recommended next action for support"
    )
    order_details: Optional[OrderDetails] = Field(
        None, description="Order details if action is send_order_status"
    )
    faq_response: Optional[str] = Field(
        None, description="FAQ response if action is send_faq_response"
    )
    creation_date: datetime.datetime = Field(
        ..., description="Date and time the ticket was created"
    )
