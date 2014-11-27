from lettuce import world, steps
import unittest


# @step(u'''main page loaded''')
# def given_main_page_loaded(step):
#     world.browser.visit('https://google.com/')
#
#
# @step(u'''type "([^"]*)" and press enter''')
# def typed_and_pressed_enter(step, query_string):
#         world.browser.fill('q', query_string)
#         button = world.browser.find_by_name('btnG')
#         button.click()
#
#
# @step(u'''results page should have "([^"]*)" link''')
# def first_link_should_be(step, link_text):
#     links = world.browser.find_link_by_text(link_text)
#     assert links.is_empty() is False
#
#

@steps
class GoogleSimpleQueryTests(unittest.TestCase):

    exclude = [ 'browser' ]

    def __init__(self, environment):
        self.environment = environment

    def get_browser(self):
        return self.environment.browser

    def given_main_page_loaded(self, step):
        u'''main page loaded'''
        self.get_browser().visit('https://google.com/')

    def typed_and_pressed_enter(self, step, query_string):
        u'''type "([^"]*)" and press enter'''
        self.get_browser().fill('q', query_string)
        button = self.get_browser().find_by_name('btnG')
        button.click()

    def first_link_should_be(self, step, link_text):
        u'''results page should have "([^"]*)" link'''
        links = self.get_browser().find_link_by_text(link_text)
        self.assertFalse(links.is_empty())
