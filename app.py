from flask import Flask, render_template, flash
from models import db
from controllers.user_controller import user_bp
from controllers.reservation_controller import reservation_bp
from controllers.display_car_controller import display_car_bp
from models.car import Car
from models.car_dao import CarDAO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opencar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Adicione uma chave secreta para usar flash

db.init_app(app)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/usuarios')
app.register_blueprint(reservation_bp, url_prefix='/reservas')
app.register_blueprint(display_car_bp, url_prefix='/carros')

@app.route('/')
def index():
    return render_template('index.html')

def initialize_cars():
    cars = [
        {"model": "Fiat Uno", "price_per_day": 70.0, "stock": 3},
        {"model": "Volkswagen Gol", "price_per_day": 70.0, "stock": 3},
        {"model": "Ford Fiesta", "price_per_day": 70.0, "stock": 3},
        {"model": "Chevrolet Onix", "price_per_day": 150.0, "stock": 3},
        {"model": "Toyota Corolla", "price_per_day": 300.0, "stock": 3},
        {"model": "Honda Civic", "price_per_day": 250.0, "stock": 3},
        {"model": "Hyundai HB20", "price_per_day": 150.0, "stock": 3}
    ]
    for car_data in cars:
        car = Car(model=car_data["model"], price_per_day=car_data["price_per_day"], is_reserved=False, stock=car_data["stock"])
        CarDAO.add_car(car)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if Car.query.count() == 0:
            initialize_cars()
    app.run(debug=True)
