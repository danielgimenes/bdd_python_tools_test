from behave import *

@given(u'main page loaded')
def given_main_page_loaded(context):
    context.browser.visit('https://google.com/')

@when(u'type "{query_string}" and press enter')
def typed_and_pressed_enter(context, query_string):
    context.browser.fill('q', query_string)
    button = context.browser.find_by_name('btnG')
    button.click()

@then(u'results page should have "{link_text}" link')
def first_link_should_be(context, link_text):
    links = context.browser.find_link_by_text(link_text)
    assert links.is_empty() is False
