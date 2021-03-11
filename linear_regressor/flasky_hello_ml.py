from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    intro = "Hello World!"
    return render_template('hello_ml_deploy.html',intro = intro)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
