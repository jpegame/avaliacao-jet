from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flaskr.redis import jwt_required
from flask_apispec.views import MethodResource
from flask_restful import Resource
from flaskr.models.post import PostModel
from flaskr.schemas.post import (PostResponseSchema,
                                     PostRequestPostSchema,
                                     PostRequestGetSchema,
                                     PostRequestDeleteSchema,
                                     PostRequestPutSchema,
                                     post_schema)


@doc(description='Registro de Post', tags=['Post'])
class PostRegisterResource(MethodResource, Resource):

    @use_kwargs(PostRequestPostSchema, location=('json'))
    @marshal_with(PostResponseSchema, code=200)
    @doc(description='Registro de Post')
    @jwt_required()
    def post(self, **kwargs):
        post: PostModel = PostModel(**kwargs)
        post.save()
        return make_response(post_schema.dump(post), 200)

    @marshal_with(PostResponseSchema, code=200)
    @doc(description='Get tipo de analise by id')
    @use_kwargs(PostRequestGetSchema, location=('query'))
    def get(self, **kwargs):
        post_id = kwargs["id"]

        post: PostModel = PostModel.find_by_id(post_id)
        if post:
            return make_response(post_schema.dump(post), 200)
        return make_response({'message': 'Item not found'}, 404)

    @doc(description='Update tipo de analise by id')
    @use_kwargs(PostRequestPutSchema, location=('json'))
    @jwt_required()
    def put(self, **kwargs):
        post_id = kwargs["id"]
        post: PostModel = PostModel.find_by_id(post_id)

        if post:
            post.update(**kwargs)
            return make_response(post_schema.dump(post), 200)

        return make_response({'message': 'Item not found'}, 404)

    @doc(description='Delete tipo de analise by id')
    @use_kwargs(PostRequestDeleteSchema, location=('query'))
    @jwt_required()
    def delete(self, **kwargs):
        post_id = kwargs["id"]
        post: PostModel = PostModel.find_by_id(post_id)

        if post:
            post.delete()

        return make_response({'message': 'Item deleted'}, 200)


@doc(description='Listagem de Post', tags=['Post'])
class PostListResource(MethodResource, Resource):

    @marshal_with(PostResponseSchema, code=200)
    @doc(description='Listagem de Post')
    def get(self, **kwargs):

        posts = PostModel.find_all()
        if posts:
            return make_response(post_schema.dump(posts, many=True), 200)

        return make_response({'message': 'Item not found'}, 404)
