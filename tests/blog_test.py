import unittest
from app.models import Blog, User
from app import db

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_charles = User(username='janeffer',password='123456789',email='test@test.com')
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_charles.id)