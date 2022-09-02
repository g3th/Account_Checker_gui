import tkinter
import subprocess
from disney import disney_checker
from graphics.title import main_title, disney_title
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
		title=main_title()
		self.titlebox.place(x=40,y=15)
		self.titlebox.pack()
		self.titlebox.create_text(300,40,text=title[0],font=('Courier New',8),tag='account')
		self.titlebox.create_text(400,125,text=title[1],font=('Courier New',8),tag='checker')
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
		title=disney_title()
		self.titlebox.delete('account')
		self.titlebox.delete('checker')
		self.service_label.destroy()
		self.titlebox.create_text(300,40,text=title[0],font=('Courier New',8),tag='disney')
		self.titlebox.create_text(400,125,text=title[1],font=('Courier New',8),tag='plus')
		self.disney.destroy()
		checker = disney_checker(self.gui)
		checker.split_combo_file(self.gui)
		checker.draw_checker_button(self.gui)

	def loop(self):
		self.gui.mainloop()
		
if __name__ == '__main__':
	checker = checker_gui()
	checker.draw_title()
	checker.draw_services_box()
	checker.services_buttons()
	checker.labels()
	checker.loop()
