import os
import tkinter
from functools import partial
from tkinter import *
from tkinter import ttk
from pathlib import Path

class split_combos():

	def __init__(self, root):
		self.split_combos_button = Button(root, text = 'Split Combos', font=('Arial', 12), command= partial(self.combo_splitter,'disney',root))
		self.split_combos_button.place(x=188, y=115)

	def combo_splitter(self,service,root):		
		directory = str(Path(__file__).parent)
		combo_list_name = service
		clean_list=[]
		with open(combo_list_name, 'r') as combo:
			for line in combo.readlines():
					clean_list.append(line.split(' | ')[0])			
		parsed_list_name = service+'_'
		with open(parsed_list_name,'a') as clean:
			for line in clean_list:
				clean.write(line+'\n')
		os.remove(service)
		os.rename(parsed_list_name, service)
		self.split_combos_button.destroy()
		split_text_completed= Label(root, text='Done Splitting',font=('Arial',14))
		split_text_number_of_combos= Label(root, text='Total Number of Combos {}'.format(str(len(clean_list))), font=('Arial',14))
		split_text_completed.place(x=195,y=85)
		split_text_number_of_combos.place(x=120,y=115)
		
