# blog/tests.py
from django.test import TestCase
from .models import Post

class PostModelTestCase(TestCase):
    def test_create_post(self):
        post = Post.objects.create(title="Test Title", body="Test Content")
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.title, "Test Title")

from django.urls import reverse

class PostListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('frontpage')
        Post.objects.create(title="Test Title", slug='1', intro='Test case practice', body="Test Content")

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/frontpage.html')
        self.assertContains(response, "Test Title")