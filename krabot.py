"""Importing third parties and in_built modules"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from time import sleep
from datetime import datetime
import sys
import json

class KraBot:
	"""Main KraBot """

	def __init__(self, data):
		"""Parameter initilization"""

		self.driver = webdriver.Firefox()
		self.email = data["email"]
		self.password = data["password"]
		self.pin = data["Pin"]

	def login_kra(self):
		"""This program logins into your Kra account"""

		self.driver.get("https://itax.kra.go.ke")
		sleep(3)
		login_id = self.driver.find_element_by_name("logid")
		login_id.clear()
		login_id.send_keys(self.pin)
		login_id.send_keys(Keys.RETURN)
		sleep(2)
		self.driver.execute_script("javascript:CheckPIN();")
		sleep(1)
		login_password = self.driver.find_element_by_xpath("//input[contains(@type='password')]")
		login_password.clear()
		login_password.send_keys(self.password)
		self.driver.find_elements_by_xpath("//input[contains(@name = 'captchaText')]")
		sleep(1)
		self.driver.execute_script("javascript:submitForm1();")
if __name__ == "__main__":

	with open("config.json") as f:
		data = json.load(f)

	bot = KraBot(data)
	bot.login_kra()
	