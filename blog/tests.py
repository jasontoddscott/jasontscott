from django.core.urlresolvers import resolve
from django.test import TestCase
from blog.views import home_page


class BlogTest(TestCase):

    def test_can_get_blog(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
