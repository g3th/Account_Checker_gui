from tkinter import *

class create_app_title:
	
	def __init__(self, root):
	
		self.titlebox= Canvas(root,width=510,height=178)
	
	def create_title(self, x1,y1,x2,y2,header,top_colour_list,bottom_colour_list):
	
		self.titlebox.delete('top')
		self.titlebox.delete('bottom')
		title = header
		self.titlebox.place(x=148,y=15)
		try:
			for i in range(len(top_colour_list)):
				self.titlebox.create_text(x1,y1,text = title[0][i],fill = top_colour_list[i],font=('Courier New',8),tag = 'top')
				y1=y1+12
		except IndexError:
			pass
		try:
			for i in range(len(bottom_colour_list)):
				self.titlebox.create_text(x2,y2,text = title[1][i],fill = bottom_colour_list[i],font=('Courier New',8),tag = 'bottom')
				y2=y2+12
		except IndexError:
			pass
		
	def configure_canvas_colour(self, colour):
		self.titlebox.configure(bg=colour)

def main_title():

	account= ['    █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗','   ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝','███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║','██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║','██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║','╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝']
	checker=['██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗','██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗','██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝','██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗','╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║',' ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝','	 			github.com/g3th']
	return account, checker

def disney_title():

	colour_top=['indigo', 'blueviolet', 'purple1', 'purple2', 'purple3', 'purple4']
	colour_bottom=['lightskyblue','lightskyblue1','lightskyblue2','lightskyblue3','lightskyblue4','lightskyblue3','lightskyblue2']
	disney=['██████╗ ██╗███████╗███╗   ██╗███████╗██╗   ██╗','██╔══██╗██║██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝','██║  ██║██║███████╗██╔██╗ ██║█████╗   ╚████╔╝ ','██║  ██║██║╚════██║██║╚██╗██║██╔══╝    ╚██╔╝  ','██████╔╝██║███████║██║ ╚████║███████╗   ██║   ','╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝']
	plus=['██████╗ ██╗     ██╗   ██╗███████╗','██╔══██╗██║     ██║   ██║██╔════╝','██████╔╝██║     ██║   ██║███████╗','██╔═══╝ ██║     ██║   ██║╚════██║','██║     ███████╗╚██████╔╝███████║','╚═╝     ╚══════╝ ╚═════╝ ╚══════╝']
	return disney, plus

def espn_title():

	espn='''███████╗███████╗██████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╗  ███████╗██████╔╝██╔██╗ ██║
██╔══╝  ╚════██║██╔═══╝ ██║╚██╗██║
███████╗███████║██║     ██║ ╚████║
╚══════╝╚══════╝╚═╝     ╚═╝  ╚═══╝'''
	plus='''██████╗ ██╗     ██╗   ██╗███████╗
██╔══██╗██║     ██║   ██║██╔════╝
██████╔╝██║     ██║   ██║███████╗
██╔═══╝ ██║     ██║   ██║╚════██║
██║     ███████╗╚██████╔╝███████║
╚═╝     ╚══════╝ ╚═════╝ ╚══════╝'''
	return espn, plus
	
