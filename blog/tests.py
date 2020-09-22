
# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='majd',
            email='majd@gmail.com',
            password='password'
        )

        self.post = Post.objects.create(
            title='test_post',
            body='this post for test reason ',
            auther=self.user
        )


    def test_string_representation(self):
        post = Post(title='post')
        self.assertEqual(str(post), post.title)


    def test_trip_content(self):
        self.assertEqual(f'{self.post.title}', 'test_post')
        self.assertEqual(f'{self.post.auther}', 'majd')
        self.assertEqual(f'{self.post.body}', 'this post for test reason ')







    def test_blog_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_post_details_view(self):
        response = self.client.get(reverse('post_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args='1'), {
            'title': 'test_test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_test')

    def test_post_delet_view(self):
        response = self.client.get(reverse('post_delet',args='1'))
        self.assertEqual(response.status_code, 200)
