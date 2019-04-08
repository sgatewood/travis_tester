from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.test.utils import override_settings
from django.conf import settings

import os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumTest(LiveServerTestCase):

    print(os.listdir())

    def setUp(self):
        cap = DesiredCapabilities().FIREFOX
        # cap["marionette"] = False

        try:
            self.browser = webdriver.Firefox(executable_path="geckodriver")

            # self.browser = webdriver.Firefox()
            0/0
        except Exception as e:
            print(e)
            print(open("geckodriver.log").read())
            raise e
        super(SeleniumTest, self).setUp()

    def load(self,url):
        self.browser.get(self.live_server_url+url)

    def test_yay(self):
        self.load("/pasta")
        self.browser.quit()

    # def test_yay2(self):
    #     y = open("geckodriver.log")
    #     print("LOG:",y.read())
    #     y.close()
    #     self.load("/pasta")
