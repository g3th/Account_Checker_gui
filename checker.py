import threading
from services import services_elements
from streaming_services.disney import disney_checker
from streaming_services.espn import espn_checker
from graphics.title import main_title, disney_title, espn_title
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from pathlib import Path

class checker_gui():

	def __init__(self):

		self.gui = Tk()
		self.style = Style()
		self.gui.iconbitmap('@graphics/checker.xbm')
		self.style.configure('GUI_Buttons.TButton',background='goldenrod3', font=('Arial', 10))
		self.gui.configure(bg='goldenrod4')
		self.gui.resizable(False,False)
		self.gui.geometry('800x600')
		self.gui.title('Selenium Webdriver Account Checkers')
		self.titlebox= Canvas(self.gui,bg='goldenrod2',width=510,height=178)
		self.servicesbox= Canvas(self.gui,bg='goldenrod3',width=710,height=320)
		self.back_button = Button(self.gui, text = 'Back', command= self.return_to_main_page, style='GUI_Buttons.TButton')
		
	def draw_main_title(self):
	
		title=main_title()
		self.titlebox.place(x=148,y=15)
		self.titlebox.create_text(233,44,text=title[0],font=('Courier New',8),tag='top_title')
		self.titlebox.create_text(290,132,text=title[1],font=('Courier New',8),tag='bottom_title')
		self.titlebox.config(state = DISABLED)
	
	def draw_services_title(self, title,x1,y1,x2,y2):
	
		self.titlebox.delete('top_title')
		self.titlebox.delete('bottom_title')
		self.titlebox.create_text(x1,y1,text=title[0],font=('Courier New',8),tag='top_title')
		self.titlebox.create_text(x2,y2,text=title[1],font=('Courier New',8),tag='bottom_title')
	
	def create_back_button(self,xpos,ypos):

		self.back_button = Button(self.gui, text = 'Back', command= self.return_to_main_page, style='GUI_Buttons.TButton')
		self.back_button.place(x=xpos,y=ypos)
	
	def back_button_own_thread(self):
	
		threading.Thread(target=self.create_back_button,args=(363,560)).start()
	
	def services_buttons(self):

		self.services = services_elements()
		self.services.services_buttons(self.gui, 'Disney+', self.disney, 55, 360)
		self.services.services_buttons(self.gui, 'ESPN+', self.espn_plus, 160, 360)
	
	def draw_services_box(self):
		
		self.servicesbox.create_line(700,50,8,50,width=2,fill='goldenrod4')
		self.servicesbox.place(x=43,y=230)
		
	def return_to_main_page(self):
		
		self.checker.destroy_all_elements()
		self.labels()
		self.back_button.place_forget()
		self.services_buttons()
		self.titlebox.delete('top_title')
		self.titlebox.delete('bottom_title')
		self.draw_main_title()
			
	def labels(self):
		
		self.service_label = Label(self.gui, background='goldenrod3',text='Choose a Service to Check',font=('Arial', 18))
		self.service_label.place(x=48, y=238)

	def disney(self):
	
		title=disney_title()
		self.checker = disney_checker(self.gui)
		self.service_label.destroy()
		self.services.services_destroy()
		self.back_button_own_thread()
		self.draw_services_title(title,220,45,300,128)
		self.checker.split_combo_file(self.gui)
		self.checker.draw_checker_button()

	def espn_plus(self):
	
		title=espn_title()
		self.checker = espn_checker(self.gui)
		self.service_label.destroy()
		self.services.services_destroy()
		self.draw_services_title(title,280,40,300,125)
		self.back_button_own_thread()
		
	def loop(self):
	
		self.gui.mainloop()
		
if __name__ == '__main__':
	checker = checker_gui()
	checker.draw_main_title()
	checker.services_buttons()
	checker.draw_services_box()
	checker.labels()
	checker.loop()
