import uuid
from datetime import datetime


class CommentRepository:
    def __init__(self):
        # In-memory storage: {comment_id: comment_data}
        self._comments = {}

    def create(self, task_id: str, text: str) -> dict:
        comment_id = str(uuid.uuid4())
        comment = {
            "id": comment_id,
            "task_id": task_id,
            "text": text,
            "created_at": datetime.utcnow().isoformat()
        }
        self._comments[comment_id] = comment
        return comment

    def get_by_task(self, task_id: str) -> list:
        return [
            comment for comment in self._comments.values()
            if comment["task_id"] == task_id
        ]

    def update(self, comment_id: str, text: str) -> dict | None:
        comment = self._comments.get(comment_id)
        if not comment:
            return None

        comment["text"] = text
        return comment

    def delete(self, comment_id: str) -> bool:
        if comment_id not in self._comments:
            return False

        del self._comments[comment_id]
        return True
