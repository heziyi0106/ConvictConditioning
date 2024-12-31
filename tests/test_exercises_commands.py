from django.core.management import call_command
from django.test import TestCase
from exercises.models import Skill, ExerciseLevel
from django.utils.translation import gettext as _

class PopulateExercisesCommandTest(TestCase):
    def setUp(self):
        # 清空數據庫中的 Skill 和 ExerciseLevel 表
        Skill.objects.all().delete()
        ExerciseLevel.objects.all().delete()

    def test_populate_exercises(self):
        # 執行 populate_exercises 命令
        call_command('populate_exercises')

        # 檢查 Skill 和 ExerciseLevel 表是否已填充數據
        self.assertTrue(Skill.objects.exists())
        self.assertTrue(ExerciseLevel.objects.exists())

        # 檢查特定的 Skill 和 ExerciseLevel 是否存在
        push_up = Skill.objects.get(name=_("Push-Up"))
        self.assertIsNotNone(push_up)
        self.assertEqual(push_up.category, _("Upper Body"))

        wall_push_up = ExerciseLevel.objects.get(skill=push_up, level_number=1)
        self.assertIsNotNone(wall_push_up)
        self.assertEqual(wall_push_up.description, _("Wall Push-Up"))

    def test_idempotency(self):
        # 執行 populate_exercises 命令兩次，檢查數據是否重複
        call_command('populate_exercises')
        call_command('populate_exercises')

        # 檢查 Skill 和 ExerciseLevel 表中的記錄數量是否正確
        self.assertEqual(Skill.objects.count(), 9)  # 假設有 6 個 Skill
        self.assertEqual(ExerciseLevel.objects.count(), 75)  # 假設每個 Skill 有 10 個 Level