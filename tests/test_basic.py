from django.test import SimpleTestCase
from django.conf import settings


class SettingsTest(SimpleTestCase):
    def test_debug_is_false_in_production(self):
        self.assertFalse(settings.DEBUG)
