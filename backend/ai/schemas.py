from pydantic import BaseModel


class ImageResponse(BaseModel):
    emotion: str
