import json
from datetime import datetime

from app.clients.openai import openai_client
from app.models.customer_query import CustomerQuery
from app.models.support_ticket import SupportTicket
from app.prompts.support_ticket import build_support_ticket_prompt
from app.config.settings import settings


def generate_structured_support_ticket(
        customer_query: CustomerQuery, message, tool_outputs: list
):
    tool_results_str = "\n".join([
        f"Tool: {out['tool_call_id']} Output: {json.dumps(out['output'])}"
        for out in tool_outputs
    ]) if tool_outputs else "No tool calls were made."
    prompt = build_support_ticket_prompt(
        customer_query, message, tool_results_str
    )
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
