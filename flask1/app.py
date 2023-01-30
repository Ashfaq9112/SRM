from flask import Flask, url_for, render_template, request, redirect, session
app = Flask(__name__)





@app.route('/login', )
def login():
    return render_template('login.html')

@app.route('/login2', )
def login2():
    return render_template('login2.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/inbox')
def inbox():
    return render_template('studentmenu/inbox.html')

@app.route('/events')
def events():
    return render_template('studentmenu/events.html')

@app.route('/result')
def result():
    return render_template('studentmenu/result.html')

@app.route('/query')
def query():
    return render_template('studentmenu/query.html')













if(__name__ == '__main__'):
    app.run(debug=True)