import threading
from services import services_elements
from streaming_services.disney import disney_checker
from streaming_services.espn import espn_checker
from graphics.title import create_app_title
from graphics.title import main_title, disney_title, espn_title
from colour_list.change_gui_colours import interactive_colour_changes
from tkinter import *
from tkinter.ttk import *
from pathlib import Path

class checker_gui():
	
	def __init__(self):
		stored_colours = []
		with open('colour_list/stored_colours','r') as stored:
			for line in stored.readlines():
				stored_colours.append(line)
			stored.close()
		print(stored_colours)			
		self.gui = Tk()
		self.style = Style()
		self.gui.iconbitmap('@graphics/checker.xbm')
		self.style.map("GUI_Buttons.TButton", foreground=[('pressed', 'WhiteSmoke'), ('active', 'WhiteSmoke')], background=[('pressed', '!disabled', 'SteelBlue4'), ('active', 'SteelBlue4')])
		self.style.configure('GUI_Buttons.TButton', foreground = 'WhiteSmoke', background = 'SteelBlue', font=('Arial', 10),height=20,width=14)
		self.gui.configure(bg='#87d7ff')
		self.gui.resizable(False, False)
		self.gui.geometry('800x600')
		self.gui.title('Selenium Webdriver Account Checkers')
		self.titlebox= create_app_title(self.gui)
		self.servicesbox= Canvas(self.gui,bg='#5fd7d7',width=710,height=320,bd=5,relief=SUNKEN)
		self.back_button = Button(self.gui, text = 'Back', command= self.return_to_main_page, style='GUI_Buttons.TButton')
		self.colour_page_back_button = Button(self.gui, text = 'Back', command= self.store_colours_and_return_to_main_page, style='GUI_Buttons.TButton')
	
	def gui_colour_change_button(self):
	
		self.gui_colour_change = Button(self.gui, text= 'Change GUI Colours', command = self.draw_gui_colour_change_page_elements)
		self.gui_colour_change.place(x=360, y=567)
		
	def draw_gui_colour_change_page_elements(self):
		self.colour_page_back_button.place(x=448,y=565)
		self.services.services_destroy()
		self.gui_colour_change.place_forget()
		self.service_label.configure(text='Pick a Colour to Change a GUI Element')
		self.change_colours = interactive_colour_changes(self.gui)
		self.change_colours.unpack_lists_for_tabs()
		change_colour_button = Button(self.gui, text = 'Change Colour', command = self.change_and_store_gui_colours)
		change_colour_button.place(x=335,y=566)

	def change_and_store_gui_colours(self):
		
		self.change_colours.change_the_colour_of_elements()
		colours = self.change_colours.change_the_colour_of_elements()[3]

		if self.change_colours.change_the_colour_of_elements()[0] == '0':

			self.background = colours[self.change_colours.change_the_colour_of_elements()[1]].strip()			
			self.gui.configure(bg=colours[self.change_colours.change_the_colour_of_elements()[1]].strip())	
		
		if self.change_colours.change_the_colour_of_elements()[0] == '1':

			self.canvas = colours[self.change_colours.change_the_colour_of_elements()[2]].strip()
			self.servicesbox.configure(bg=colours[self.change_colours.change_the_colour_of_elements()[2]].strip())

	def store_colours_and_return_to_main_page(self):

		with open('colour_list/stored_colours','a') as stored:
			stored.write('Background: {}\nCanvas: {}'.format(self.background,self.canvas))
		stored.close()
		self.change_colours.clear_all_page_elements()
		self.labels()
		self.back_button.place_forget()
		self.services_buttons()
		self.draw_gui_titles()
		self.change_colours.clear_all_page_elements()
	def draw_gui_titles(self):
	
		title=main_title()
		self.titlebox.create_title(233,18,290,100,title)
	
	def create_back_button(self,xpos,ypos):

		self.back_button = Button(self.gui, text = 'Back', command= self.return_to_main_page, style='GUI_Buttons.TButton')
		self.back_button.place(x=xpos,y=ypos)
	
	def back_button_own_thread(self):
	
		threading.Thread(target=self.create_back_button,args=(358, 560)).start()
	
	def services_buttons(self):

		self.services = services_elements()
		self.services.services_buttons(self.gui, 'Disney+', self.disney, 115, 315)
		self.services.services_buttons(self.gui, 'Paramount+', self.espn_plus, 314, 315)
		self.services.services_buttons(self.gui, 'ESPN+', self.espn_plus, 513, 315)
		self.services.services_buttons(self.gui, 'Dazn', self.espn_plus, 115, 380)
		self.services.services_buttons(self.gui, 'HBO', self.espn_plus, 314, 380)
		self.services.services_buttons(self.gui, 'Fubo', self.espn_plus, 513, 380)
		self.services.services_buttons(self.gui, 'Peacock', self.espn_plus, 115, 442)
	
	def draw_services_box(self):
		
		self.servicesbox.create_line(700,50,8,50,width=2,fill='#005f87')
		self.servicesbox.place(x=43,y=230)
		
	def return_to_main_page(self):
		
		self.checker.destroy_all_elements()
		self.labels()
		self.back_button.place_forget()
		self.services_buttons()
		self.draw_gui_titles()
			
	def labels(self):
		
		self.service_label = Label(self.gui, background='#5fd7d7',text='Choose a Service to Check a Combo-list:',font=('Arial', 13))
		self.service_label.place(x=52, y=245)

	def disney(self):
		
		title = disney_title()
		self.titlebox.create_title(220,45,300,128,title)
		self.checker = disney_checker(self.gui)
		self.service_label.destroy()
		self.services.services_destroy()
		self.back_button_own_thread()
		self.checker.split_combo_file(self.gui)
		self.checker.draw_checker_button()

	def espn_plus(self):
	
		title = espn_title()
		self.checker = espn_checker(self.gui)
		self.service_label.destroy()
		self.services.services_destroy()
		self.back_button_own_thread()
		
	def loop(self):
	
		self.gui.mainloop()
		
if __name__ == '__main__':
	checker = checker_gui()
	checker.gui_colour_change_button()
	checker.draw_gui_titles()
	checker.services_buttons()
	checker.draw_services_box()
	checker.labels()
	checker.loop()
