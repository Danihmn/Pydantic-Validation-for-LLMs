import json

from app.examples.sample_inputs import USER_INPUT_JSON, USER_JSON
from app.services.customer_query import create_customer_query
from app.services.support_agent import decide_next_action_with_tools
from app.services.support_ticket import generate_structured_support_ticket
from app.services.validation import validate_user_input
from app.tools.dispatcher import get_tool_outputs

valid_data = validate_user_input(USER_INPUT_JSON).model_dump_json()
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

valid_user_json = validate_user_input(USER_JSON).model_dump_json()
customer_query = create_customer_query(valid_user_json)
message, tool_calls, messages = decide_next_action_with_tools(
    customer_query
)
tool_outputs = get_tool_outputs(tool_calls)
support_ticket = generate_structured_support_ticket(
    customer_query, message, tool_outputs
)
print(support_ticket.model_dump_json(indent=2))
