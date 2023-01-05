from flask import Flask, render_template, redirect, flash, request, session
import jinja2
import melons

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/melons')
def all_melons():
    melon_list = melons.list_of_melons()

    return render_template('melons.html', melon_list = melon_list)

@app.route('/melons/<melon_id>')
def individual_melon(melon_id):
    melon = melons.get_melon_by_id(melon_id)

    return render_template('individual_melon.html', melon = melon)

@app.route('/add_to_cart<melon_id>')
def add_to_cart(melon_id):
    return f'{melon_id} added to cart.'

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug = True, port = 8000, host = 'localhost')