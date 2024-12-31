from ninja import Router
from exercises.models import Skill

router = Router()

@router.get('/list', response={200: str})
def list_skills(request):
    return "Expected response"

@router.get('/skills/{skill_id}', response={200: str})
def retrieve_skill(request, skill_id: int):
    return Skill.objects.get(id=skill_id)