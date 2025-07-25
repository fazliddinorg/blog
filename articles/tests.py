from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Article, Comment

User = get_user_model()

class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='secret'
        )
        self.article = Article.objects.create(
            title='Test Article',
            summary='Test Summary',
            body='Test body of the article',
            author=self.user
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_article_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(),
            reverse('article_detail', args=[str(self.article.id)])
        )
