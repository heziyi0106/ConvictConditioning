from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Exercise, WorkoutSession

@admin.register(Exercise)
class ExerciseAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(ModelAdmin):
    list_display = ('date', 'exercise', 'progression_level', 'sets', 'reps_per_set', 'notes')
    search_fields = ('exercise__name',)
    list_filter = ('date', 'exercise')
