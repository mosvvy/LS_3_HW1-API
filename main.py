from flask import Flask
from flask_restful import Api

from apis import Home, Question, QuestionAnswer, QuestionAnswer2

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(Question, '/question')
api.add_resource(QuestionAnswer, '/answer')
api.add_resource(QuestionAnswer2, '/question/<int:q>')

if __name__ == '__main__':
    app.run(debug=True)
