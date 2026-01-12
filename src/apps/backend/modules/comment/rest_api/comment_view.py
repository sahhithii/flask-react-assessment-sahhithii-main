from flask import request, jsonify
from modules.comment.internal.comment_service import CommentService


class CommentView:
    def __init__(self):
        self._service = CommentService()

    def create_comment(self, task_id: str):
        try:
            data = request.get_json() or {}
            text = data.get("text")

            comment = self._service.add_comment(task_id, text)
            return jsonify(comment), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_comments_for_task(self, task_id: str):
        comments = self._service.get_comments_for_task(task_id)
        return jsonify(comments), 200

    def update_comment(self, comment_id: str):
        try:
            data = request.get_json() or {}
            text = data.get("text")

            comment = self._service.update_comment(comment_id, text)
            return jsonify(comment), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_comment(self, comment_id: str):
        try:
            self._service.delete_comment(comment_id)
            return jsonify({"message": "Comment deleted"}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 404
