from helpers.check_order_status import check_order_status
from helpers.lookup_faq_answer import lookup_faq_answer
from models.check_order_status_args import CheckOrderStatusArgs
from models.faq_lookup_args import FAQLookupArgs


def get_tool_outputs(tool_calls):
    tool_outputs = []
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.function.name == "lookup_faq_answer":
                print("Agent requested a call to the Lookup FAQ tool...")
                args = FAQLookupArgs.model_validate_json(
                    tool_call.function.arguments
                )
                result = lookup_faq_answer(args)
                tool_outputs.append({
                    "tool_call_id": tool_call.id, "output": result
                })
                print(f"Lookup FAQ tool returned {result}")
            elif tool_call.function.name == "check_order_status":
                print("Agent requested a call to Check Order Status tool...")
                args = CheckOrderStatusArgs.model_validate_json(
                    tool_call.function.arguments
                )
                result = check_order_status(args)
                tool_outputs.append({
                    "tool_call_id": tool_call.id, "output": result
                })
                print(f"Check Order Status tool returned {result}")
    return tool_outputs
