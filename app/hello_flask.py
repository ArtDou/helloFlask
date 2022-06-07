import random
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '834ef4e918003e0e0b01265df22f471b8ab028b20b6b34a6'

messages = []
with open("static/citations.txt") as file:
    citations = [line.rstrip() for line in file.readlines()]

@app.route('/')
def index():
    return render_template('index.html',messages=messages)

@app.route("/home")
def home():
    image = "./static/home.jpeg"
    return render_template('home.html', name="Tutur", image=image)

@app.route("/about")
def about():
    print (citations)
    citation = random.choice(citations)
    return render_template('about.html', citation=citation)

@app.route("/form", methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    
    return render_template('form.html')

app.run()