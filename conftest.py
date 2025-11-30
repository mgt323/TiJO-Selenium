import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#BROWSERS = ["firefox", "edge", "opera"]
BROWSERS = ["firefox"]

@pytest.fixture(params=BROWSERS, scope="function")
def driver(request):
    browser = request.param
    driver = None

    print(f"\nRunning test on: {browser}")

    if browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)


    elif browser == "opera":
        options = webdriver.ChromeOptions()

        path_to_opera_exe = r"C:\Users\makst\AppData\Local\Programs\Opera GX\124.0.5705.38\opera.exe"
        options.binary_location = path_to_opera_exe

        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")

        path_to_operadriver = r"C:\Users\makst\Documents\PycharmProjects\TiJO-Selenium\operadriver.exe"

        service = ChromeService(executable_path=path_to_operadriver)
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()