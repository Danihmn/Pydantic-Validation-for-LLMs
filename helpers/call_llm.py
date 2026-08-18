from client import client
from settings import settings


def call_llm(prompt):
    response = client.chat.completions.create(
        model=settings.deployment_name,
        messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content
