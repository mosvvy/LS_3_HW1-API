from flask_restful import Resource
from flask import request


class Question(Resource):
    def get(self):
        """
        Returns random question
        :return:
        """
        return {'id': 0,
                'question': 'Test question',
                'a1': 'r',
                'a2': 'r',
                'a3': 'r',
                'a4': 'r',
                'answer': '1'
                }


class QuestionAnswer(Resource):
    def get(self, q):
        a = 'a'
        a = request.args.get("a")
        return {'q': q,
                'a': a}
