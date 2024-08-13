from marshmallow import Schema, fields
from flaskr.schema import ma

class CommentResponseSchema(ma.Schema):
    id = fields.Int()
    body = fields.Str()
    post_id = fields.Int()
    author_id = fields.Int()
    class Meta:
        fields = ("id", "body", "post_id","author_id")
        ordered = True
        
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("comment")
        }
    )

class CommentRequestPostSchema(Schema):
    body = fields.Str(required=False, help='This field cannot be blank')
    post_id = fields.Integer(required=False, help='This field cannot be blank')
    author_id = fields.Integer(required=False, help='This field cannot be blank')
    
class CommentRequestGetSchema(Schema):
    id = fields.UUID(required=True, default='id', help='Invalid id')
    
class CommentRequestPutSchema(CommentRequestPostSchema):
    id = fields.UUID(required=True, default='id', help='ID invalido')
    
class CommentRequestDeleteSchema(Schema):
    id = fields.UUID(required=True, default='id', help='ID invalido')
    
comment_schema = CommentResponseSchema()