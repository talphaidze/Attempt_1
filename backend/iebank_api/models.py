from iebank_api import db
from datetime import datetime
import string, random

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.recipe_number

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    