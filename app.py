import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return flask.render_template('quiz.html', name='Marianna')

if __name__ == '__main__':
   app.run(debug = True)
