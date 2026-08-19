from pydantic_ai import Agent

from models.customer_query import CustomerQuery
from settings import settings


def create_customer_query(valid_user_json: str) -> CustomerQuery:
    customer_query_agent = Agent(
        model=settings.deployment_name,
    )
    response = customer_query_agent.run_sync(valid_user_json)
    print("CustomerQuery generated...")
    return response.output
