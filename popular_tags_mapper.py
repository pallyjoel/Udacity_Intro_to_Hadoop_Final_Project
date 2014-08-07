import sys, csv

#break up string line in to an array of strings
reader = csv.reader(sys.stdin, delimiter='\t')

for row in reader:
		if len(row) != 19:
			continue
		#print len(row)
		if row[0] == "id" :
			continue
		
		#break up array into useful pieces of info
		#print len(row)
		if row[3] == "\\N":
			author_id = 0
		else:
			author_id = (row[3])
		if row[0] == "\\N":
			forum_id = 0
		else:
			forum_id = (row[0])
		
		if row[2] == "\\N":
			tag = None;
		else:
			#break up individual tags of a post
			tag_full = row[2]
			tags = tag_full.split(" ")
			
		
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
		
		#individually print every tag associated with the question only along with a counter
		if node_type == "question":
			for i in range(0,len(tags)):
				print "{0}\t{1}".format(tags[i], 1)
	
		
		"""
		print '{0}\t{1}\t{2}\t{3}'.format(forum_id, parent_id, abs_parent_id, node_type,)
		#print '{0}\t{1}\t{2}\t{3}'.format(forum_id, node_type, parent_id, abs_parent_id)
		"""
		