import json
from datetime import datetime

from client import openai_client
from models.customer_query import CustomerQuery
from models.support_ticket import SupportTicket
from settings import settings


def generate_structured_support_ticket(
        customer_query: CustomerQuery, message, tool_outputs: list
):
    tool_results_str = "\n".join([
        f"Tool: {out['tool_call_id']} Output: {json.dumps(out['output'])}"
        for out in tool_outputs
    ]) if tool_outputs else "No tool calls were made."
    # Concatenate prompt parts into a single string for Anthropic
    prompt = f"""
        You are a support agent. Use all information below to 
        generate a support ticket as a validated Pydantic model.
        Customer query: {customer_query.model_dump_json(indent=2)}
        LLM message: {str(message.content)}
        Tool results: {tool_results_str}
    """
    # Create the message with structured output
    response = openai_client.messages.create(
        model=settings.deployment_name,
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_model=SupportTicket
    )

    support_ticket = response
    support_ticket.creation_date = datetime.now()
    return support_ticket
