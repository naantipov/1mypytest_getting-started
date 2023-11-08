from selene.support.shared import browser
from selene import be, have
import pytest



@pytest.fixture
def browser_configs():
    browser.config.window_width = 600
    browser.config.window_height = 800
    yield
    browser.clear_session_storage()
    browser.save_screenshot()
    browser.close()
def test_google_find_selene(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_find_fdghsjkdhsfk(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fdghsjkdhsfk').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу fdghsjkdhsfk ничего не найдено'))








