from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_jwt_extended import jwt_required
from flask_apispec.views import MethodResource
from flask_restful import Resource
from flaskr.models.comment import CommentModel
from flaskr.schemas.comment import (CommentResponseSchema,
                                     CommentRequestPostSchema,
                                     CommentRequestGetSchema,
                                     CommentRequestDeleteSchema,
                                     CommentRequestPutSchema,
                                     comment_schema)


@doc(description='Registro de Comment', tags=['Comment'])
class CommentRegisterResource(MethodResource, Resource):

    @use_kwargs(CommentRequestPostSchema, location=('json'))
    @marshal_with(CommentResponseSchema, code=200)
    @doc(description='Registro de Comment')
    @jwt_required()
    def post(self, **kwargs):
        comment:  CommentModel = CommentModel(**kwargs)
        comment.save()
        return make_response(comment_schema.dump(comment), 200)

    @marshal_with(CommentResponseSchema, code=200)
    @doc(description='Get tipo de analise by id')
    @use_kwargs(CommentRequestGetSchema, location=('query'))
    def get(self, **kwargs):
        comment_id = kwargs["id"]

        comment:  CommentModel = CommentModel.find_by_id(comment_id)
        if comment:
            return make_response(comment_schema.dump(comment), 200)
        return make_response({'message': 'Item not found'}, 404)

    @doc(description='Update tipo de analise by id')
    @use_kwargs(CommentRequestPutSchema, location=('json'))
    @jwt_required()
    def put(self, **kwargs):
        comment_id = kwargs["id"]
        comment:  CommentModel = CommentModel.find_by_id(comment_id)

        if comment:
            comment.update(**kwargs)
            return make_response(comment_schema.dump(comment), 200)

        return make_response({'message': 'Item not found'}, 404)

    @doc(description='Delete tipo de analise by id')
    @use_kwargs(CommentRequestDeleteSchema, location=('query'))
    @jwt_required()
    def delete(self, **kwargs):
        comment_id = kwargs["id"]
        comment:  CommentModel = CommentModel.find_by_id(comment_id)

        if comment:
            comment.delete()

        return make_response({'message': 'Item deleted'}, 200)


@doc(description='Listagem de Comment', tags=['Comment'])
class CommentListResource(MethodResource, Resource):

    @marshal_with(CommentResponseSchema, code=200)
    @doc(description='Listagem de Comment')
    def get(self, **kwargs):

        comments = CommentModel.find_all()
        if comments:
            return make_response(comment_schema.dump(comments, many=True), 200)

        return make_response({'message': 'Item not found'}, 404)
