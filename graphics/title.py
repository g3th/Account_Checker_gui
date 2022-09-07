from tkinter import *

class create_app_title:
	
	def __init__(self, root):
	
		self.titlebox= Canvas(root,bg='WhiteSmoke',width=510,height=178)
	
	def create_title(self, x1,y1,x2,y2,header):
	
		self.titlebox.delete('top')
		self.titlebox.delete('bottom')
		title = header
		self.titlebox.place(x=148,y=15)
		for i in range(len(title[0])):
			self.titlebox.create_text(x1,y1,text = title[0][i],fill = title[2][i],font=('Courier New',8),tag = 'top')
			y1=y1+12
		for i in range(len(title[1])):
			self.titlebox.create_text(x2,y2,text = title[1][i],fill = title[3][i],font=('Courier New',8),tag = 'bottom')
			y2=y2+12

def main_title():

	colour_top=['#000000', 'blueviolet', 'purple1', 'purple2', 'purple3', 'purple4']
	colour_bottom=['lightskyblue','lightskyblue1','lightskyblue2','lightskyblue3','lightskyblue4','lightskyblue3','lightskyblue2']
	account= ['    █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗','   ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝','███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║','██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║','██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║','╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝']
	checker=['██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗','██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗','██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝','██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗','╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║',' ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝','	 			github.com/g3th']
	return account, checker, colour_top, colour_bottom

def disney_title():

	colour_top=['indigo', 'blueviolet', 'purple1', 'purple2', 'purple3', 'purple4']
	colour_bottom=['lightskyblue','lightskyblue1','lightskyblue2','lightskyblue3','lightskyblue4','lightskyblue3','lightskyblue2']
	disney=['██████╗ ██╗███████╗███╗   ██╗███████╗██╗   ██╗','██╔══██╗██║██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝','██║  ██║██║███████╗██╔██╗ ██║█████╗   ╚████╔╝ ','██║  ██║██║╚════██║██║╚██╗██║██╔══╝    ╚██╔╝  ','██████╔╝██║███████║██║ ╚████║███████╗   ██║   ','╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝']
	plus=['██████╗ ██╗     ██╗   ██╗███████╗','██╔══██╗██║     ██║   ██║██╔════╝','██████╔╝██║     ██║   ██║███████╗','██╔═══╝ ██║     ██║   ██║╚════██║','██║     ███████╗╚██████╔╝███████║','╚═╝     ╚══════╝ ╚═════╝ ╚══════╝']
	return disney, plus, colour_top, colour_bottom

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
	
