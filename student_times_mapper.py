import sys, csv
#use csv reader to convert String lines into String arrays for processing
reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:

		
		print len(data)
		if len(data) != 19:
			continue
		#breaks up the line into useful information
		
		author_id = data[3]
		body = data[4]
		node_type = data[5]
		parent_id = data[6]
		abs_parent_id = data[7]
		
		#extract hour from time data
		time = data[8]
		hour = time[11:13]
		
		#print out author and hour of post
		print '{0}\t{1}'.format(author_id, hour)
		