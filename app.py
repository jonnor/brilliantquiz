import os.path

import flask
from flask import Flask
app = Flask(__name__)

import quiz2020

images = os.listdir('static/images')

print('N questions', len(quiz2020.questions))
print('images', len(images), images)


def render_question(question_no,
                    submit_text='', submit_url='',
                    checked_idx=None, show_answer=False):
    info = quiz2020.questions[question_no]

    question = info[0]
    options = info[1]
    correct = info[2]

    image_url = flask.url_for('static', filename=os.path.join('images', images[question_no]))

    # Keep the given answer checked
    checks = [ checked_idx == i for i, _ in enumerate(options) ]

    # Mark the correct answer
    if show_answer:
        corrects = [ o == correct for o in options ]
    else:
        corrects = [ False ] * len(options)

    print(options, checks)

    html = flask.render_template('quiz.html',
            submit_url=submit_url,
            submit_text=submit_text,
            image_url=image_url,
            question_no=question_no,
            question=question,
            options=options,
            options_checked=checks,
            options_correct=corrects,
    )
    return html


@app.route('/question/<int:question_no>')
def get_question(question_no):

    if question_no == len(quiz2020.questions):
        return flask.redirect(f'/done')


    html = render_question(question_no,
            submit_text="Submit answer",
            submit_url=f"/answer/{question_no}")

    return html

@app.route('/answer/<int:question_no>')
def give_answer(question_no):

    info = quiz2020.questions[question_no]
    options = info[1]
    correct = info[2]

    answer = flask.request.args.get('answer', '')


    # Keep selected option checked
    try:
        answer_idx = options.index(answer)
    except ValueError:
        answer_idx = None
    # TODO: check if correct answer, increase score
    #if answer == correct:
    #    score += 1

    next = question_no + 1
    html = render_question(question_no,
                    submit_text="Next",
                    submit_url=f'/question/{next}',
                    checked_idx=answer_idx,
                    show_answer=True)

    return html

@app.route('/done')
def get_done():
    return "Congrats! Have a nice new year"


@app.route('/')
def index():
    return flask.redirect('/question/0')


if __name__ == '__main__':
   app.run(debug = True)
