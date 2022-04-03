from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile, Post


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='elly')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='', bio=' testing profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)
    
class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='elly', user=User(username='bora'))
        self.profile_test.save()

        self.image_test = Post(image='', name='test', caption='default test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)