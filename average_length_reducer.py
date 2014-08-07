import csv, sys


old_id = None

#question length
ques_len = 0

#the summed length of all the answers for a question
sum_ans_len = 0

#the number of answers for a given question
num_ans = 0


for row in sys.stdin:
	data = row.strip().split("\t")
	
	if len(data) != 3:
		continue
		
	new_id = data[0]
	node = data[1]
	lent = int(data[2])
	
	# Calculates the average answer length of previous question ID when a new question ID is reached
	if old_id != new_id and old_id !=None:
		#handles cases where no answers are provided
		if num_ans == 0:
			avg_ans = 0
		
		else:
			avg_ans = sum_ans_len / num_ans 
		print "{0}\t{1}\t{2}".format(old_id, ques_len, avg_ans)
		old_id = new_id
		ques_len = 0
		sum_ans_len = 0
		num_ans = 0
		
	if node == "question":
		ques_len = lent
	
	
	elif node == "answer":
		sum_ans_len += lent
		num_ans += 1
		
	old_id = new_id
	

		
if old_id != None:
	if num_ans == 0:
		avg_ans = 0
		
	else:
		avg_ans = sum_ans_len / num_ans 
	print "{0}\t{1}\t{2}".format(old_id, ques_len, avg_ans)	
	

	