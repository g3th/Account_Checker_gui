import os
import tkinter
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from pathlib import Path

class split_combos():

	def __init__(self,root,service,background_colour):

		self.clean_list=[]
		self.split_combos_button = Button(root, text = 'Split Combos', command= partial(self.combo_splitter, service), style='GUI_Buttons.TButton')
		self.split_combos_button.place(x=480, y=560)
		self.split_text_completed= Label(root, background=background_colour,font=('Arial',12))
	
	def destroy_split_button(self):
		self.split_combos_button.destroy()

	def combo_splitter(self, service):
		directory = str(Path(__file__).parent)
		combo_list_name = service
		try:
		
			with open(combo_list_name, 'r') as combo:
				for line in combo.readlines():
						self.clean_list.append(line.split(' | ')[0])			
			parsed_list_name = service+'_'
			with open(parsed_list_name,'a') as clean:
				for line in self.clean_list:
					clean.write(line+'\n')
			os.remove(service)
			os.rename(parsed_list_name, service)		
			self.destroy_split_button()
			self.split_text_completed['text']='Done Splitting - Total Combos {}'.format(str(len(self.clean_list)))
			self.split_text_completed.place(x=65,y=247)
		except FileNotFoundError:
			self.split_text_completed['text']='No Combo-list Found.'
			self.split_text_completed.place(x=65,y=247)
			
	def destroy_info_label(self):
		self.split_text_completed.destroy()
