from django.test import TestCase
from exercises.models import Skill, ExerciseLevel

class SkillModelTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(name="Push-Up", category="Upper Body")

    def test_skill_creation(self):
        self.assertEqual(self.skill.name, "Push-Up")
        self.assertEqual(self.skill.category, "Upper Body")

class ExerciseLevelModelTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(name="Push-Up", category="Upper Body")
        self.exercise_level = ExerciseLevel.objects.create(skill=self.skill, level_number=1, description="Wall Push-Up")

    def test_exercise_level_creation(self):
        self.assertEqual(self.exercise_level.skill.name, "Push-Up")
        self.assertEqual(self.exercise_level.level_number, 1)
        self.assertEqual(self.exercise_level.description, "Wall Push-Up")