hex_colour_list=[]
colour_names = []
x_term = []
with open('colourslist','r') as hexs:
	for line in hexs.readlines():
		hex_colour_list.append(line.split('#')[1].split('\t')[0])
		colour_names.append(line.split('\t')[1])
		x_term.append(line.split('\t')[0])

while True:
	try:
		user_option = input('\x1bc1) Convert X-Term to Colour Name \n2) Convert Hex to Colour Name\n')
		if user_option == '1':
			x_term_to_hex = int(input('\nEnter an X-Term value (1-256)'))
			print('\nThe x-term colour {} converts to colour name \33[38;5;{}m{} and hex #{}'.format(str(x_term_to_hex),str(x_term_to_hex-1),colour_names[x_term_to_hex-1].replace('\t','').replace('(SYSTEM)',''),hex_colour_list[x_term_to_hex-1]))
			print("\n\033[0mCan't see the colour? Your terminal background is probably the same colour.\n")
			break
		if user_option == '2':
			hex_to_colour = input('Enter hex value: (000000-eeeeee)')	
			hex_value = [value for value in hex_colour_list if hex_to_colour in value]
			index = hex_colour_list.index(hex_value[0])
			print('\nThe hex number #{} converts to colour name \33[38;5;{}m{}'.format(str(hex_to_colour),str(x_term[index]),colour_names[index]).replace('\t','').replace('(SYSTEM)',''))
			break
	except ValueError:
		print('Error')
