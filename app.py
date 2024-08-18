# S-1 import falsk
from flask import Flask


# S-2 create the object and pass __name__
app = Flask(__name__)

@app.route('/about') 
def about():
    return " this is the about us page"
@app.route('/', methods=['POST'])
def home():
    return "Hello! This is a Billion dollars Project"

@app.route('/magic')
def addition_function():
    a= 5
    b= 6
    sum= a+b
    return str(sum)

if __name__ == '__main__':
    app.run(debug=True)