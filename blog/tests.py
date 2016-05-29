from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from blog.views import home_page


class BlogTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Blog</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
