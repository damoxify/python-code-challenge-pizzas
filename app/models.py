from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref, ForeignKey

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    pizzas = db.relationship('Restaurant', backref='pizza')


    def __repr__(self):
        return f'<Restaurant {self.name} is the best in {self.address}>'

# add any models you may need. 

class Pizza(db.Model):
    __tablename__: 'Pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)


    def __repr__(self):
        return f'<Pizza {self.name} is the best in {self.address}>'



class RestaurantPizza(db.Model):
    __tablename__: "RestaurantPizza"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return f'<Restaurant_Pizza price is {self.price}>'
