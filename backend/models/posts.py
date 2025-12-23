from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

DataBase_URL = "sqlite:///database.db"
engine = create_engine(DataBase_URL, echo=True)

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    author = Column(String)
    title = Column(String)
    message = Column(String)

#Create tables
Base.metadata.create_all(engine)  

#Create Session
Session = sessionmaker(bind=engine)
session = Session()

def create_post(author, message):
    try:
        new_post = Post(author=author, message=message)
        session.add(new_post)
        session.commit()
        return new_post
    except Exception as e:
        session.rollback()
        print(f"error creating new post")
        return None
    
def get_post_by_id(post_id = id):
    """Get post by ID"""
    try:
        return session.query(Post).filter_by(id=post_id).first()
    except Exception as e:
        print(f"Error getting post by ID: {e}")
        return None
    
def get_post_by_title(title):
    """Get post by title"""
    try:
        return session.query(Post).filter_by(title=title).first()
    except Exception as e:
        print(f"Error getting post by title: {e}")
        return None