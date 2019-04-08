from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.test.utils import override_settings
from django.conf import settings

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumTest(LiveServerTestCase):



    def setUp(self):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        browser = webdriver.Firefox(capabilities=cap, executable_path="geckodriver")

        self.browser = webdriver.Firefox()
        super(SeleniumTest, self).setUp()

    def load(self,url):
        self.browser.get(self.live_server_url+url)

    def test_yay(self):
        self.load("/pasta")
