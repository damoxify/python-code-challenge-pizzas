from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())

    # restaurant_pizzas = db.relationship('RestaurantPizza',  backref='restaurant')

    def _repr_(self):
        return f'<Restaurant {self.name} is the best in {self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurant_pizzas.pizza',)


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())

    # restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')

    def _repr_(self):
        return f'<Pizza {self.name} with ingredients {self.ingredients}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-restaurant.restaurant_pizzas', "-pizza.restaurant_pizzas",)


    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    price = db.Column(db.Float)


    # Validation: price must be between 1 and 30
    db.CheckConstraint('price >= 1 AND price <= 30', name='check_price_range')

    def _repr_(self):
        return f'<Restaurant_Pizza price is {self.price}>'