import os
from pathlib import Path

def combo_splitter(service):	
	directory = str(Path(__file__).parent)
	print('Current Directory: \n{} \n'.format(os.listdir(directory)))
	combo_list_name = service
	clean_list=[]
	with open(combo_list_name, 'r') as combo:
		for line in combo.readlines():
				clean_list.append(line.split(' | ')[0])			
	parsed_list_name = service+'_'
	with open(parsed_list_name,'a') as clean:
		for line in clean_list:
			clean.write(line+'\n')
	os.remove(service)
	os.rename(parsed_list_name, service)
