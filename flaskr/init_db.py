from sqlalchemy import inspect

from flaskr.db import db_instance
from flaskr.models.user import UserModel
from flaskr.models.post import PostModel
from flaskr.models.comment import CommentModel
from flaskr.models.like import LikeModel

def model_exists(model_class):
    engine = db_instance.get_engine()
    inspector = inspect(engine)
    return inspector.has_table(model_class.__tablename__, model_class.__table_args__["schema"]) \
        or inspector.has_table(model_class.__tablename__)


def init_load_data():
    if model_exists(UserModel):
        UserModel.init_data()
    if model_exists(PostModel):
        PostModel.init_data()
    if model_exists(CommentModel):
        CommentModel.init_data()
    if model_exists(LikeModel):
        LikeModel.init_data()
    
