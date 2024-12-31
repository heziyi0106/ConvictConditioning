from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("使用者")
    )  # The user who created the post
    content = models.TextField(_("內容"))  # The content of the post
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("建立時間")
    )  # Timestamp when the post was created

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("貼文"))  # The related post
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("使用者")
    )  # The user who made the comment
    content = models.TextField(_("內容"))  # The content of the comment
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("建立時間"))  # Timestamp for the comment
    
    class Meta:
        verbose_name = _("評論")
        verbose_name_plural = _("評論")
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("貼文"))  # The related post
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("使用者")
    )  # The user who liked the post
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("建立時間"))  # Timestamp for the like

    class Meta:
        verbose_name = _("讚")
        verbose_name_plural = _("讚")
        ordering = ["created_at"]
        
    def __str__(self):
        return f"Like by {self.user.username} on {self.post.id}"
