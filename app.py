import json
from flask import Flask, render_template, request
from project.http_requests import search_advanced

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/recipe')
def recipe():
    return render_template('recipe.html')


@app.route('/pantry')
def pantry():
    return render_template('pantry.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/pantrymethod', methods=['POST'])
def get_pantry_data():
    with open('pantry.json') as f:
      data = json.load(f)
    return json.dumps(data)


@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    print(list((pr, request.form[pr]) for pr in request.form))

    request_data = json.loads(list(request.form.keys())[0])
    query = request_data['query']
    incl = request_data['includeIngredients']
    excl = request_data['excludeIngredients']
    search = search_advanced(query, [], "", [], incl, excl, "",
                             0, None, None, None, None, "91c872bcb84c442f8599092ea7b1affb",
                             num_results=2)
    json_recipes = list(map(lambda r: r.to_json(), search))
    print("finished")
    print(json.dumps(json_recipes))
    return json.dumps(json_recipes)


def run():
    app.run(debug=False)


if __name__ == '__main__':
    run()
