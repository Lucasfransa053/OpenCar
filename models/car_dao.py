from models import db
from models.car import Car

class CarDAO:
    @staticmethod
    def get_all_cars():
        return Car.query.all()

    @staticmethod
    def get_car_by_id(car_id):
        return Car.query.get(car_id)

    @staticmethod
    def add_car(car):
        db.session.add(car)
        db.session.commit()

    @staticmethod
    def update_car(car):
        db.session.commit()

    @staticmethod
    def delete_car(car):
        db.session.delete(car)
        db.session.commit()