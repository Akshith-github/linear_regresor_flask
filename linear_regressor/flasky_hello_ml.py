from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
bootstrap=Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'
class NameForm(FlaskForm):
    bmi = IntegerField('What is your bmi?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    intro = "Hello World!"
    form = NameForm()
    return render_template('hello_ml_deploy.html',intro = intro,form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
