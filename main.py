from typing import List
from fastapi import FastAPI,status,HTTPException, Depends
from database import Base,engine,SessionLocal
from sqlalchemy.orm import Session
import schemas
import models  

Base.metadata.create_all(engine) #Database creation

app= FastAPI()
#initialize app

def get_session():
    session=SessionLocal()
    try:
        yield session
    finally:
        session.close()    

#Get API
@app.get("/")
def root():
    return "Welcome to todo apllication built with FastAPI"

# Post API
@app.post("/todo", response_model=schemas.ToDoAll, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, session: Session = Depends(get_session)):
    # create an instance of Todo Model
    todo_obj = models.ToDo(task = todo.task)
    # Add the object into our database Table
    session.add(todo_obj)
    session.commit()
    session.refresh(todo_obj)
# return the todo object
    return todo_obj 
# PUT API
@app.put("/todo/{id}", response_model=schemas.ToDoAll)
def update_todo(id: int, task: str, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table
    todo_obj = session.query(models.ToDo).get(id)
    # If the record is present in our DB table then update 
    if todo_obj:
        todo_obj.task = task
        session.commit()
    # if todo item with given id does not exists, raise exception and return 404 not found response
    if not todo_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return todo_obj
# DELETE API
@app.delete("/todo/{id}", response_model = str)
def delete_todo(id: int, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table
    todo_obj = session.query(models.ToDo).get(id)
    # Check if Todo record is present in our Database,If not then raise 404 error
    if todo_obj:
        session.delete(todo_obj)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return f"Todo task with id {id} successfully deleted"

@app.get("/todo/{id}", response_model=schemas.ToDoAll)
def read_todo(id: int, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table
    Todo_obj = session.query(models.ToDo).get(id)
# Check if there is record with the provided id, if not then Raise 404 
    Exception
    if not todo_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return todo_obj
   