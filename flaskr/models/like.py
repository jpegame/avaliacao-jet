import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy_history import make_versioned
import flaskr.config_app as ca
from flaskr.db import db_instance, db_persist

make_versioned(user_cls='LikeModel')

class LikeModel(db_instance.Model):
    __versioned__ = {
        'exclude': ['created_at', 'updated_at']
    }
    __tablename__ = 'likes'
    __table_args__ = {"schema": ca.DEFAULT_DB_SCHEMA}

    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    post_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey(f'{ca.DEFAULT_DB_SCHEMA}.posts.id'))
    author_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey(f'{ca.DEFAULT_DB_SCHEMA}.users.id'))
    created_at = db_instance.Column(db_instance.DateTime(timezone=True), default=func.now())


    def __init__(self, post_id, author_id):
        self.post_id = post_id
        self.author_id = author_id
        
    @db_persist
    def save(self):
        db_instance.session.add(self)

    @db_persist
    def delete(self):
        db_instance.session.delete(self)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @staticmethod
    def init_data():
        if db_instance.session.query(LikeModel.id).count() == 0:
            for index in range(1, 6):
                post = LikeModel(post_id=index ,author_id=index)
                post.save()
                
sa.orm.configure_mappers()