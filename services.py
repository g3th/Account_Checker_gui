from tkinter import *

class services_elements:

	def __init__(self):
		
		self.service_type_list = []

	def services_buttons(self, root, service_name, call, horizontal_placement, vertical_placement):
		self.service_type = Button(root, text = service_name, command = call)
		self.service_type.place(x= horizontal_placement, y= vertical_placement)
		self.service_type_list.append(self.service_type)
		
	def services_destroy(self):
		for item in self.service_type_list:
			item.destroy()

#55 360
		
