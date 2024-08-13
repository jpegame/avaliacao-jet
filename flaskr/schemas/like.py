from marshmallow import Schema, fields
from flaskr.schema import ma

class LikeResponseSchema(ma.Schema):
    id = fields.Int()
    post_id = fields.Int()
    author_id = fields.Int()
    class Meta:
        fields = ("id", "post_id","author_id")
        ordered = True
        
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("like")
        }
    )

class LikeRequestPostSchema(Schema):
    post_id = fields.Integer(required=False, help='This field cannot be blank')
    author_id = fields.Integer(required=False, help='This field cannot be blank')
    
class LikeRequestGetSchema(Schema):
    id = fields.UUID(required=True, default='id', help='Invalid id')
    
class LikeRequestPutSchema(LikeRequestPostSchema):
    id = fields.UUID(required=True, default='id', help='ID invalido')
    
class LikeRequestDeleteSchema(Schema):
    id = fields.UUID(required=True, default='id', help='ID invalido')
    
like_schema = LikeResponseSchema()