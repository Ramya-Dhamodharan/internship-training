# Here we will create the Python classes = database tables
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#first table 

class User(Base):
    __tablename__ = "users_orm"
    #these are the columns of new table named users_orm 
    id    = Column(Integer, primary_key=True, index=True)
    name  = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age   = Column(Integer)

#creating relationship b/w tables
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"
    

#second table

class Post(Base):
    __tablename__ = "posts_orm"

    id      = Column(Integer, primary_key=True, index=True)
    title   = Column(String(255), nullable=False)
    content = Column(Text)
    done    = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users_orm.id"))

#creating relationship b/w tables
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title})"
    



