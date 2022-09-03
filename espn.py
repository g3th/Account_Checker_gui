import time
import os
import requests
import tkinter
from functools import partial
from split_combos import split_combos
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from bs4 import BeautifulSoup as soup
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, InvalidSessionIdException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path

class espn_checker():

	def __init__(self, root):
	
		self.infobox = Text(root, bg='goldenrod3',font=('Arial',11),height = 360, width=460)
		self.file_directory = str(Path(__file__).parent)+''
		self.page = ''
		self.users = []
		self.passwords = []
		self.Two_Factor = False
		self.browser_options = Options()
		self.browser_options.add_argument = ('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')		
		self.browser_options.headless = True
		self.start_checker = Button(root, text = 'Start Checker',command = 'None', style='GUI_Buttons.TButton')
		
	def split_combo_file(self,root):
	
		self.split_combos = split_combos(root)
	
	def draw_checker_button(self,root):
			
		self.start_checker.place(x=328,y=560)
			
	def draw_the_infobox(self):
	
		self.infobox.place(x=58,y=288,width=681,height=250)
		
	def split_username_and_password(self):
	
		os.makedirs('accounts',exist_ok=True)
		with open(self.file_directory, 'r') as disney:
			for line in disney.readlines():
					self.users.append(line.split(':')[0].strip())
					self.passwords.append(line.split(':')[1].strip())
						
	def destroy_all_elements(self):
	
		self.start_checker.destroy()
		self.infobox.destroy()

