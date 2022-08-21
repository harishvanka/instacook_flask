from flask import Flask, request, jsonify
from models import recipes
from http import HTTPStatus

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'First API'


@app.route('/recipes', methods=['GET'])
def get_all_recipies():
    """
    This method will return all recipies
    :return: json data with all recipies
    """
    return jsonify(data=recipes)


@app.route('/recipes/<int:recipe_id>')
def get_recipe(recipe_id):
    """
    This method will return a recipe if  id is found else returns NOT FOUND
    :param recipe_id:
    :return: recipe if found else NOT_FOUND status
    """
    recipe_found = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if recipe_found:
        return jsonify(recipe_found)
    return jsonify(message='Recipe not found'), HTTPStatus.NOT_FOUND
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
