from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='some user',
            email='some@some.com',
            password='secret',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='some title',
            body='some body',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'some user')
        self.assertEqual(self.post.title, 'some title')
        self.assertEqual(self.post.body, 'some body')
        self.assertEqual(str(self.post), 'some title')