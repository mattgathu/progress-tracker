'''
	check_skill_completed function accepts two parameter
	skillname, which is the name of the skill and skill_dict,
	which is the dictonary containing all skills
'''
def check_skill_completed(skillname, skill_dict):

	# checks if skill name is in dictonary, if not raises a Value Error
	if skillname not in skill_dict:
		raise ValueError
	else:
		skill_dict[skillname] = True;

	return skill_dict;
