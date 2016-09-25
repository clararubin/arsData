from collections import OrderedDict

class Question:
    """ Question class for storing all question data"""
    
    # constructor
    def __init__(self, question_id, question_text, topic, time, correct_character, array_choices, num_col):
        self.question_id       = question_id
        self.question_text     = question_text
        self.correct_character = correct_character 
        self.topic             = topic
        self.time              = time 
        self.choices_dict      = OrderedDict( zip(MULTIPLE_CHOICE_LETTERS[0:len(array_choices)], array_choices))
        self.num_choices       = len(array_choices)
        self.num_col           = min(100000,num_col)
    
    # override default String returned when calling print()
    def __str__(self):
        return  "\nQuestion(\n\tquestion_id: {}\n\ttime: {}\n\ttopic: {}\n\tquestion_text: {}\n\tcorrect_character: {}\n\tchoices_dict: {}\n\tnum_col: {}\n)".format(self.question_id, self.time, self.topic, self.question_text, self.correct_character, self.choices_dict, self.num_col)
    def __repr__(self):
        return  "\n" + str(self)


class QuestionSection:
    """ QuestionSection class contains data for a particular set of questions"""

    # constructor
    def __init__(self, ids, questions):
        """
        Args:
            ids   : list of question_ids.
            questions : list of Question objects.
        """
        self.ids = ids
        self.questions = questions       
    
    # override default String returned when calling print()
    def __str__(self):
        return  "QuestionSection(\n\tid: {}\n\tquestions:{})".format(self.ids, self.questions)
    def __repr__(self):
        return  "\n" + str(self)




""" CONSTANTS: """
MULTIPLE_CHOICE_LETTERS = ['A','B','C','D','E','F','G','H']
NOT_APPLICABLE = 'n/a'
NO_CORRECT_ANSWER = 'none'
NO_RESPONSE = '-'
PRE = 'pre'
POST = 'post'
DEMO = 'demo'
ALL = 'all'
QFILE = "questions2.csv"
