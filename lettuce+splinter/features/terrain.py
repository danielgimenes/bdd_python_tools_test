from lettuce import *
from splinter import Browser
from google_test_steps import GoogleSimpleQueryTests


@before.all
def set_up():
    world.browser = Browser()


@after.all
def destroy(total):
    world.browser.quit()

GoogleSimpleQueryTests(world)
