def view_skills(dct):
	for i in dct:
		if dct=={}:
			return "no status"
		else:
			return dict.items()


def view_studied(dct):
	studied={}
	for i in dct:
		if dct[i]==True:
			studied[i]= True
			print(studied) 
		else:
			pass
			
def view_not_studied(dct):
	not_studied={}
	for i in dct:
		if dct[i]==False:
			not_studied[i]= True
			print(not_studied) 
		else:
			pass




