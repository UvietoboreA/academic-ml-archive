from pydantic import BaseModel

class NoteParam(BaseModel):
    variance: float
    skewness: float 
    curtosis: float
    entropy: float