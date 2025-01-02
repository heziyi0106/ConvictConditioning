from django.db import models
from django.utils.translation import gettext_lazy as _
from django_web_convict_conditioning.common import Common


class Exercise(Common):
    name = models.CharField(_("名稱"), max_length=100)  # e.g., Push-Up, Pull-Up
    description = models.TextField(_("描述"), blank=True)  # Optional description of the exercise

    class Meta:
        verbose_name = _("動作")
        verbose_name_plural = _("動作")
        
    def __str__(self):
        return self.name


class WorkoutSession(Common):
    date = models.DateField(_("日期"))  # The date of the workout
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name=_("動作"))  # Related exercise
    progression_level = models.IntegerField(_("進階級別"))  # The progression level for the exercise
    sets = models.PositiveIntegerField(_("組數"))  # Number of sets completed
    reps_per_set = models.PositiveIntegerField(_("每組次數"))  # Number of repetitions per set
    notes = models.TextField(_("備註"), blank=True)  # Optional notes
    is_completed = models.BooleanField(_("是否完成"), default=False)


    class Meta:
        verbose_name = _("訓練記錄")
        verbose_name_plural = _("訓練記錄")
        ordering = ("-date",)
        
    def __str__(self):
        return f"{self.date} - {self.exercise.name}"
