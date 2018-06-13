from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Leard TDD" into a text box
        inputbox.send_keys('Learn TDD')

        # Whe he hits enter, the page updates, and now the page lists
        # "1: Learn TDD" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Learn TDD' for row in rows),
            "New to-do item did not appear in the table"
        )

        # There is still a text box inviting him to add another item.
        # He enters "Use TDD to build killer web app"
        self.fail('Finish the test!')

        # The page updates again, and now both items show on his list

        # Vance wonders whether the site will remember his list. The site
        # generated a unique URL for him and there is some explanatory text
        # to that effect.

        # He visits that URL - his to-do list is still there.

if __name__ == '__main__':
    unittest.main()
