from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False 
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome to Pizza Restaurant Full stack Application</h1>'

@app.route('/restaurants')
def restaurants():
    restaurants = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = restaurant.to_dict()
        restaurants.append(restaurant_dict)

    response = make_response(jsonify(restaurants), 200)
    return response

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_id(id):
    if request.method == 'GET':
        restaurant = Restaurant.query.get(id)  
        if restaurant:
            restaurant_dict = restaurant.to_dict()
            response = make_response(jsonify(restaurant_dict), 200)
        else:
            response = make_response(jsonify({"error": "Restaurant not found"}), 404)
        return response

    elif request.method == 'DELETE':
        restaurant_deleted = Restaurant.query.get(id)  
        if restaurant_deleted:
            restaurant_dict = restaurant_deleted.to_dict()
            db.session.delete(restaurant_deleted)
            db.session.commit()
            response = make_response(jsonify(restaurant_dict), 200)
        else:
            response = make_response(jsonify({"error": "Restaurant not found"}), 404)
        return response

@app.route('/pizzas')
def pizzas():
    pizzas_list = Pizza.query.all()  

    pizza_dicts = [pizza.to_dict() for pizza in pizzas_list]
    response = make_response(jsonify(pizza_dicts), 200)
    return response

@app.route('/restaurant_pizzas', methods=['GET', 'POST'])
def restaurant_pizza():
    if request.method == 'GET':
        rps = []
        for rp in RestaurantPizza.query.all():
            rp_dict = rp.to_dict()
            rps.append(rp_dict)
        response = make_response(jsonify(rps), 200)
        return response
    
    elif request.method == 'POST':
        # rp shorts for restaurant pizza
        created_rp = RestaurantPizza(
            price=request.form.get("price"),
            pizza_id=request.form.get("pizza_id"),
            restaurant_id=request.form.get("restaurant_id")
            )
        db.session.add(created_rp)
        db.session.commit()

        created_rp_dict = created_rp.to_dict()
        response = make_response(jsonify(created_rp_dict), 201)
        if not response:
            return {"errors": ["validation errors"]}
        
        return response
    



    

if __name__ == '__main__':
    app.run(port=5555)