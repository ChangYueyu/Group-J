from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def introduction():
    return render_template('introduction.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/presentation')
def presentation():
    return render_template('presentation.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/github')
def github():
    return render_template('github.html')

if __name__ == '__main__':
    app.run(debug=True)