import random
from flask_restful import Resource
from flask import request, render_template, render_template_string, make_response

from utils import get_questions, get_question_by_id


class Home(Resource):
    def get(self):
        return make_response(render_template('home.html', content="Hello World!"))


class Question(Resource):
    def get(self):
        questions = get_questions()
        i = random.randint(0, len(questions) - 1)
        res = questions[i]
        return make_response(render_template('home.html', content=res))


class QuestionAnswer(Resource):
    def get(self):
        q = int(request.args.get("q"))
        question = get_question_by_id(q)
        if question.get("answer") == "-1":
            res = "Question not found!"
            return make_response(render_template('home.html', content=res))

        a = request.args.get("a")
        if a not in ['1', '2', '3', '4']:
            res = "Not valid answer!"
            return make_response(render_template('home.html', content=res))

        res = {'q': q,
               'a': a,
               'result': a == question.get("answer")}
        return make_response(render_template('home.html', content=res))


class QuestionAnswer2(Resource):
    def get(self, q):
        a = request.args.get("a")
        if a not in ['1', '2', '3', '4']:
            res = "Not valid answer!"
            return make_response(render_template('home.html', content=res))

        question = get_question_by_id(q)

        if question.get("answer") == "-1":
            res = "Question not found!"
            return make_response(render_template('home.html', content=res))

        res = {'q': q,
               'a': a,
               'result': a == question.get("answer")}
        return make_response(render_template('home.html', content=res))
