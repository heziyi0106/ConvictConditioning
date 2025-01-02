from django.db import models
from django.utils.translation import gettext_lazy as _
from django_web_convict_conditioning.common import Common
from exercises.models import Skill

class Goal(Common):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name=_("技能"))
    target_level = models.PositiveIntegerField(_("目標級別"))
    due_date = models.DateField(_("目標完成日期"), null=True, blank=True)
    is_achieved = models.BooleanField(_("是否達成"), default=False)

    class Meta:
        verbose_name = _("健身目標")
        verbose_name_plural = _("健身目標")

    def __str__(self):
        return f"{self.user.username}'s goal for {self.skill.name}"
