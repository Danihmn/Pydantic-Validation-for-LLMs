import json

from client import client
from helpers.tool_definitions import tool_definitions
from models.customer_query import CustomerQuery
from models.support_ticket import SupportTicket
from settings import Settings, settings


def decide_next_action_with_tools(customer_query: CustomerQuery):
    support_ticket_schema = json.dumps(
        SupportTicket.model_json_schema(), indent=2
    )
    system_prompt = f"""
        You are a helpful customer support agent. Your job is to 
        determine what support action should be taken for the customer, 
        based on the customer query and the expected fields in the 
        SupportTicket schema below. If more information on a particular 
        order_id or FAQ response would be helpful in responding to the 
        user query and can be obtained by calling a tool, call the 
        appropriate tool to get that information. If an order_id is 
        present in the query, always look up the order status to get 
        more information on the order.

        Here is the JSON schema for the SupportTicket model you must 
        use as context for what information is expected:
        {support_ticket_schema}
    """
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
