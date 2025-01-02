from django.test import TestCase
from django.contrib.auth.models import User
from exercises.models import Skill, ExerciseLevel

class SkillModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.skill = Skill.objects.create(name="Push-Up", category="Upper Body", user=self.user)

    def test_skill_creation(self):
        self.assertEqual(self.skill.name, "Push-Up")

class ExerciseLevelModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.exercise_level = ExerciseLevel.objects.create(level="Beginner", description="Beginner level", user=self.user)

    def test_exercise_level_creation(self):
        self.assertEqual(self.exercise_level.level, "Beginner")