from openai import OpenAI

from settings import settings

client = OpenAI(base_url=settings.endpoint, api_key=settings.api_key)
