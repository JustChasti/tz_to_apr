from pydantic import BaseModel


class PostModel(BaseModel):
    text: str
