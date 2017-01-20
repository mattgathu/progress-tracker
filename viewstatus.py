def view_skills(dct):
	for i in dct:
		if dct[i]:
			print("{}:   - Completed".format(i))
		else:
			print("{}:   - Not completed".format(i))


def view_studied(dct):
	for key in dct:
		if key:
			print(key)

def view_not_studied(dct):
	for key in dct:
		if not key:
			print(key)
