import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   options = ['Foo', 'Bar', 'Baz', 'BarBaz']

   question = "What is the right answer?"
   question_no = 1

   return flask.render_template('quiz.html', question_no=question_no, question=question, options=options)

if __name__ == '__main__':
   app.run(debug = True)
