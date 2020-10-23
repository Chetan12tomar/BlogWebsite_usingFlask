from flask import Flask, render_template
app=Flask(__name__)

@app.route('/') 
def homepage():
    return 'Welcome to Algoladder'

@app.route('/about')
def about():
    return 'Hi,my name is Shreya'

app.run(debug=True)

