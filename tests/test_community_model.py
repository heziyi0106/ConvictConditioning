from django.contrib.auth.models import User
from django.test import TestCase
from community.models import Post, Comment, Like

class CommunityModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, content="This is a test post")
        self.comment = Comment.objects.create(post=self.post, user=self.user, content="This is a test comment")
        self.like = Like.objects.create(post=self.post, user=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.user.username, 'testuser')
        self.assertEqual(self.post.content, "This is a test post")
        self.assertIsNotNone(self.post.created_at)

    def test_comment_creation(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.user.username, 'testuser')
        self.assertEqual(self.comment.content, "This is a test comment")
        self.assertIsNotNone(self.comment.created_at)

    def test_like_creation(self):
        self.assertEqual(self.like.post, self.post)
        self.assertEqual(self.like.user.username, 'testuser')
        self.assertIsNotNone(self.like.created_at)