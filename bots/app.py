from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')
@app.route('/your_flask_funtion1')
def get_ses1():
 	return render_template('index.html')
@app.route('/your_flask_funtion2')
def get_ses2():
 	return render_template('index.html')
@app.route('/your_flask_funtion3')
def get_ses3():
 	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
