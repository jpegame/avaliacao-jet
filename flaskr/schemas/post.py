from marshmallow import Schema, fields
from flaskr.schema import ma

class PostResponseSchema(ma.Schema):
    id = fields.Int()
    title = fields.Str()
    body = fields.Str()
    author_id = fields.Int()
    class Meta:
        fields = ("id", "body", "title","author_id")
        ordered = True
        
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("post")
        }
    )

class PostRequestPostSchema(Schema):
    body = fields.Str(required=False, help='This field cannot be blank')
    title = fields.Str(required=False, help='This field cannot be blank')
    author_id = fields.Integer(required=False, help='This field cannot be blank')
    
class PostRequestGetSchema(Schema):
    id = fields.UUID(required=True, default='id', help='Invalid id')
    
class PostRequestPutSchema(PostRequestPostSchema):
    id = fields.UUID(required=True, default='id', help='ID invalido')
    
class PostRequestDeleteSchema(Schema):
    id = fields.UUID(required=True, default='id', help='ID invalido')
    
post_schema = PostResponseSchema()