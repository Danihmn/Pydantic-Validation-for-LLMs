import json

from helpers.create_customer_query import create_customer_query
from helpers.decide_next_action_with_tools import decide_next_action_with_tools
from helpers.generate_structured_support_ticket import generate_structured_support_ticket
from helpers.get_tool_outputs import get_tool_outputs
from helpers.validate_user_input import validate_user_input
from models.check_order_status_args import CheckOrderStatusArgs
from models.faq_lookup_args import FAQLookupArgs

user_input_json = """
{
    "name": "Joe User",
    "email": "joe@example.com",
    "query": "When can I expect delivery of the headphones I ordered?",
    "order_id": "ABC-12345",
    "purchase_date": "2025-12-01"
}"""

faq_db = [
    {
        "question": "How can I reset my password?",
        "answer": "To reset your password, click 'Forgot Password' on the sign-in page and follow the instructions sent to your email.",
        "keywords": ["password", "reset", "account"]
    },
    {
        "question": "How long does shipping take?",
        "answer": "Standard shipping takes 3-5 business days. You can track your order in your account dashboard.",
        "keywords": ["shipping", "delivery", "order", "tracking"]
    },
    {
        "question": "How can I return an item?",
        "answer": "You can return any item within 30 days of purchase. Visit our returns page to start the process.",
        "keywords": ["return", "refund", "exchange"]
    },
    {
        "question": "How can I delete my account?",
        "answer": "To delete your account, go to your account settings tab and select 'delete account'.",
        "keywords": ["delete", "account", "remove"]
    }
]

order_db = {
    "ABC-12345": {
        "status": "shipped", "estimated_delivery": "2025-12-05",
        "purchase_date": "2025-12-01", "email": "joe@example.com"
    },
    "XYZ-23456": {
        "status": "processing", "estimated_delivery": "2025-12-15",
        "purchase_date": "2025-12-10", "email": "sue@example.com"
    },
    "QWE-34567": {
        "status": "delivered", "estimated_delivery": "2025-12-20",
        "purchase_date": "2025-12-18", "email": "bob@example.com"
    }
}

tool_definitions = [
    {
        "type": "function",
        "function": {
            "name": "lookup_faq_answer",
            "description": "Look up an FAQ answer by matching tags to FAQ entry keywords.",
            "parameters": FAQLookupArgs.model_json_schema()
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_order_status",
            "description": "Check the status of a customer's order.",
            "parameters": CheckOrderStatusArgs.model_json_schema()
        }
    }
]

valid_data = validate_user_input(user_input_json).model_dump_json()
customer_query = create_customer_query(valid_data)
print(type(customer_query))
print(customer_query.model_dump_json(indent=2))

message, tool_calls, messages = decide_next_action_with_tools(
    customer_query
)
# Investigate the LLM's outputs before proceeding
print("LLM message:\n", json.dumps(message.model_dump(), indent=2))
print(
    "\nTool calls:\n",
    json.dumps([call.model_dump() for call in tool_calls], indent=2)
)

tool_outputs = get_tool_outputs(tool_calls)

# Print tool outputs for inspection
print("Tool outputs:\n", json.dumps(tool_outputs, indent=2))

support_ticket = generate_structured_support_ticket(
    customer_query, message, tool_outputs
)
print(support_ticket.model_dump_json(indent=2))

user_json = """
{
    "name": "Joe User",
    "email": "joe@example.com",
    "query": "I'm really not happy with this product I bought",
    "order_id": "QWE-34567",
    "purchase_date": null
}
"""

valid_user_json = validate_user_input(user_json).model_dump_json()
customer_query = create_customer_query(valid_user_json)
message, tool_calls, messages = decide_next_action_with_tools(
    customer_query
)
tool_outputs = get_tool_outputs(tool_calls)
support_ticket = generate_structured_support_ticket(
    customer_query, message, tool_outputs
)
print(support_ticket.model_dump_json(indent=2))