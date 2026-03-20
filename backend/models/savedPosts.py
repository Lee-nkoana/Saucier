from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

DataBase_URL = "sqlite:///database.db"
engine = create_engine(DataBase_URL, echo=True)

Base = declarative_base()

class SavedPosts(Base):
    __tablename__ = 'saved_posts'

    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.post_id'))

    post = relationship("Post")

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'post_id'),
    )

    def to_dict(self):
        return{
            "post_id": self.post_id,
            "user_id": self.user_id,
            "post": {
                "author": self.post.author if self.post else None,
                "title": self.post.title if self.post else None,
                "recipe": self.post.recipe if self.post else None
            }
        }

Base.metadata.create_all(engine)  

Session = sessionmaker(bind=engine)
db_session = Session()

def save_post(post_id, user_id):
    try:
        saved_post = SavedPosts(post_id=post_id, user_id=user_id)
        db_session.add(saved_post)
        db_session.commit()
        return saved_post
    except IntegrityError:
        db_session.rollback()
        print(f"Post already saved")
        return None
    except Exception as e:
        db_session.rollback()
        print(f"Error saving post: {e}")
        return None
    