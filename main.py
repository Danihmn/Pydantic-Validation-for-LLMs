from helpers.call_llm import call_llm
from helpers.create_customer_query import create_customer_query
from helpers.validate_user_input import validate_user_input
from models.user_input import UserInput

user_input_json = """
{
    "name": "Joe User",
    "email": "joe@example.com",
    "query": "When can I expect delivery of the headphones I ordered?",
    "order_id": "ABC-12345",
    "purchase_date": "2025-12-01"
}"""

valid_data = validate_user_input(user_input_json).model_dump_json()
customer_query = create_customer_query(valid_data)
print(type(customer_query))
print(customer_query.model_dump_json(indent=2))
