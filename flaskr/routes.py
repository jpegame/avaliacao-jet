from flask_restful import Api

from flaskr.resources.health_checker import HealthCheckerResource
from flaskr.resources.token import TokenRefresherResource, TokenResource
from flaskr.resources.user import UserRegisterResource
from flaskr.resources.post import PostRegisterResource, PostListResource
from flaskr.resources.comment import CommentRegisterResource, CommentListResource
from flaskr.resources.like import LikeRegisterResource, LikeListResource


def config_app_routes(app, docs):
    api = Api(app)
    __setting_route_doc(UserRegisterResource, '/user', api, docs)
    __setting_route_doc(TokenResource, '/token', api, docs)
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api, docs)
    __setting_route_doc(HealthCheckerResource, '/health', api, docs)
    
    __setting_route_doc(PostRegisterResource, '/post', api, docs)
    __setting_route_doc(PostListResource, '/post/all', api, docs)
    __setting_route_doc(CommentRegisterResource, '/comment', api, docs)
    __setting_route_doc(CommentListResource, '/comment/all', api, docs)
    __setting_route_doc(LikeRegisterResource, '/like', api, docs)
    __setting_route_doc(LikeListResource, '/like/all', api, docs)
    return api


def __setting_route_doc(resource, route, api, docs):
    # Config routes
    api.add_resource(resource, route)
    # Add API in Swagger Documentation
    docs.register(resource)
