from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from community.models import Post, Comment, Like, Notification

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, content="This is a test post")

    def test_create(self):
        self.assertEqual(self.post.user.username, 'testuser')
        self.assertEqual(self.post.content, "This is a test post")
        self.assertIsNotNone(self.post.created_at)
        
    def test_read(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.user.username, 'testuser')
        self.assertEqual(post.content, "This is a test post")
        self.assertIsNotNone(post.created_at)
    
    def test_update(self):
        self.post.content = "This is an updated test post"
        self.post.save()
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.content, "This is an updated test post")
        
    def test_delete(self):
        post_id = self.post.id
        self.post.delete()
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=post_id)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, content="This is a test post")
        self.comment = Comment.objects.create(post=self.post, user=self.user, content="This is a test comment")

    def test_create(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.user.username, 'testuser')
        self.assertEqual(self.comment.content, "This is a test comment")
        self.assertIsNotNone(self.comment.created_at)
        
    def test_read(self):
        comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.user.username, 'testuser')
        self.assertEqual(comment.content, "This is a test comment")
        self.assertIsNotNone(comment.created_at)
        
    def test_update(self):
        self.comment.content = "This is an updated test comment"
        self.comment.save()
        comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(comment.content, "This is an updated test comment")
        
    def test_delete(self):
        comment_id = self.comment.id
        self.comment.delete()
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(id=comment_id)

class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, content="This is a test post")
        self.comment = Comment.objects.create(post=self.post, user=self.user, content="This is a test comment")
        post_content_type = ContentType.objects.get_for_model(Post)
        comment_content_type = ContentType.objects.get_for_model(Comment)
        self.like_post = Like.objects.create(content_type=post_content_type, object_id=self.post.id, user=self.user)
        self.like_comment = Like.objects.create(content_type=comment_content_type, object_id=self.comment.id, user=self.user)

    def test_create_like_post(self):
        self.assertEqual(self.like_post.content_object, self.post)
        self.assertEqual(self.like_post.user.username, 'testuser')
        self.assertIsNotNone(self.like_post.created_at)

    def test_create_like_comment(self):
        self.assertEqual(self.like_comment.content_object, self.comment)
        self.assertEqual(self.like_comment.user.username, 'testuser')
        self.assertIsNotNone(self.like_comment.created_at)

    def test_read_like_post(self):
        like = Like.objects.get(id=self.like_post.id)
        self.assertEqual(like.content_object, self.post)
        self.assertEqual(like.user.username, 'testuser')
        self.assertIsNotNone(like.created_at)

    def test_read_like_comment(self):
        like = Like.objects.get(id=self.like_comment.id)
        self.assertEqual(like.content_object, self.comment)
        self.assertEqual(like.user.username, 'testuser')
        self.assertIsNotNone(like.created_at)

    def test_delete_like_post(self):
        like_id = self.like_post.id
        self.like_post.delete()
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like_id)

    def test_delete_like_comment(self):
        like_id = self.like_comment.id
        self.like_comment.delete()
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like_id)

class NotificationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.other_user = User.objects.create_user(username='otheruser', password='12345')
        self.third_user = User.objects.create_user(username='thirduser', password='12345')
        self.post = Post.objects.create(user=self.user, content="This is a test post")
        self.comment = Comment.objects.create(post=self.post, user=self.user, content="This is a test comment")

    def test_like_post_notification(self):
        post_content_type = ContentType.objects.get_for_model(Post)
        like = Like.objects.create(content_type=post_content_type, object_id=self.post.id, user=self.other_user)
        notification = Notification.objects.get(content_type=ContentType.objects.get_for_model(Like), object_id=like.id)
        self.assertEqual(notification.user, self.user)
        self.assertIn("Your post", notification.message)

    def test_like_comment_notification(self):
        comment_content_type = ContentType.objects.get_for_model(Comment)
        like = Like.objects.create(content_type=comment_content_type, object_id=self.comment.id, user=self.other_user)
        notification = Notification.objects.get(content_type=ContentType.objects.get_for_model(Like), object_id=like.id)
        self.assertEqual(notification.user, self.user)
        self.assertIn("Your comment", notification.message)

    def test_comment_post_notification(self):
        new_comment = Comment.objects.create(post=self.post, user=self.other_user, content="This is another test comment")
        notification = Notification.objects.get(content_type=ContentType.objects.get_for_model(Comment), object_id=new_comment.id)
        self.assertEqual(notification.user, self.post.user)
        self.assertIn("Your post", notification.message)

    def test_mention_user_notification(self):
        new_comment = Comment.objects.create(post=self.post, user=self.other_user, content="This is another test comment @thirduser")
        notification = Notification.objects.get(content_type=ContentType.objects.get_for_model(Comment), object_id=new_comment.id, user=self.third_user)
        self.assertEqual(notification.user, self.third_user)
        self.assertIn("You were mentioned", notification.message)