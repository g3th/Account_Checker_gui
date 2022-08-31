import tkinter
from disney import disney_checker
from tkinter import *
from tkinter import ttk

class checker_gui():
	def __init__(self):
		self.gui = Tk()
		self.gui.resizable(False,False)
		self.gui.geometry('300x600')
		self.gui.title('Selenium Account Checkers')
		
	def labels(self):
		self.service_label = Label(self.gui, text='Pick a Service',font=('Arial',24,'underline'))
		self.service_label.place(x=45, y=20)
		
	def services_buttons(self):
		self.disney_checks = disney_checker(self.gui)
		self.disney = Button(self.gui, text = 'Disney+', font=('Arial',12), command = self.disney_checks.check_the_accounts)
		self.disney.place(x=35, y=80)

	def loop(self):
		self.gui.mainloop()
		
checker = checker_gui()
checker.services_buttons()
checker.labels()
checker.loop()
