#!/usr/bin/env python


import re 

#flags =1 means ignore case 
def do_search(flags, regex, content):
	result=None
	if flags == 1 :
		result=re.search(regex, content,re.I)
		if result == None:
			return 0
		else:
			return 1 
	else:
		result=re.search(regex, content)
		if result == None:
			return 0
		else:
			return 1

 

def  match(match_type , condition, content,log ):
#file stuff 
	if match_type == "file":
		if condition == "regex":
			return do_search(0, content, log["object1"])
				

		if condition == "is":
			if content == log["object1"]:
				return 1 
			else :
				return 0 

		if condition == "eq":
			if content == log["object1"]:
				return 1 
			else :
				return 0 

		if condition == "eq_i":
			if content.upper() == log["object1"].upper():
				return 1 
			else :
				return 0 

		if condition == "regex_i":
			return do_search(1, content, log["object1"])

#reg stuff
	if match_type == "registry":
	


		if condition == "regex":
			return do_search(0, content, log["object1"])
				

		if condition == "is":
			if content == log["object1"]:
				return 1 
			else :
				return 0 

		if condition == "eq":
			if content == log["object1"]:
				return 1 
			else :
				return 0 

		if condition == "eq_i":
			if content.upper() == log["object1"].upper():
				return 1 
			else :
				return 0 

		if condition == "regex_i":
			return do_search(1, content, log["object1"])



if __name__ =="__main__":
	test="c:\window\test.exe"
	regex=".EXE$"

	print do_search(1, regex, test)
	print do_search(0, regex, test)




