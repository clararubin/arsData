import qfp, rfp
reload(qfp)
reload(rfp)

qs = qfp.read_question_file('questions2.csv')
#q15 = qs.filter('num', 15).get()

us = rfp.read_response_file('Results Detail - Houston.csv')
#u1 = us.lookup('94CB9')

for q in qs.filter('time','pre'):
    x = q.sum_responses(us)
    y = q.partner().sum_responses(us)
    print str(q['num']) + '/' + str(q.partner()['num']) + ': ' + q['q']
    print q['correct_char'] + ': ' + q['correct_ans']
    print x
    print y
    print ''