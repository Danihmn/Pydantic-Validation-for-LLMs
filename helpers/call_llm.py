from client import openai_client
from models.customer_query import CustomerQuery
from settings import settings


def call_llm(prompt):
    response = openai_client.messages.create(
        model=settings.deployment_name,
        messages=[{"role": "user", "content": prompt}],
        response_model=CustomerQuery)
    return response
