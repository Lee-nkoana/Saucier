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
    recipe = Column(String)

    def to_dict(self):
        return{
            "post_id": self.post_id,
            "author": self.author,
            "title": self.title,
            "recipe": self.recipe
        }

#Create tables
Base.metadata.create_all(engine)  

#Create Session
Session = sessionmaker(bind=engine)
db_session = Session()

def create_new_post(title, author, recipe):
    try:
        new_post = Post(title=title, author=author, recipe=recipe)
        db_session.add(new_post)
        db_session.commit()
        return new_post
    except Exception as e:
        db_session.rollback()
        print(f"error creating new post")
        return None
    
def get_post_by_id(post_id = id):
    """Get post by ID"""
    try:
        return db_session.query(Post).filter_by(id=post_id).first()
    except Exception as e:
        print(f"Error getting post by ID: {e}")
        return None
    
def get_post_by_title(title):
    """Get post by title"""
    try:
        return db_session.query(Post).filter_by(title=title).first()
    except Exception as e:
        print(f"Error getting post by title: {e}")
        return None
    
def get_post_by_author(author):
    """Getting posts by users name"""
    try:
        return db_session.query(Post).filter_by(author=author).all()
    except Exception as e:
        print(f"Error retreiving posts by author name: {e}")
        return []
    
def get_all_existing_posts():
    """Get all existing posts in the database"""
    try:
        return db_session.query(Post).all()
    except Exception as e:
        print(f"Error fetching posts: {e}")
        return []