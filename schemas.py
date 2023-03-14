from pydantic import BaseModel
#Create ToDo Schema(Pydantic Module)
class ToDoCreate(BaseModel):
    task: str
#Complete ToDo Schema(Pydantic module)

class ToDoAll(BaseModel):
    id: int
    task: str
    class Config:
        orm_mode= True    