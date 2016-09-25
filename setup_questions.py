import shared as sh
import numpy as np
import pandas as pd

def get_qs_by_time(all_questions, time):
    """
    Utility function-- gets subset of Questions based on time.

    Args:
        all_questions : array of questions.
        time          : time (pre/post/demo) used to filter all_questions
    
    Returns:
        ids           : question_ids of Questions in specified time.
        questions     : subset of Questions in specified time.
    """

    questions  = list(filter(lambda q: q.time == time,  all_questions))
    ids        = [q.question_id for q in questions]
    return ids, questions



def import_questions(file_name):
    """Imports question data from csv file.

    Args:
        file_name : csv file containing question info.
    
    Returns:
        questions_by_time        : contains all question data, split by time (demo/pre/post).
        pre_post_question_ids : contains each group of corresponding pre/post question_ids.
    """

    # get dataframe from file
    questions_df = pd.DataFrame.from_csv(file_name)

    # create array of Question objects, each containing data for a single question
    all_questions = [
        sh.Question(
            question_id       = question_id,
            question_text     = questions_df[question_id]['question text'], 
            topic             = questions_df[question_id]['topic'], 
            time              = questions_df[question_id]['time'], 
            correct_character = questions_df[question_id]['correct character'], 
            array_choices     = [questions_df[question_id][k] for k in sh.MULTIPLE_CHOICE_LETTERS if questions_df[question_id][k]!= sh.NO_RESPONSE],
            num_col           = int(questions_df[question_id]['display cols'])
        ) 
        for question_id in questions_df
    ]

    # array of question_id's ("Q1", "Q2", etc.)
    question_ids = [q.question_id for q in all_questions]
    
    # filter Questions & question_id's by time
    pre_question_ids , pre_qs  = get_qs_by_time(all_questions, sh.PRE)
    post_question_ids, post_qs = get_qs_by_time(all_questions, sh.POST)
    demo_question_ids, demo_qs = get_qs_by_time(all_questions, sh.DEMO)

    # create QuestionSection object for each time section and store in dict
    questions_by_time = {
        sh.ALL  : sh.QuestionSection(question_ids     , all_questions), 
        sh.PRE  : sh.QuestionSection(pre_question_ids , pre_qs), 
        sh.POST : sh.QuestionSection(post_question_ids, post_qs), 
        sh.DEMO : sh.QuestionSection(demo_question_ids, demo_qs)
    }
    
    # group each corresponding pre/post question_id
    pre_post_question_ids = zip(pre_question_ids, post_question_ids)

    return questions_by_time, pre_post_question_ids


