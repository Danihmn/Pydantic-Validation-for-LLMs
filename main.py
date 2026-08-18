from helpers.validate_llm_response import validate_llm_response
from models.customer_query import CustomerQuery
from models.user_input import UserInput

user_input_json = '''{
    "name": "joe",
    "email": "joe@gmail.com",
    "query": "I forgot my password",
    "order_id": null
}'''

user_input = UserInput.model_validate_json(user_input_json)

example_response_structure = """{
name="Example User",
email="user@example.com",
query="I ordered a new computer monitor and it arrived with broken screen",
order_id=123456,
priority="medium",
category="refund_request",
is_complaint=True,
tags=["monitor", "support"]
}
"""

prompt = f"""
Please analyze this user query\n{user_input.model_dump_json(indent=4)}:

Return your analysis as a JSON object matching this exact structure and data types:\n
{example_response_structure}

Respond ONLY with valid JSON. Do not include any explanations or other text
or formatting before or after the JSON object.
"""

validated_data, error_message = validate_llm_response(prompt, CustomerQuery, 10)
