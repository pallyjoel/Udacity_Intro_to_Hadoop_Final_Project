import sys, csv

#break up string line into an array of strings
reader = csv.reader(sys.stdin, delimiter='\t')


for row in reader:
		if len(row) != 19:
			continue
		#print len(row)
		if row[0] == "id" :
			continue
		
		#break up array into useful information
		if row[3] == "\\N":
			author_id = 0
		else:
			author_id = (row[3])
		if row[0] == "\\N":
			forum_id = 0
		else:
			forum_id = (row[0])
		
		if row[6] == "\\N":
			parent_id = 0
		else:
			parent_id = (row[6])
		
		if row[7] == "\\N":
			abs_parent_id = 0;
		else:	
			abs_parent_id = (row[7])		
		body = row[4]
		
		node_type = row[5]

		time = row[8]
		hour = time[11:13]
		
		#prints all authors associated with a common forum_id
		
		if node_type == "question":
			print "{0}\t{1}".format(forum_id, author_id)
	
		if node_type == "answer" or node_type == "comment":
			print "{0}\t{1}".format(parent_id, author_id)
		
		"""
		print '{0}\t{1}\t{2}\t{3}'.format(forum_id, parent_id, abs_parent_id, node_type,)
		#print '{0}\t{1}\t{2}\t{3}'.format(forum_id, node_type, parent_id, abs_parent_id)
		"""
		