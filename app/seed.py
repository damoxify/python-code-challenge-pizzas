#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app, db
from models import Restaurant, Pizza, RestaurantPizza


pizza_data = [
   {"id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
    {"id": 2, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
    {"id": 3, "name": "Supreme", "ingredients": "Pizza sauce, mozzarella, bacon, onion, beef mince, capsicum, pepperoni, mushroom, olives"},
    {"id": 4, "name": "HAWAIIAN (HAM & PINEAPPLE)", "ingredients": "Pizza sauce, mozzarella, ham, pineapple"},
    {"id": 5, "name": "BBQ MEATLOVERS", "ingredients": "BBQ sauce, mozzarella, pepperoni, bacon, cabanossi, beef mince, ham"},
    {"id": 6, "name": "GARLIC BUTTER PRAWNS AND CHILLI", "ingredients": "Pizza sauce, mozzarella, garlic butter prawns, capsicum, onion, chilli, rocket"},
    {"id": 7, "name": " SAUSAGE & KALE", "ingredients": "Pizza sauce, mozzarella, sausage, kale"},
    {"id": 8, "name": "Hot n’ spicy", "ingredients": "spicy salami, capsicum, sliced jalapenos, onions, hot sauce"},
    {"id": 9, "name": "Aussie pizza", "ingredients": "bacon, red onion, a whole egg cracked on"},
    {"id": 10, "name": "Spring pizza", "ingredients": "zucchini, artichoke, asparagus, spinach, and pesto dolloped"},
    {"id": 11, "name": "Seafood Pizza", "ingredients": "precooked squid, mussels, clams, prawns"},
    {"id": 12, "name": "BBQ chicken", "ingredients": "BBQ sauce, shredded chicken, red onion, smoked paprika"},
    {"id": 13, "name" : "CAPRICCIOSA (HAM, ARTICHOKE, MUSHROOMS, OLIVES)", "ingredients": "Pizza sauce, mozzarella, ham, artichoke, mushrooms, olives"},
    {"id": 14, "name" : "QUATTRO FORMAGGIO (FOUR CHEESE PIZZA)", "ingredients": "mozzarella, parmesan, provolone, blue cheese"},
    {"id": 15, "name" : "PROSCIUTTO AND ROCKET", "ingredients": "Pizza sauce, mozzarella, prosciutto, rocket/arugula, extra virgin olive oil"},
    {"id": 16, "name" : "MARGHERITA", "ingredients": "Pizza sauce, buffalo mozzarella, basil, olive oil, salt"},
    {"id": 17, "name" : "POTATO & ROSEMARY", "ingredients": "mozzarella, potato, fresh rosemary, extra virgin olive oilt"},


]


restaurant_names = [
    "A Better Pizza",	
    "All Around Pizza",
    "American Pie",
	"Americo Pizza",
    "Angry Pan Pizza",
    "Awesome Pizza",
	"Bar Toma",
    "Baroque Pizza",
    "Dodo Pizza",
    "Domino Pizza",
    "Basil & Cheese Pizzeria",
    "Bellapizza	Better Pizza",
    "Beyond Pizza",
    "Bigpizza",
    "Blood Pie Pizza",
    "Boldpizza",	
    "Bruno’s Pizza",	
    "Buddy’s Pizza",
    "Busy Street Pizza Cafe",
    "Buttercrust",
    "California Couple Pizza",
    "Cheesy and Bity",
    "Cherrypop Pizza",
    "Cippolini"
    "Circle Dream",
    "Circular Pi",
    "Coast Pizza",
    "Crazy Jack’s Pizza",
    "Crispy Pizza Corner",
    "Crispy Slices"
]


fake = Faker()

def pizzas():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    restaurants = []    
    for i in range(50):
        restaurant_details = Restaurant(name=rc(restaurant_names), address=fake.address())
        restaurants.append(restaurant_details)
    db.session.add_all(restaurants)
    db.session.commit()
        

    pizzas= []
    for pizza_properties in pizza_data:
        pizza_details = Pizza(name=(pizza_properties["name"]), ingredients=pizza_properties["ingredients"])
        pizzas.append(pizza_details)
    db.session.add_all(pizzas)
    db.session.commit()
        
    restaurant_pizzas = []
    for i in range(50):
        restaurant_pizza = RestaurantPizza(
            price=randint(5, 60),
            restaurant_id =rc(restaurants).id,
            pizza_id=rc(pizzas).id
            )
        restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
        

if __name__ == '__main__':
    with app.app_context():
        pizzas()
