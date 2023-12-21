import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.savvy.security/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Savvy"))


def test_terms_of_use_link(page: Page):
    page.goto("https://www.savvy.security/")

    # click Reject All
    # page.get_by_role("dialog", name="Reject All").click()
    page.get_by_role("button", name="Reject All").click()

    # Click the Terms of Use link.
    page.get_by_role("link", name="Terms of Use").click()

    # Expects page to have a heading with the name Terms of Use.
    expect(page.get_by_role("heading", name="Terms of Use")).to_be_visible()
