import flask
from flask import Flask
app = Flask(__name__)

import quiz2020


@app.route('/')
def index():
    question_no = 0

    info = quiz2020.questions[question_no]

    question = info[0]
    options = info[1]
    correct = info[2]

    html = flask.render_template('quiz.html',

            question_no=question_no+1,
            question=question,
            options=options
    )

    return html


if __name__ == '__main__':
   app.run(debug = True)
