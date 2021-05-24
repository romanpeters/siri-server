from flask import render_template, redirect, request
from app import app
from app.siri import hey_siri

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['siri-input']
        if query:
            hey_siri(query)
    return render_template("index.html")
