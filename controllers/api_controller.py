from flask import Blueprint, request, jsonify
from models.car import Car
from models.car_dao import CarDAO

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/cars', methods=['GET'])
def get_cars():
    cars = CarDAO.get_all_cars()
    return jsonify([car.to_dict() for car in cars])

@api_bp.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    new_car = Car(
        model=data['model'],
        price_per_day=data['price_per_day'],
        stock=data['stock'],
        image_url=data['image_url']
    )
    CarDAO.add_car(new_car)
    return jsonify(new_car.to_dict()), 201

@api_bp.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    car = CarDAO.get_car_by_id(car_id)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404

    car.model = data['model']
    car.price_per_day = data['price_per_day']
    car.stock = data['stock']
    car.image_url = data['image_url']
    CarDAO.update_car(car)
    return jsonify(car.to_dict())

@api_bp.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = CarDAO.get_car_by_id(car_id)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404

    CarDAO.delete_car(car)
    return '', 204
