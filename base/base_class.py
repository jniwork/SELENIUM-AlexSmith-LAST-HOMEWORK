from datetime import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url : {get_url}")
        return get_url

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.strftime(datetime.now(), '%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(
            'D:\\PythonProject1\\PythonProject\\PythonProject\\UpStore24\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good URL")
