from django.db import models
from django.contrib.auth.models import User

class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, verbose_name="使用者"
    )

    class Meta:
        abstract = True
