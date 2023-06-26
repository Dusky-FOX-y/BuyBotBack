from pydantic import BaseModel


class CreateGood(BaseModel):
    name: str
    value: float


class GetGood(CreateGood):
    id_: int