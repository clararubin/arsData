import csv

class User_Set(list):
    #def __init__(self):
    #    pass
    def __str__(self):
        string = ''
        for i in self:
            string += str(self[i]) + '\n\n'
        return string
    def get(self):
        if len(self)==1:
            return self[0]
        else:
            raise Exception("Can't 'get' from list with size %s" % (len(self)))
    def lookup(self, ID):
        for u in self:
            if u.ID == ID:
                return u
    def got_right(self, Question):
        us2 = User_Set()
        for u in self:
            if u.got_right(Question):
                us2.append(u)
        return us2
    def gave_answer(self, Question, ans):
        us2 = User_Set()
        for u in self:
            if u.gave_answer(Question, ans):
                us2.append(u)
        return us2

class User(object):
    def __init__(self, ID, answers):
        self.ID = ID
        self.answers = {}
        for i,j in enumerate(answers):
            self.answers[i+1] = j
    def __str__(self):
        string = self.ID
        for i in range(1,4):
            string += str(i) + ": " + self.answers[i] + ", "
        string += '...'
        return string
    def got_right(self, Question):
        num = Question['num']
        my_ans = self.answers[num]
        correct_char = Question['correct_char']
        return (my_ans == correct_char)
    def gave_answer(self, Question, ans):
        num = Question['num']
        my_ans = self.answers[num]
        return (my_ans == ans)

def read_response_file(file):
    us = User_Set()
    with open(file, 'rb') as file:
        #fileData = {}
        reader = csv.reader(file)
        data = list(reader)
        for i in range(7,200):
            row = data[i:i+1]
            if row:
                row = row[0]
                ID = row[0]
                answers = row[1:]
                us.append(User(ID, answers))
    return us

#us = read_response_file('Results Detail - Houston.csv')
#print us.lookup('5778E')