import os
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.window_width = int(os.getenv('selene.window_width', 1920))
    browser.config.window_height = int(os.getenv('selene.window_height', 1080))
