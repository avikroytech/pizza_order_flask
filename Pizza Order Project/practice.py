from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    orders = [1, 2, 3, 4, 5]
    return render_template('practices.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)
