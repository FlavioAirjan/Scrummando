from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
from subprocess import *
import sys
import random
import string
import time

class TestFunctional(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.close()

  def test_website_on(self):
    driver = self.driver
    driver.get("http://192.241.184.37:6543")
    assert "Scrummando" in driver.title
    print "Website on OK"

class TestLogin(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.close()

  def test_website_on(self):
    driver = self.driver
    driver.get("http://192.241.184.37:6543")
    login_name = driver.find_element_by_name("login_username")
    login_name.send_keys("matheus")
    login_pass = driver.find_element_by_name("login_password")
    login_pass.send_keys("matheus")
    login_btn = driver.find_element_by_id("login_btn")
    login_btn.click()
    driver.implicitly_wait(2)
    username = driver.find_element_by_class_name("username")
    assert username.text == "matheus"
    print "Login OK"

class TestRegister(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.close()

  def test_website_on(self):
    driver = self.driver
    driver.get("http://192.241.184.37:6543")
    register_name = driver.find_element_by_name("username")
    
    novo_btn = driver.find_element_by_id("novo_btn")
    novo_btn.click()
    driver.implicitly_wait(2)
    generated_login_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    register_name.send_keys(generated_login_name)
    register_pass = driver.find_element_by_name("password")
    register_pass.send_keys(generated_login_name)
    register_btn = driver.find_element_by_id("register_btn")
    register_btn.click()
    time.sleep(1)
    msg = driver.find_element_by_id("login_status")
    driver.implicitly_wait(2)
    assert "registrado com sucesso" in msg.text
    print "Register OK"


if __name__ == '__main__':
    unittest.main()

