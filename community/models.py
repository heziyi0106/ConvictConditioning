from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # The user who created the post
    content = models.TextField()  # The content of the post
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the post was created

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # The related post
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # The user who made the comment
    content = models.TextField()  # The content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the comment

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # The related post
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # The user who liked the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the like

    def __str__(self):
        return f"{self.user.username} liked {self.post.id}"
