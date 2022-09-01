import tkinter
import subprocess
from header import title_text
from disney import disney_checker
from tkinter import *
from tkinter import ttk

class checker_gui():

	def __init__(self):

		self.gui = Tk()
		self.gui.resizable(False,False)
		self.gui.geometry('800x600')
		self.gui.title('Selenium Account Checkers')
		#self.ascii_title= Text(self.gui, bg='black',fg='aquamarine',bd = 5,width=56, height=11)
		self.box= Canvas(self.gui,bg='black',width=458,height=150)
		self.title = Label(self.gui, text ='''   ▄▄▄·  ▄▄·  ▄▄·       ▄• ▄▌ ▐ ▄ ▄▄▄▄▄
 ▐█ ▀█ ▐█ ▌▪▐█ ▌▪▪     █▪██▌•█▌▐█•██      
▄█▀▀█ ██ ▄▄██ ▄▄ ▄█▀▄ █▌▐█▌▐█▐▐▌ ▐█.▪    
▐█ ▪▐▌▐███▌▐███▌▐█▌.▐▌▐█▄█▌██▐█▌ ▐█▌·    
     ▀  ▀ ·▀▀▀ ·▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪ ▀▀▀ ''',justify=LEFT)  
		self.disney_plus = disney_checker(self.gui)

	def draw_title(self):
		self.box.place(x=20,y=20)
		self.title.grid(row=4,column=0)
	def labels(self):
		
		self.service_label = Label(self.gui, text='Pick A Service',font=('Arial', 15,'underline'))
		self.service_label.place(x=38, y=228)
		
	def services_buttons(self):
		
		self.disney = Button(self.gui, text = 'Disney+', font=('Arial', 12), command = self.disney)
		self.disney.place(x=35, y=270)

	def disney(self):
		self.service_label.destroy()
		self.disney.destroy()
		checker = disney_checker(self.gui)
		checker.split_combo_file(self.gui)
		checker.draw_checker_button(self.gui)
		checker.draw_the_infobox()

	def loop(self):
		self.gui.mainloop()
		
checker = checker_gui()
checker.draw_title()
checker.services_buttons()
checker.labels()
checker.loop()
