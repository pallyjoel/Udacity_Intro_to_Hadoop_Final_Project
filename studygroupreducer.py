import csv, sys


old_id = None

#array of all author ids for a given forum id
users = []

for row in sys.stdin:
	data = row.strip().split("\t")
	
	if len(data) != 2:
		continue
	
	id, author = data
	
	if old_id != id and old_id != None:
		print "{0}\t{1}".format(old_id, users)
		users = []
	
	#iteratively appends the users array
	old_id = id
	users.append(author)


		
if old_id != None:
	print "{0}\t{1}".format(old_id, users)	


	
	