from flask import Flask, redirect, url_for, render_template
from forms import User
app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/")
def index():
    return redirect(url_for('signup'))


@app.route("/signup")
def signup():
    form = User()
    return render_template('items/signup.html', form = form)


if __name__ == "__main__":
    app.debug = True
    app.run()