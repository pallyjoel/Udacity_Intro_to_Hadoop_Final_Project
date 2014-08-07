import csv, sys


old_id = None

old_tag = None;
counter = 0;
tags = dict()
top= []

for row in sys.stdin:
	data = row.strip().split("\t")
	
	if len(data) != 2:
		continue
		
	new_tag, count = data
	
	#when a new tag is reached the counter is recorded as a key:value pair in a tag dictionary
	if old_tag != new_tag and old_tag !=None:
		tags[old_tag] = counter
		counter = 0;
		
	old_tag = new_tag
	counter = counter + 1
	

		
if old_tag != None:
	tags[old_tag] = counter	

#sort tag dictionary by highest count

sortedtags = sorted(tags.iteritems(), key=lambda x: x[1])

#print sortedtags
for i in range(1, 11):
	print sortedtags[-i][0], sortedtags[-i][1]

	
	