import datetime
import os
import pytest
import logging

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="choose browser: chrome, firefox, yandex")
    parser.addoption("--driver_folder", default=os.path.expanduser("drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.15:8081")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    driver = None
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"seleium-tests-with-jenkins/logs/{request.node.name}.log")
    # file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    if _browser == "firefox" or _browser == "ff":
        driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox", executable_path=f"{driver_folder}{os.sep}geckodriver")
    elif _browser == "chrome":
        # driver = webdriver.Chrome(executable_path=f"{driver_folder}{os.sep}chromedriver")
        # path_to_driver_test = "/Users/anastasiiamonakhova/.jenkins/workspace/opencart-tests/seleium-tests-with-jenkins/drivers/chromedriver_correct"
        path_to_driver_test = "./seleium-tests-with-jenkins/drivers/chromedriver_correct"
        print(f"PATH TO DRIVER: {path_to_driver_test}")
        driver = webdriver.Chrome(executable_path=f"{path_to_driver_test}")
    elif _browser == "yandex":
        driver = webdriver.Chrome(executable_path=f"{driver_folder}{os.sep}yandexdriver")

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser, driver.capabilities))

    driver.maximize_window()

    driver.get(url)
    driver.url = url

    yield driver
    logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))
    driver.close()
