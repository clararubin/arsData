import setup_questions as sq
import shared as sh
import sys

def main():
	questions_by_time , pre_post_question_ids, questions_by_id = sq.import_questions(sh.QFILE)	

	output = ""
	output+= "*****printing questions_by_time[PRE]:\n"
	output+= str(questions_by_time[sh.PRE])

	output+= "\n\n\n*****printing pre_post_question_ids[0]:\n"
	output+= str(pre_post_question_ids)
	output+= str(pre_post_question_ids[0])

	output+= "\n\n*****printing Q1:"
	output+= str(questions_by_id['Q1'])

	# print to console
	print output

	# also print to testout.txt
	f = open('testout.txt', 'w')
	f.write(output)
	f.close()

if __name__ == "__main__":
    main()