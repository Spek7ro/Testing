import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Android',
#     appPackage='com.android.settings',
#     appActivity='.Settings',
#     language='en',
#     locale='US'
# )



capabilities = {
    "platformName":"Android",
    "appium:automationName":"uiautomator2",
    "appium:deviceName":"Android",
    # "appium:appPackage":"com.android.settings",
    # "appium:appPackage":"com.google.android.apps.nexuslauncher",
    # "appium:appActivity":".Settings",
    # "appium:app":"/Users/alexmau/Documents/UAZ/materias/enero2023/frameworks/frameworks/flutter/hola_mundo2/build/app/outputs/flutter-apk/app-debug.apk",
    "language":"en",
    "locale":"US"
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Phone').click()
        time.sleep(3)
        
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='key pad').click()
        time.sleep(3)
        
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='4,GHI').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='9,WXYZ').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='2,ABC').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1,').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='0').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='3,DEF').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1,').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='6,MNO').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='5,JKL').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='5,JKL').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='dial').click()
        
        # username = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[1]')
        # password = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[2]')
        # username.send_keys('hola')
        # password.send_keys('mundo')
        # time.sleep(3)
        
        # self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Ingresar').click()
        
        # time.sleep(3)
        
        # mensaje = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Materias')
        # print(mensaje)
        # self.assertTrue(mensaje)
        # time.sleep(10)