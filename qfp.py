import csv

class Question_Set(list):
    def filter(self, attr, val):
        qs2 = Question_Set()
        for q in self:
            if q[attr] == val:
                qs2.append(q)
        return qs2
    def get(self):
        if len(self)==1:
            return self[0]
        else:
            raise Exception("Can't 'get' from list with size %s" % (len(self)))
    def __str__(self):
        string = ''
        for i in self:
            string += str(i) + '\n\n'
        return string
        
class Question(dict):
    def __init__(self,parent,num,q,topic,time,correct_char,display_cols,choices):
        self.parent = parent
        self['num'] = num
        self['q'] = q
        self['topic'] = topic
        self['time'] = time
        self['correct_char'] = correct_char
        self['display_cols'] = display_cols
        self['choices'] = choices
        if self['correct_char'] != "none":
            self['correct_ans'] = self['choices'][self['correct_char']]
        else:
            self['correct_ans'] = "none"
    def partner(self):
        if self['time'] == 'demo':
            raise Exception("demo questions are only asked once")
        a = ['pre','post']
        a.remove(self['time'])
        partner_time = a[0]
        return self.parent.filter('q', self['q']).filter('time', partner_time).get()
    def sum_responses(self, us):
        num = self['num']
        total = {'-': 0}
        for i in self['choices']:
            total[i] = 0
        for u in us:
            ans = u.answers[num]
            if ans in total:
                total[ans] += 1
            else:
                print '%s tried to answer question %s with %s' % (u.ID, str(num), ans)
        return total
                
class Choices(dict):
    def __init__(self, data):
        for i,j in enumerate(data):
            if not (j=='-' or j==''):
                self[letter(i)] = j
                
def letter(n): #letter(0) = "A", etc
    if 0<=n and n<= 26:
        return chr(n + ord("A")).upper()
    else:
        raise Exception("n out of range")   

def read_question_file(filename):
    #Assumes that the file has a blank A1 and that Q1 data comes from column B
    qs = Question_Set()
    with open(filename, 'rb') as file:
        reader = csv.reader(file)
        data = list(reader)
        questions = data[0]
        for i,question in enumerate(questions):
            if i==0: continue  #skip the first column because it doesn't contain a question
            q = data[1][i]
            topic = data[2][i]
            time = data[3][i]
            correct_char = data[4][i]
            display_cols = data[5][i]
            choices = []
            for j in range(6,20):
                choiceRow = data[j:j+1]
                if choiceRow:
                    choice = choiceRow[0][i]
                choices.append(choice)
            choices = Choices(choices)
            q = Question(qs,i,q,topic,time,correct_char,display_cols,choices)
            qs.append(q)
    return qs

#qs = read_question_file('questions2.csv')
#x = qs.filter('num', 15).get()
#print x