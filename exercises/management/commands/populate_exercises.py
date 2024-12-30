from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate database with initial exercises and levels for Convict Conditioning'

    def handle(self, *args, **kwargs):
        from exercises.models import Skill, ExerciseLevel

        big_six = [
            {"name": "Push-Up", "category": "Upper Body", "levels": [
                "Wall Push-Up", "Incline Push-Up", "Kneeling Push-Up", "Half Push-Up", "Full Push-Up",
                "Close Push-Up", "Uneven Push-Up", "1/2 One Arm Push-Up", "Lever Push-Up", "One Arm Push-Up"
            ]},
            {"name": "Pull-Up", "category": "Upper Body", "levels": [
                "Vertical Pulls", "Horizontal Pulls", "Jackknife Pulls", "Half Pull-Ups", "Full Pull-Ups",
                "Close Pull-Ups", "Uneven Pull-Ups", "1/2 One Arm Pull-Up", "Assisted One Arm Pull-Up", "One Arm Pull-Up"
            ]},
            {"name": "Squat", "category": "Lower Body", "levels": [
                "Shoulderstand Squats", "Jackknife Squats", "Supported Squats", "Half Squats", "Full Squats",
                "Close Squats", "Uneven Squats", "1/2 One Leg Squat", "Assisted One Leg Squat", "One Leg Squat"
            ]},
            {"name": "Leg Raise", "category": "Core", "levels": [
                "Knee Tucks", "Flat Knee Raises", "Flat Bent Leg Raises", "Flat Frog Raises", "Flat Straight Leg Raises",
                "Hanging Knee Raises", "Hanging Bent Leg Raises", "Hanging Frog Raises", "Partial Straight Leg Raises", "Hanging Straight Leg Raises"
            ]},
            {"name": "Bridge", "category": "Core", "levels": [
                "Short Bridges", "Straight Bridges", "Angled Bridges", "Head Bridges", "Half Bridges",
                "Full Bridges", "Wall Walking (Down)", "Wall Walking (Up)", "Closing Bridges", "Stand-to-Stand Bridges"
            ]},
            {"name": "Handstand Push-Up", "category": "Upper Body", "levels": [
                "Wall Headstands", "Crow Stands", "Wall Handstands", "Half Handstand Push-Ups", "Handstand Push-Ups",
                "Close Handstand Push-Ups", "Uneven Handstand Push-Ups", "1/2 One Arm Handstand Push-Up", "Lever Handstand Push-Up", "One Arm Handstand Push-Up"
            ]},
        ]

        trifecta = [
            {"name": "L-Sit", "category": "Core", "levels": [
                "Short Sit", "Parallel L-Sit", "Advanced L-Sit", "V-Sit"
            ]},
            {"name": "Bridge Hold", "category": "Spinal", "levels": [
                "Short Bridge Hold", "Straight Bridge Hold", "Full Bridge Hold"
            ]},
            {"name": "Twist Hold", "category": "Rotational", "levels": [
                "Beginner Twist", "Intermediate Twist", "Advanced Twist"
            ]},
        ]

        # Populate Big Six
        for skill_data in big_six:
            skill, created = Skill.objects.get_or_create(name=skill_data["name"], category=skill_data["category"])
            for i, level in enumerate(skill_data["levels"], start=1):
                ExerciseLevel.objects.get_or_create(skill=skill, level_number=i, description=level)

        # Populate Trifecta
        for skill_data in trifecta:
            skill, created = Skill.objects.get_or_create(name=skill_data["name"], category=skill_data["category"])
            for i, level in enumerate(skill_data["levels"], start=1):
                ExerciseLevel.objects.get_or_create(skill=skill, level_number=i, description=level)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with exercises and levels.'))
