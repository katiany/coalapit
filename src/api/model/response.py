from pydantic import BaseModel


class Response(BaseModel):
    deductible: int
    stop_loss: int
    oop_max: int