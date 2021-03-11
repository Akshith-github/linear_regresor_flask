from flask import Flask, render_template , redirect ,url_for, session
from flask_bootstrap import Bootstrap
import pickle

from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField
# from wtforms import IntegerRangeField
from wtforms.validators import DataRequired
app = Flask(__name__)
bootstrap=Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'
class NameForm(FlaskForm):
    bmi = FloatField('What is your bmi?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET', 'POST'])
def index():
    intro = "Hello World!"
    form = NameForm()
    bmi_inp= session.get("inp",None)
    result= session.get("result",None)
    if form.validate_on_submit():
        bmi_inp = form.bmi.data
        # print(bmi,type(bmi))
        #18.5 --> -0.1
        #22   -->  0.0
        #30.5  --> 0.2
        inp = (bmi_inp-22.5)*(1/40)
        filename = 'finalized_lr_diabets_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = float(loaded_model.predict([[inp]]))
        form.bmi.data=None
        session["inp"] = bmi_inp
        session["result"] = result
        print(inp,result)
        return redirect(url_for('index'))
    return render_template('hello_ml_deploy.html',intro = intro,form=form,input = bmi_inp,prediction = result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
