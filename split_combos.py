import os
import tkinter
from tkinter import *
from tkinter import ttk
from pathlib import Path

def combo_splitter(service,root):
	split_text = Label(root, text='Splitting Combos')
	split_text.place(x=50,y=60)
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
	split_text['text']='Done Splitting'
