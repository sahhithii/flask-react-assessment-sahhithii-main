from flask import Blueprint
from modules.comment.rest_api.comment_view import CommentView


class CommentRouter:
    def __init__(self):
        self.blueprint = Blueprint("comment", __name__)
        self._view = CommentView()
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule(
            "/tasks/<task_id>/comments",
            view_func=self._view.create_comment,
            methods=["POST"],
        )

        self.blueprint.add_url_rule(
            "/tasks/<task_id>/comments",
            view_func=self._view.get_comments_for_task,
            methods=["GET"],
        )

        self.blueprint.add_url_rule(
            "/comments/<comment_id>",
            view_func=self._view.update_comment,
            methods=["PUT"],
        )

        self.blueprint.add_url_rule(
            "/comments/<comment_id>",
            view_func=self._view.delete_comment,
            methods=["DELETE"],
        )
