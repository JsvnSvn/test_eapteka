import os
import allure
import pytest
from selenium import webdriver
from loguru import logger


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--browser_version', action='store', default='90.0', help='Choose version')
    parser.addoption('--size', action='store', default=None, help='Choose size')
    parser.addoption('--mode', action='store', default='desktop', help='Choose size')
    parser.addoption('--env', action='store', default='local', help='Choose env')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    version = request.config.getoption('browser_version')
    screen_resolution = request.config.getoption('size')
    mode = request.config.getoption('mode')
    env = request.config.getoption('env')
    browser = None
    capabilities = {
        "browserName": browser_name,
        "version": version,
        "enableVNC": True,
        "enableVideo": False,
        "screenResolution": screen_resolution
    }

    if env == 'local':
        executor = 'http://127.0.0.1:4444/wd/hub'
    else:
        executor = ''

    logger.info(f"\nstart {browser_name} browser for test..")

    if mode == 'desktop':
        browser = webdriver.Remote(command_executor=executor, desired_capabilities=capabilities)
        browser.set_window_size(1920, 1080)
    elif mode == 'mobile':
        options = webdriver.ChromeOptions()
        user_agent: str = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1'
        options.add_argument(f'user-agent={user_agent}')
        browser = webdriver.Remote(command_executor=executor, desired_capabilities=capabilities, options=options)
        browser.set_window_size(414, 736)
    yield browser

    logger.info("\nquit browser..")
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
