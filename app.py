import os.path

import flask
from flask import Flask
app = Flask(__name__)

import quiz2020

images = os.listdir('static/images')

print('N questions', len(quiz2020.questions))
print('images', len(images), images)


@app.route('/question/<int:question_no>')
def get_question(question_no):

    if question_no == len(quiz2020.questions):
        return flask.redirect(f'/done')


    info = quiz2020.questions[question_no]

    question = info[0]
    options = info[1]
    correct = info[2]


    image_url = flask.url_for('static', filename=os.path.join('images', images[question_no]))

    html = flask.render_template('quiz.html',
            image_url=image_url,
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
