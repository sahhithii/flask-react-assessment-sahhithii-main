from modules.comment.internal.store.comment_repository import CommentRepository


class CommentService:
    def __init__(self):
        self._repository = CommentRepository()

    def add_comment(self, task_id: str, text: str) -> dict:
        if not text or not text.strip():
            raise ValueError("Comment text cannot be empty")

        return self._repository.create(task_id=task_id, text=text)

    def get_comments_for_task(self, task_id: str) -> list:
        return self._repository.get_by_task(task_id)

    def update_comment(self, comment_id: str, text: str) -> dict:
        if not text or not text.strip():
            raise ValueError("Comment text cannot be empty")

        updated = self._repository.update(comment_id, text)
        if not updated:
            raise ValueError("Comment not found")

        return updated

    def delete_comment(self, comment_id: str) -> None:
        deleted = self._repository.delete(comment_id)
        if not deleted:
            raise ValueError("Comment not found")
