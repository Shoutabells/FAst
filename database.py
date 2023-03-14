from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#Create a Sqlite engine instance 
engine = create_engine("sqlite:///todo.db")
#Create a DeclaritiveMeta instance
Base=declarative_base()
#Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
#Pre-defined requisites for creating the database