import instructor
from openai import OpenAI

from settings import settings

openai_client = instructor.from_openai(OpenAI(base_url=settings.endpoint, api_key=settings.api_key))
