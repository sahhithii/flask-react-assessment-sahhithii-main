from modules.comment.rest_api.comment_router import CommentRouter


class CommentRestApiServer:
    def __init__(self, app):
        self._app = app
        self._register_routes()

    def _register_routes(self):
        router = CommentRouter()
        self._app.register_blueprint(router.blueprint)
