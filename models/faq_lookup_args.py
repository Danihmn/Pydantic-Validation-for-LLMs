from pydantic import Field, BaseModel


class FAQLookupArgs(BaseModel):
    query: str = Field(description="user's query")
    tags: list[str] = Field(description="relevant keyword tags from the customer query")
