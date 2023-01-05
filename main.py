from flask import Flask, render_template, request, flash, session, redirect, url_for, send_file

app = Flask(__name__)


@app.route('/')
def index():
    titles = []
    amount = 0
    with open('static/assets/titles.txt', 'r') as data:
        for line in data:
            titles.append(line)
            amount += 1
    return render_template('index.html', titles=titles, amount=amount)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
