from flask import Flask, request
from iebank_api import db, app
from iebank_api.models import Recipe


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'

@app.route('/recipes', methods=['POST'])
def create_account():
    name = request.json['name']
    ingredients = request.json['ingredients']
    recipe = Recipe(name, ingredients)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'created_at': recipe.created_at
    }