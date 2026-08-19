import json

from app.clients.openai import client
from app.tools.definitions import tool_definitions
from app.models.customer_query import CustomerQuery
from app.models.support_ticket import SupportTicket
from app.prompts.support_action import build_support_action_prompt
from app.config.settings import settings


def decide_next_action_with_tools(customer_query: CustomerQuery):
    support_ticket_schema = json.dumps(
        SupportTicket.model_json_schema(), indent=2
    )
    system_prompt = build_support_action_prompt(support_ticket_schema)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": str(customer_query.model_dump())}
    ]
    response = client.chat.completions.create(
        model=settings.deployment_name,
        messages=messages,
        tools=tool_definitions,
        tool_choice="auto"
    )
    message = response.choices[0].message
    tool_calls = getattr(message, "tool_calls", None)
    return message, tool_calls, messages
