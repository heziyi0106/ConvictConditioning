from django.test import TestCase
from workouts.models import Exercise, WorkoutSession

class WorkoutsTestCase(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(name="Push-Up", description="A basic push-up exercise")
        self.workout_session = WorkoutSession.objects.create(
            date="2024-12-30",
            exercise=self.exercise,
            progression_level=1,
            sets=3,
            reps_per_set=15,
            notes="Felt good"
        )

    def test_workout_session_creation(self):
        self.assertEqual(self.workout_session.date, "2024-12-30")
        self.assertEqual(self.workout_session.exercise.name, "Push-Up")
        self.assertEqual(self.workout_session.progression_level, 1)
        self.assertEqual(self.workout_session.sets, 3)
        self.assertEqual(self.workout_session.reps_per_set, 15)
        self.assertEqual(self.workout_session.notes, "Felt good")