from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    site_name = "Roy Pizzeria"
    return render_template('home_page.html', site_name=site_name)


@app.route('/menu')
def prices():
    size_prices = {'small': 3,
                   'medium': 5,
                   'big': 7,
                   'alfredo': 1,
                   'mozzarella': 1}
    topping_prices = {'pineapple': 1,
                      'pepper': 1,
                      'olive': 1,
                      'chicken': 1,
                      'onion': 1}
    return render_template('menu.html', size_prices=size_prices, topping_prices=topping_prices)


@app.route('/pizzas')
def pizzas():
    return render_template('pizzas.html')


@app.route('/order')
def order():
    return render_template('order.html')


@app.route('/payment')
def payment():
    return render_template('order_payment.html')


@app.route('/current')
def current():
    orders = ['Baba', 'Ma', 'Avik', 'Aishi']
    return render_template('current_orders.html', orders=orders)


@app.route('/thank_you')
def thanks():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
