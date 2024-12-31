from django.test import TestCase, Client
from exercises.models import Skill

class SkillsAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        # 在測試數據庫中創建一個 Skill
        self.skill = Skill.objects.create(name="Push-Up", category="Upper Body", description="Push-Up movements")


    def test_list_skills(self):
        response = self.client.get('/api/exercises/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Expected response")
        
    def test_retrieve_skill(self):
        response = self.client.get(f'/api/exercises/skills/{self.skill.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id": self.skill.id,
            "name": "Push-Up",
            "category": "Upper Body",
            "description": "Push-Up movements",
        })