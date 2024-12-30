from django.test import TestCase

class BasicTestCase(TestCase):
    def test_hello_world(self):
        self.assertEqual("hello world", "hello world")