import json


def get_questions():
    with open('data/questions.json', 'r') as file:
        questions = json.load(file)
        return questions


def get_question_by_id(q):
    with open('data/questions.json', 'r') as file:
        questions = json.load(file)
        for question in questions:
            if question.get('id') == q:
                return question
    return {'answer': '-1'}
