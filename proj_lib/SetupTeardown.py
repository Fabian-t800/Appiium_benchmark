import psutil
import os
from appium import webdriver


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
def connect_to_application(app_name):
    """
    :param: app_name: Either the name of the application such as "Notepad", "Notepad.exe", or the entire path leading to the application
    :return: Connection to the Desktop App via WinAppDriver. WinAppDriver (essentially a listener) must be executed prior to test suite execution.
    """
    desired_caps = {}
    desired_caps["app"] = str(app_name)
    desired_caps["automationName"] = "winappdriver"
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)
    driver.implicitly_wait(2)
    return driver


class SetupTeardown:

    def setup_suite(self):
        os.startfile('WinAppDriver.exe')

    def teardown_suite(self):
        try:
            for process in (process for process in psutil.process_iter() if process.name() == "Calculator.exe"):
                process.kill()
        except Exception:
            pass
        try:
            for process in (process for process in psutil.process_iter() if process.name() == "WinAppDriver.exe"):
                process.kill()
        except Exception:
            pass


if __name__ == "__main__":
    SetupTeardown().setup()