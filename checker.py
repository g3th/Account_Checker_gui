import tkinter
import subprocess
from disney import disney_checker
from tkinter import *
from tkinter import ttk

class checker_gui():

	def __init__(self):

		self.gui = Tk()
		self.gui.configure(bg='goldenrod4')
		self.gui.resizable(False,False)
		self.gui.geometry('800x600')
		self.gui.title('Selenium Account Checkers')
		self.titlebox= Canvas(self.gui,bg='goldenrod2',width=710,height=178)
		self.servicesbox= Canvas(self.gui,bg='goldenrod3',width=710,height=320)
		self.disney_plus = disney_checker(self.gui)

	def draw_title(self):
		self.titlebox.place(x=40,y=15)
		self.titlebox.pack()
		self.titlebox.create_text(300,40,text=r''' █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝''',font=('Courier New',8))
		self.titlebox.create_text(400,125,text=r''' ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 			github.com/g3th''',font=('Courier New',8))
		self.titlebox.config(state = DISABLED)
	
	def draw_services_box(self):
	
		self.servicesbox.create_line(700,50,8,50,width=2,fill='goldenrod4')
		self.servicesbox.place(x=43,y=230)
 
	def labels(self):
		
		self.service_label = Label(self.gui, bg='goldenrod3',text='Choose a Service to Check',font=('Arial', 18))
		self.service_label.place(x=48, y=238)
		
	def services_buttons(self):
		
		self.disney = Button(self.gui, text = 'Disney+', font=('Arial', 12), command = self.disney)
		self.disney.place(x=55, y=320)

	def disney(self):
		self.service_label.destroy()
		self.disney.destroy()
		checker = disney_checker(self.gui)
		checker.split_combo_file(self.gui)
		checker.draw_checker_button(self.gui)
		checker.draw_the_infobox()

	def loop(self):
		self.gui.mainloop()
		
if __name__ == '__main__':
	checker = checker_gui()
	checker.draw_title()
	checker.draw_services_box()
	checker.services_buttons()
	checker.labels()
	checker.loop()
