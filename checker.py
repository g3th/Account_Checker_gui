import threading
from services import services_elements
from streaming_services.disney import disney_checker
from streaming_services.espn import espn_checker
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
		self.gui.configure(bg='skyblue4')
		self.gui.resizable(False, False)
		self.gui.geometry('800x600')
		self.gui.title('Selenium Webdriver Account Checkers')
		self.titlebox= Canvas(self.gui,bg='skyblue2',width=510,height=178)
		self.servicesbox= Canvas(self.gui,bg='skyblue3',width=710,height=320)
		self.back_button = Button(self.gui, text = 'Back', command= self.return_to_main_page, style='GUI_Buttons.TButton')
	
	def create_main_title(self,x1,y1,titletext,colour):

		self.titlebox.create_text(x1,y1,text=titletext,fill=colour,font=('Courier New',8),tag='top_title')
		self.titlebox.create_text(x1,y1,text=titletext,fill=colour,font=('Courier New',8),tag='bottom_title')

	def colourize_main_title(self):

		x1=233;y1=18;x2=290;y2=108
		colour=['indigo', 'blueviolet', 'purple1', 'purple2', 'purple3', 'purple4', 'mediumpurple', 'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4']
		title=main_title()
		self.titlebox.place(x=148,y=15)
		for i in range(len(title[0])):
			self.create_main_title(x1,y1,title[0][i]+'\n',colour[i])
			self.create_main_title(x2,y2,title[1][i]+'\n',colour[i])
			y1=y1+12
			y2=y2+12
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
	
		threading.Thread(target=self.create_back_button,args=(358, 560)).start()
	
	def services_buttons(self):

		self.services = services_elements()
		self.services.services_buttons(self.gui, 'Disney+', self.disney, 115, 315)
		self.services.services_buttons(self.gui, 'ESPN+', self.espn_plus, 314, 315)
		self.services.services_buttons(self.gui, 'Paramount+', self.espn_plus, 513, 315)
		self.services.services_buttons(self.gui, 'Dazn', self.espn_plus, 115, 380)
		self.services.services_buttons(self.gui, 'HBO', self.espn_plus, 314, 380)
		self.services.services_buttons(self.gui, 'Fubo', self.espn_plus, 513, 380)
		self.services.services_buttons(self.gui, 'Peacock', self.espn_plus, 115, 442)
	
	def draw_services_box(self):
		
		self.servicesbox.create_line(700,50,8,50,width=2,fill='skyblue4')
		self.servicesbox.place(x=43,y=230)
		
	def return_to_main_page(self):
		
		self.checker.destroy_all_elements()
		self.labels()
		self.back_button.place_forget()
		self.services_buttons()
		self.titlebox.delete('top_title')
		self.titlebox.delete('bottom_title')
		self.colourize_main_title()
			
	def labels(self):
		
		self.service_label = Label(self.gui, background='skyblue3',text='Choose a Service to Check a Combo-list:',font=('Arial', 13))
		self.service_label.place(x=52, y=245)

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
	checker.colourize_main_title()
	checker.services_buttons()
	checker.draw_services_box()
	checker.labels()
	checker.loop()
