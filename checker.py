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
import os

class checker_gui():
	
	def __init__(self):
	
		stored_colours = []
		background_colour = open('colour_list/background','r')
		canvas_colour = open('colour_list/canvas','r')
		title_canvas_colour = open('colour_list/title_canvas','r')
		self.gui = Tk()
		self.style = Style()
		self.gui.iconbitmap('@graphics/checker.xbm')
		self.style.map("GUI_Buttons.TButton", foreground=[('pressed', 'WhiteSmoke'), ('active', 'WhiteSmoke')], background=[('pressed', '!disabled', 'SteelBlue4'), ('active', 'SteelBlue4')])
		self.style.configure('GUI_Buttons.TButton', foreground = 'WhiteSmoke', background = 'SteelBlue', font=('Arial', 10),height=20,width=14)
		self.gui.configure(bg=background_colour.readline().strip())
		self.gui.resizable(False, False)
		self.gui.geometry('800x600')
		self.gui.title('Selenium Webdriver Account Checkers')
		self.titlebox= create_app_title(self.gui)
		self.servicesbox= Canvas(self.gui,bg=canvas_colour.readline().strip(),width=710,height=320,bd=5,relief=SUNKEN)
		self.titlebox.configure_canvas_colour(title_canvas_colour.readline().strip())
		self.back_button = Button(self.gui, text = 'Back', command= self.return_to_main_page, style='GUI_Buttons.TButton')
		self.colour_page_back_button = Button(self.gui, text = 'Back', command= self.store_colours_and_return_to_main_page, style='GUI_Buttons.TButton')
	
	def gui_colour_change_button(self):
	
		self.gui_colour_change = Button(self.gui, text= 'Change Colours', command = self.draw_gui_colour_change_page_elements, style='GUI_Buttons.TButton')
		self.gui_colour_change.place(x=355, y=567)
		
	def draw_gui_colour_change_page_elements(self):
	
		self.colour_page_back_button.place(x=422,y=566)
		self.services.services_destroy()
		self.gui_colour_change.place_forget()
		self.service_label.configure(text='Pick a Colour to Change a GUI Element')
		self.change_colours = interactive_colour_changes(self.gui)
		self.change_colours.unpack_lists_for_tabs()
		self.change_colour_button = Button(self.gui, text = 'Confirm Change', command = self.change_and_store_gui_colours, style='GUI_Buttons.TButton')
		self.change_colour_button.place(x=310,y=566)
		
	def nothing_selected_error(self):
	
		self.nothing_selected_popup = Toplevel(self.gui)
		self.nothing_selected_popup.iconbitmap('@graphics/checker.xbm')
		self.nothing_selected_popup.geometry("160x110")
		self.nothing_selected_popup.resizable(False,False)
		self.nothing_selected_popup.title("Index Error")
		Label(self.nothing_selected_popup, font=("Arial", 12),text='Please Select a \nColour',justify=CENTER).pack()
		ok_button = Button(self.nothing_selected_popup, text = 'Will Do Chief', command = self.destroy_error_window, style='GUI_Buttons.TButton')
		ok_button.place(x=25,y=55)
		
	def destroy_error_window(self):
	
		self.nothing_selected_popup.destroy()
		

	def change_and_store_gui_colours(self):
		try:
			self.change_colours.change_the_colour_of_elements()
			colours = self.change_colours.change_the_colour_of_elements()[4]

			if self.change_colours.change_the_colour_of_elements()[0] == '0':
				self.background = colours[self.change_colours.change_the_colour_of_elements()[1]].strip()			
				self.gui.configure(bg=colours[self.change_colours.change_the_colour_of_elements()[1]].strip())	
			
			if self.change_colours.change_the_colour_of_elements()[0] == '1':
				self.canvas = colours[self.change_colours.change_the_colour_of_elements()[2]].strip()
				self.servicesbox.configure(bg=colours[self.change_colours.change_the_colour_of_elements()[2]].strip())
				
			if self.change_colours.change_the_colour_of_elements()[0] == '2':
				self.title_canvas = colours[self.change_colours.change_the_colour_of_elements()[3]].strip()
				self.titlebox.configure_canvas_colour(colours[self.change_colours.change_the_colour_of_elements()[3]].strip())
				
		except IndexError:
			self.nothing_selected_error()

	def store_colours_and_return_to_main_page(self):
	
		try:	
			try:
				if self.background:
					with open('colour_list/background','w') as background:
						background.write('{}\n'.format(self.background))
			except AttributeError:
				pass
			try:
				if self.canvas:
					with open('colour_list/canvas','w') as canvas:
						canvas.write('{}\n'.format(self.canvas))
			except AttributeError:
				pass
			try:
				if self.title_canvas:
					with open('colour_list/title_canvas','w') as title_canvas:
						title_canvas.write('{}\n'.format(self.title_canvas))
			except AttributeError:
				pass
			self.return_to_main_page_from_change_colour_page()
		
		except AttributeError as e:
	
			if str(e) == "'checker_gui' object has no attribute 'canvas'":
				with open('colour_list/background','w') as background:
					background.write('{}\n'.format(self.background))
				background.close()
			if str(e) == "'checker_gui' object has no attribute 'background'":
				with open('colour_list/canvas','w') as canvas:
					canvas.write('{}\n'.format(self.canvas))
				canvas.close()
			self.return_to_main_page_from_change_colour_page()
	
	def return_to_main_page_from_change_colour_page(self):
	
		self.change_colours.clear_all_page_elements()
		self.change_colour_button.place_forget()
		self.colour_page_back_button.place_forget()
		self.labels()	
		self.services_buttons()
		self.draw_gui_titles()
		self.gui_colour_change_button()
			
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
		self.gui_colour_change_button()	
	def labels(self):
		canvas_colour = open('colour_list/canvas','r')
		self.service_label = Label(self.gui, background=canvas_colour.readline().strip(),text='Choose a Service to Check a Combo-list:',font=('Arial', 13))
		self.service_label.place(x=52, y=245)

	def disney(self):
		
		title = disney_title()
		self.titlebox.create_title(220,45,300,128,title)
		self.checker = disney_checker(self.gui)
		self.service_label.destroy()
		self.gui_colour_change.destroy()
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
