"""
function description : Take a dictionary and add a skill into into
algorithm :If skill exists in dictionary do not add else add
"""

def add_skill(skillname,skillname_dictionary):
	if skillname in skillname_dictionary:
		raise ValueError()
	else:
		skillname_dictionary[skillname]=False;


