from flask import Flask, render_template

app = Flask(__name__)

from controllers.products_controller import products_blueprint

app.register_blueprint(products_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True)