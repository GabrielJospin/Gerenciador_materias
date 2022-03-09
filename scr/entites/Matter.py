from pydantic import BaseModel


class Matter(BaseModel):
    matter_id: int
    semester: int
    name: str
    code: str
    teacher: str
    description: str
    color_hex: str
    page: str




