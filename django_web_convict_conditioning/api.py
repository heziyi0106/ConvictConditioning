from ninja import NinjaAPI
from django_web_convict_conditioning import settings
api = NinjaAPI()

api = NinjaAPI(docs_url='/docs' if settings.DEBUG else None, urls_namespace='api')
api.add_router("/community", 'community.api.router', tags=["community"])    # You can add a router as an object
api.add_router("/exercises", 'exercises.api.router', tags=["exercises"])  #   or by Python path
api.add_router("/workouts", 'workouts.api.router', tags=["workouts"])