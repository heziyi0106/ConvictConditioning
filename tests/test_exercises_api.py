from django.test import TestCase, Client
from exercises.models import Skill
from django.contrib.auth.models import User

class SkillsAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.skill = Skill.objects.create(name="Push-Up", description="Push-Up movements", user=self.user)

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