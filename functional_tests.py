from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self): # like begin of thing
        # set up my browser and determine it
        self.browser = webdriver.Firefox()

    def tearDown(self):  # like end of thing
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): # any method start with test_ is a test method
        # new cool app
        # check home page
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':  # just run from file
    unittest.main(warnings='ignore')  #


