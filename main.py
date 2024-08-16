from flask import Flask
from flask_restful import Api

from apis import Question, QuestionAnswer

app = Flask(__name__)
api = Api(app)

api.add_resource(Question, '/question')
api.add_resource(QuestionAnswer, '/question/<int:q>')

if __name__ == '__main__':
    app.run(debug=True)
