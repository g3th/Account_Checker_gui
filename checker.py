import threading
from services import services_elements
from streaming_services.disney import disney_checker
from streaming_services.espn import espn_checker
from graphics.title import create_app_title
from graphics.title import main_title, disney_title, espn_title
from tkinter import *
from tkinter.ttk import *
from pathlib import Path

class checker_gui():

	def __init__(self):

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
	checker.draw_gui_titles()
	checker.services_buttons()
	checker.draw_services_box()
	checker.labels()
	checker.loop()
