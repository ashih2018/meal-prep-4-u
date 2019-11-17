from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/recipe')
def index():
    return render_template('recipe.html')

@app.route('/pantry')
def index():
    return render_template('pantry.html')

@app.route('/profile')
def index():
    return render_template('profile.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route("/api/load", methods=['POST'])
def get_recipes(ingredients):



if __name__ == '__main__':
    app.run(debug=False)
