from app.models.customer_query import CustomerQuery


def build_support_ticket_prompt(
        customer_query: CustomerQuery, message, tool_results_str: str
) -> str:
    # Concatenate prompt parts into a single string for Anthropic
    return f"""
        You are a support agent. Use all information below to 
        generate a support ticket as a validated Pydantic model.
        Customer query: {customer_query.model_dump_json(indent=2)}
        LLM message: {str(message.content)}
        Tool results: {tool_results_str}
    """
