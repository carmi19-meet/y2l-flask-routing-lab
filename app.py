from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def my_shop():
	products = {"milk": "2$", "iphone xs": "too much$", "headphones": "200$", "smart watch": "300$"}

	return render_template("shop.html", products=products)



if __name__ == '__main__':
   app.run(debug = True)
