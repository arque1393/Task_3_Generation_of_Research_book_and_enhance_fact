from pydantic import BaseModel

class Query(BaseModel):
    text:str
    temperature : float
    