from pydantic import BaseModel, Field

class PassageModel(BaseModel):
    body: str | None = Field(
        default=None, title="The ", max_length=5000
    )

