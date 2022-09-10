from tkinter import *
from tkinter import ttk


class interactive_colour_changes:
	
	def __init__(self,root):
		
		self.tabs = ttk.Notebook(root)
		self.colour_names = []
		self.background_colour = ttk.Frame(self.tabs)
		self.canvas_colour = ttk.Frame(self.tabs)
		self.title_canvas_colour = ttk.Frame(self.tabs)
		self.tabs.add(self.background_colour, text = 'Background Colour')
		self.tabs.add(self.canvas_colour, text = 'Canvas Colour')
		self.tabs.add(self.title_canvas_colour , text = 'Title Canvas Colour')
		self.tabs.pack(expand = True)
		self.tabs.place(x=50,y=283)

	def colours_list(self):
		self.colour_names = []
		with open('colour_list/colourslist','r') as colours:
			for line in colours.readlines():
				self.colour_names.append(line.split('\t')[1].replace('(SYSTEM)',''))
		self.colour_names = sorted(self.colour_names)
		self.colour_names_for_list = StringVar(value = self.colour_names)
		
	def unpack_lists_for_tabs(self):
		self.colours_list()
		self.background_colour_change = Listbox (self.background_colour, listvariable = self.colour_names_for_list, height = 13)	
		self.background_colour_change.grid ( column = 3, row = 3 , sticky = 'n')
		self.background_colour_change.pack(expand = True)
		self.canvas_colour_change = Listbox (self.canvas_colour, listvariable = self.colour_names_for_list, height = 13)
		self.canvas_colour_change.grid ( column = 3, row = 3 , sticky = 'n')
		self.canvas_colour_change.pack(expand = True)
		self.title_canvas_colour = Listbox (self.title_canvas_colour, listvariable = self.colour_names_for_list, height = 13)
		self.title_canvas_colour.grid ( column = 3, row = 3 , sticky = 'n')
		self.title_canvas_colour.pack(expand = True)
		
	def change_the_colour_of_elements(self):
		colour = self.colour_names
		background_colour=''
		canvas_colour=''
		title_canvas_colour=''
		self.current_selection = self.tabs.index('current')
		current_selection = self.current_selection
		if self.current_selection == 0:
			background_colour = int(self.background_colour_change.curselection()[0])
		if self.current_selection == 1:
			canvas_colour = int(self.canvas_colour_change.curselection()[0])
		if self.current_selection == 2:
			title_canvas_colour = int(self.title_canvas_colour.curselection()[0])
		return str(current_selection), background_colour, canvas_colour, title_canvas_colour, colour
	
	def clear_all_page_elements(self):
		
		self.tabs.place_forget()

			
	
