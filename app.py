from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = '"askljdgajskldhgajhskh'



@app.route('/index')
def index():
    return render_template('index.html', current_time=datetime.utcnow()), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
