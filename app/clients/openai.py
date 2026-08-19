import instructor
from openai import OpenAI

from app.config.settings import settings

openai_client = instructor.from_openai(OpenAI(base_url=settings.endpoint, api_key=settings.api_key))
client = OpenAI(base_url=settings.endpoint, api_key=settings.api_key)
