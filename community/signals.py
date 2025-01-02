from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from community.models import Post, Like, Comment, Notification

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        content_object = instance.content_object
        if isinstance(content_object, Post):
            message = f"Your post '{content_object.title}' was liked by {instance.user.username}."
            recipient = content_object.user
        elif isinstance(content_object, Comment):
            message = f"Your comment on post '{content_object.post.title}' was liked by {instance.user.username}."
            recipient = content_object.user
        else:
            return

        Notification.objects.create(
            user=recipient,
            content_type=ContentType.objects.get_for_model(Like),
            object_id=instance.id,
            content_object=instance,
            message=message
        )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        message = f"Your post '{post.title}' received a new comment by {instance.user.username}."
        recipient = post.user

        Notification.objects.create(
            user=recipient,
            content_type=ContentType.objects.get_for_model(Comment),
            object_id=instance.id,
            content_object=instance,
            message=message
        )
        
        # 發送通知給被 @ 的用戶
        mentioned_users = instance.get_mentioned_users() # 若沒有進行@，將回傳空列表
        for user in mentioned_users:
            message = f"You were mentioned in a comment by {instance.user.username} on post '{post.title}'."
            Notification.objects.create(
                user=user,
                content_type=ContentType.objects.get_for_model(Comment),
                object_id=instance.id,
                content_object=instance,
                message=message
            )