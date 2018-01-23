from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home(total=0):
    return render_template("form.html", total=total)

def add(curr, next):
    pass

@app.route('/', methods=['POST'])
def my_form_post():
    hours = request.form['hours']
    total = request.form['total']
    return home(float(hours) + float(total))
    #need to get total from home to actually add
