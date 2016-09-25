import setup_questions as sq
import shared as sh


def main():
    questions_by_time , pre_post_question_ids = sq.import_questions(sh.QFILE)

    print "questions_by_time:"
    print questions_by_time[sh.ALL].questions

    print "\n\n\npre_post_question_ids:"
    print pre_post_question_ids


if __name__ == "__main__":
    main()