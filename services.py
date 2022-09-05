from tkinter.ttk import *

class services_elements:

	def __init__(self):
		self.style = Style()
		self.style.configure('Services_Buttons.TButton',background='goldenrod2', font=('Arial', 10),height=20,width=20)
		self.service_type_list = []

	def services_buttons(self, root, service_name, call, horizontal_placement, vertical_placement):
		
		self.service_type = Button(root, text = service_name, command = call, style='Services_Buttons.TButton')
		self.service_type.place(x= horizontal_placement, y= vertical_placement)
		self.service_type_list.append(self.service_type)
		
	def services_destroy(self):
		for item in self.service_type_list:
			item.destroy()

#55 360
		
