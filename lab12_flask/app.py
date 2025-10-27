"""
Henry Perez
October 27th, 2025
Lab 12, Introduction to Flask
"""
from flask import Flask, render_template, url_for

"""
create an object 'app' from the Flask module
__name__ set to __main__ i the script is running directly from the main file
"""
app = Flask(__name__)

# set the routing to the main(loading) page
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Quotes<h1>'

# set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == "__main__":
    app.run(debug=True)


