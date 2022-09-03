from tkinter import *

class services_elements:

	def __init__(self):
		
		self

	def services_buttons(self, root, service_name, call, horizontal_placement, vertical_placement):
		self.service_type = Button(root, text = service_name, command = call)
		self.service_type.place(x= horizontal_placement, y= vertical_placement)
	
	def services_destroy(self):
		self.service_type.destroy()

#55 360
		
