from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Vance heard about a new online to-do app.
        # He goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Leard TDD" into a text box

        # Whe he hits enter, the page updates, and now the page lists
        # "1: Learn TDD" as an item in a to-do list

        # There is still a text box inviting him to add another item.
        # He enters "Use TDD to build killer web app"

        # The page updates again, and now both items show on his list

        # Vance wonders whether the site will remember his list. The site
        # generated a unique URL for him and there is some explanatory text
        # to that effect.

        # He visits that URL - his to-do list is still there.

if __name__ == '__main__':
    unittest.main()
