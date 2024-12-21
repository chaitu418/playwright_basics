
import pytest

from playwright.sync_api import Page

import time

def test_playwright_basics(playwright):


    print("this is base line")
    browser = playwright.chromium.launch(headless=False)
    """
    context helps in adding all the cookies ,sessions,passwords and all
    """
    context= browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwright_shortcut(page:Page):
    #page.
    page.goto("https://rahulshettyacademy.com")


def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(10)
    page.get_by_role("button",name="Sign In").click()
    
