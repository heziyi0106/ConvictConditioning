from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

class Command(BaseCommand):
    help = _('Populate database with initial exercises and levels for Convict Conditioning')

    def handle(self, *args, **kwargs):
        from exercises.models import Skill, ExerciseLevel

        big_six = [
            {"name": _("Push-Up"), "category": _("Upper Body"), "levels": [
                _("Wall Push-Up"), _("Incline Push-Up"), _("Kneeling Push-Up"), _("Half Push-Up"), _("Full Push-Up"),
                _("Close Push-Up"), _("Uneven Push-Up"), _("1/2 One Arm Push-Up"), _("Lever Push-Up"), _("One Arm Push-Up")
            ]},
            {"name": _("Pull-Up"), "category": _("Upper Body"), "levels": [
                _("Vertical Pulls"), _("Horizontal Pulls"), _("Jackknife Pulls"), _("Half Pull-Ups"), _("Full Pull-Ups"),
                _("Close Pull-Ups"), _("Uneven Pull-Ups"), _("1/2 One Arm Pull-Up"), _("Assisted One Arm Pull-Up"), _("One Arm Pull-Up")
            ]},
            {"name": _("Squat"), "category": _("Lower Body"), "levels": [
                _("Shoulderstand Squats"), _("Jackknife Squats"), _("Supported Squats"), _("Half Squats"), _("Full Squats"),
                _("Close Squats"), _("Uneven Squats"), _("1/2 One Leg Squat"), _("Assisted One Leg Squat"), _("One Leg Squat")
            ]},
            {"name": _("Leg Raise"), "category": _("Core"), "levels": [
                _("Knee Tucks"), _("Flat Knee Raises"), _("Flat Bent Leg Raises"), _("Flat Frog Raises"), _("Flat Straight Leg Raises"),
                _("Hanging Knee Raises"), _("Hanging Bent Leg Raises"), _("Hanging Frog Raises"), _("Partial Straight Leg Raises"), _("Hanging Straight Leg Raises")
            ]},
            {"name": _("Bridge"), "category": _("Core"), "levels": [
                _("Short Bridges"), _("Straight Bridges"), _("Angled Bridges"), _("Head Bridges"), _("Half Bridges"),
                _("Full Bridges"), _("Wall Walking (Down)"), _("Wall Walking (Up)"), _("Closing Bridges"), _("Stand-to-Stand Bridges")
            ]},
            {"name": _("Handstand Push-Up"), "category": _("Upper Body"), "levels": [
                _("Wall Headstands"), _("Crow Stands"), _("Wall Handstands"), _("Half Handstand Push-Ups"), _("Handstand Push-Ups"),
                _("Close Handstand Push-Ups"), _("Uneven Handstand Push-Ups"), _("1/2 One Arm Handstand Push-Up"), _("Lever Handstand Push-Up"), _("One Arm Handstand Push-Up")
            ]},
        ]

        trifecta = [
            {"name": _("L-Sit"), "category": _("Core"), "levels": [
                _("Tuck Hold"), _("Flat Tuck Hold"), _("Flat Tuck L-Sit"), _("One Leg Flat Tuck L-Sit"), _("L-Sit")
            ]},
            {"name": _("Back Lever"), "category": _("Core"), "levels": [
                _("Tuck Back Lever"), _("Flat Tuck Back Lever"), _("One Leg Flat Tuck Back Lever"), _("Straddle Back Lever"), _("Back Lever")
            ]},
            {"name": _("Front Lever"), "category": _("Core"), "levels": [
                _("Tuck Front Lever"), _("Flat Tuck Front Lever"), _("One Leg Flat Tuck Front Lever"), _("Straddle Front Lever"), _("Front Lever")
            ]},
        ]

        for skill_data in big_six + trifecta:
            skill, created = Skill.objects.get_or_create(name=skill_data["name"], category=skill_data["category"])
            for level_number, level_name in enumerate(skill_data["levels"], start=1):
                ExerciseLevel.objects.get_or_create(skill=skill, level_number=level_number, description=level_name)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with exercises and levels.'))
