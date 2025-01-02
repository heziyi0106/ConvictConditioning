import re
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_web_convict_conditioning.common import Common
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Post(Common):
    title = models.CharField(_("標題"), max_length=100)
    content = models.TextField(_("內容"))
    likes = GenericRelation('Like', related_query_name='post_likes')
    notifications = GenericRelation('Notification', related_query_name='post_notifications')

    class Meta:
        verbose_name = _("貼文")
        verbose_name_plural = _("貼文")
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

class Comment(Common):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("貼文"))
    content = models.TextField(_("內容"))
    likes = GenericRelation('Like', related_query_name='comment_likes')
    notifications = GenericRelation('Notification', related_query_name='comment_notifications')

    def get_mentioned_users(self):
        # 假設用戶名不包含空格，並且以 @ 開頭
        mentioned_usernames = re.findall(r'@(\w+)', self.content)
        return User.objects.filter(username__in=mentioned_usernames)

class Like(Common):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _("讚")
        verbose_name_plural = _("讚")
        ordering = ["created_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "content_type", "object_id"], name="unique_user_content_object_like"),
        ]
        
    def __str__(self):
        return f"Like by {self.user.username} on {self.content_object}"

class Notification(Common):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"