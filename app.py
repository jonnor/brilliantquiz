import flask
from flask import Flask
app = Flask(__name__)

import quiz2020

print('N questions', len(quiz2020.questions), quiz2020.questions[-1])


@app.route('/question/<int:question_no>')
def get_question(question_no):

    if question_no == len(quiz2020.questions):
        return flask.redirect(f'/done')


    info = quiz2020.questions[question_no]

    question = info[0]
    options = info[1]
    correct = info[2]

    html = flask.render_template('quiz.html',

            question_no=question_no,
            question=question,
            options=options
    )

    return html

@app.route('/answer/<int:question_no>')
def give_answer(question_no):
    next = question_no + 1
    return flask.redirect(f'/question/{next}')

@app.route('/done')
def get_done():
    return "Congrats! Have a nice new year"


@app.route('/')
def index():
    return flask.redirect('/question/0')


if __name__ == '__main__':
   app.run(debug = True)
