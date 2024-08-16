import json
import random

from flask_restful import Resource
from flask import request, jsonify


class Question(Resource):
    def get(self):
        """
        Returns random question
        :return:
        """
        with open('data/questions.json', 'r') as file:
            questions = json.load(file)
        i = random.randint(0, len(questions)-1)
        res = questions[i]
        return res


class QuestionAnswer(Resource):
    def get(self, q):
        a = 'a'
        a = request.args.get("a")
        return {'q': q,
                'a': a}
