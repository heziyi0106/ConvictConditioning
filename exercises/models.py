from django.db import models
from django.utils.translation import gettext_lazy as _

class Skill(models.Model):
    name = models.CharField(_("名稱"), max_length=100)  # e.g., Push-Up, Pull-Up
    category = models.CharField(_("類別"), max_length=50)  # e.g., Upper Body, Core
    description = models.TextField(_("描述"), blank=True)  # Optional description of the skill

    def __str__(self):
        return self.name

class ExerciseLevel(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name=_("技能"))  # Related skill
    level_number = models.PositiveIntegerField(_("級別"))  # e.g., 1 for basic push-up, 10 for one-arm push-up
    description = models.TextField(_("描述"), blank=True)  # Description for the level

    def __str__(self):
        return f"{self.skill.name} - Level {self.level_number}"