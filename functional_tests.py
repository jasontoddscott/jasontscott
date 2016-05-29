from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_blog_and_retrieve_it_later(self):
        self.browser.implicitly_wait(9)
        self.browser.get('http://127.0.0.1:8000')

        self.assertIn('Blog', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
