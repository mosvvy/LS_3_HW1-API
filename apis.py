
import random
from flask_restful import Resource
from flask import request

from utils import get_questions, get_question_by_id


class Question(Resource):
    def get(self):
        """
        Returns random question
        :return:
        """
        questions = get_questions()
        i = random.randint(0, len(questions)-1)
        res = questions[i]
        return res


class QuestionAnswer(Resource):
    def get(self, q):
        a = request.args.get("a")
        if a not in ['1', '2', '3', '4']:
            return "Not valid answer!"

        question = get_question_by_id(q)

        if question.get("answer") == "-1":
            return "Question not found!"

        return {'q': q,
                'a': a,
                'result': a == question.get("answer")}
