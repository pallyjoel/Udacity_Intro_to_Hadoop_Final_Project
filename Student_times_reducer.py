import csv, sys

from operator import itemgetter
id = None;

hour = None;
highest_hour = [];

#counts the number of posts in a given hour
new_count = 0;

#dictionary that records hour:# posts for each user
posts_perhour = {}

#sort hours by number of posts print out hour with the most posts
def maxvalue(id):
		
	b = sorted(posts_perhour.items(), key=itemgetter(1))
	
	print id, b[0][0]

		
for row in sys.stdin:

	data = row.strip().split('\t')
	
	if len(data) != 2:
		continue
	new_id, new_hour = data

	# once the hour has changed record the count for the previous hour

	if new_id == id and new_hour != hour and hour != None:

		posts_perhour[hour] = new_count
		hour = new_hour
		new_count = 0;
	# once the id has changed print hour with the highest count for previous id
	
	if new_id != id and id != None:
		posts_perhour[hour] = new_count
		maxvalue(id)
		new_count = 0
		posts_perhour = {}
	
	id = new_id
	hour = new_hour
	new_count = new_count +1
	
if id != None:

	posts_perhour[hour] = new_count
	maxvalue(id)

	