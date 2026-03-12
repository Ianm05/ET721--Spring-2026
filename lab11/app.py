"""
Ian Martinez
Lab 11, Introduction to Flask
March 10, 2026
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Ian Martinez"
    fruits = ['apple', 'banana', 'orange']
    return render_template('index.html', username=name, listfruits=fruits)

@app.route('/about')
def about():
    images = ['Field.jpg', 'Pizzeria.jpg', 'Playground.jpg']
    return render_template('about.html', image_list=images)

@app.route('/quotes')
def quotes():
    return "<h1>Quotes</h1>"

if __name__ == '__main__':
    app.run(debug=True)