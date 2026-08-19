from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from models.customer_query import CustomerQuery
from settings import settings


def create_customer_query(valid_user_json: str) -> CustomerQuery:
    model = OpenAIChatModel(
        settings.deployment_name,
        provider=OpenAIProvider(base_url=settings.endpoint, api_key=settings.api_key),
    )
    customer_query_agent = Agent(model=model, output_type=CustomerQuery)
    response = customer_query_agent.run_sync(valid_user_json)
    print("CustomerQuery generated...")
    return response.output
