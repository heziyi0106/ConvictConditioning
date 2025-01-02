from django.db import models
from django.utils.translation import gettext_lazy as _
from django_web_convict_conditioning.common import Common
from tinymce.models import HTMLField


class Post(Common):
    title = models.CharField(_("標題"), max_length=100)  # The title of the post
    content = HTMLField(_("內容"))  # The content of the post

    class Meta:
        verbose_name = _("貼文")
        verbose_name_plural = _("貼文")
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"


class Comment(Common):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("貼文"))  # The related post
    content = HTMLField(_("內容"))  # The content of the comment    

    class Meta:
        verbose_name = _("評論")
        verbose_name_plural = _("評論")
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


class Like(Common):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("貼文"))  # The related post

    class Meta:
        verbose_name = _("讚")
        verbose_name_plural = _("讚")
        ordering = ["created_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_user_post_like"),
        ]
        
    def __str__(self):
        return f"Like by {self.user.username} on {self.post.id}"
