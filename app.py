from flask import Flask, request, render_template
from get_that_ratio import get_big_timers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_form_submission():
    text1 = request.form['text1']
    text2 = request.form['text2']

    # Call your Python script here and pass it text1 and text2 as arguments
    result = get_big_timers(text1, text2)
    # Store the returned list of strings in a variable called `result`

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()