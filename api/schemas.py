from pydantic import BaseModel

class ModelInput(BaseModel):
    caa: int
    thalachh: int
    cp: int
    thall: int
    oldpeak: float
    age: int
    trtbps: int
    chol: int
    exng: int
    slp: int

class ModelResult(BaseModel):
    result: bool