
def NULL_not_found(object: any) -> int:
	t = type(object)

	if(object == None):
		print("Nothing:", object, t)
	elif (t == float):
		print("Cheese:", object, t)
	elif (t == int):
		print("Zero:", object, t)
	elif (t == bool):
		print("Fake:", object, t)
	elif (t == str and not object):
		print("Empty:", object, t)
	else:
		print("Type not found")
	return 1