from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_jwt_extended import jwt_required
from flask_apispec.views import MethodResource
from flask_restful import Resource
from flaskr.models.like import LikeModel
from flaskr.schemas.like import (LikeResponseSchema,
                                     LikeRequestPostSchema,
                                     LikeRequestGetSchema,
                                     LikeRequestDeleteSchema,
                                     LikeRequestPutSchema,
                                     like_schema)


@doc(description='Registro de Like', tags=['Like'])
class LikeRegisterResource(MethodResource, Resource):

    @use_kwargs(LikeRequestPostSchema, location=('json'))
    @marshal_with(LikeResponseSchema, code=200)
    @doc(description='Registro de Like')
    @jwt_required()
    def post(self, **kwargs):
        like:  LikeModel = LikeModel(**kwargs)
        like.save()
        return make_response(like_schema.dump(like), 200)

    @marshal_with(LikeResponseSchema, code=200)
    @doc(description='Get tipo de analise by id')
    @use_kwargs(LikeRequestGetSchema, location=('query'))
    def get(self, **kwargs):
        like_id = kwargs["id"]

        like:  LikeModel = LikeModel.find_by_id(like_id)
        if like:
            return make_response(like_schema.dump(like), 200)
        return make_response({'message': 'Item not found'}, 404)

    @doc(description='Update tipo de analise by id')
    @use_kwargs(LikeRequestPutSchema, location=('json'))
    @jwt_required()
    def put(self, **kwargs):
        like_id = kwargs["id"]
        like:  LikeModel = LikeModel.find_by_id(like_id)

        if like:
            like.update(**kwargs)
            return make_response(like_schema.dump(like), 200)

        return make_response({'message': 'Item not found'}, 404)

    @doc(description='Delete tipo de analise by id')
    @use_kwargs(LikeRequestDeleteSchema, location=('query'))
    @jwt_required()
    def delete(self, **kwargs):
        like_id = kwargs["id"]
        like:  LikeModel = LikeModel.find_by_id(like_id)

        if like:
            like.delete()

        return make_response({'message': 'Item deleted'}, 200)


@doc(description='Listagem de Like', tags=['Like'])
class LikeListResource(MethodResource, Resource):

    @marshal_with(LikeResponseSchema, code=200)
    @doc(description='Listagem de Like')
    def get(self, **kwargs):

        likes = LikeModel.find_all()
        if likes:
            return make_response(like_schema.dump(likes, many=True), 200)

        return make_response({'message': 'Item not found'}, 404)
