#user
#posts
import os
from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker


BASE_DIR=os.path.dirname(os.path.realpath(__file__))

conn='sqlite:///'+os.path.join(BASE_DIR,'blog.db')


engine=create_engine(conn)


Base=declarative_base()


"""
class User:
    id:int pk
    username:str
    email:str


class Post:
    id:int pk
    title:str
    content:str
    user_id:int foreignkey
"""


class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    username=Column(String(40),nullable=False)
    email=Column(String(40),nullable=True)
    posts=relationship('Post',back_populates='author',cascade='all, delete')

    def __repr__(self):
        return f"<User {self.username}>"

class Post(Base):
    __tablename__='posts'
    id=Column(Integer(),primary_key=True)
    title=Column(String(45),nullable=False)
    content=Column(String(255),nullable=False)
    user_id=Column(Integer(),ForeignKey('users.id'))

    author=relationship('User',back_populates='posts')


    
    def __repr__(self):
        return f"<User {self.title}>"


Base.metadata.create_all(engine) #creates the database
session=sessionmaker()(bind=engine)
