from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
from subprocess import *
import sys

class TestFunctional(unittest.TestCase):
  def setUp(self):
	self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.close()

  def test_website_on(self):
  	driver = self.driver
  	driver.get("http://0.0.0.0:6543")
	assert "Scrummando" in driver.title
	print "Website on OK"

if __name__ == '__main__':
    unittest.main()

