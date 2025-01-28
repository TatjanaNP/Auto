from models import db, Automobilis
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_cars = Automobilis.query.all()
    if all_cars:
        return render_template("index.html", automobiliai=all_cars)
    else:
        return "Duomenų nėra"


@app.route("/automobilis/<int:row_id>")
def one_car(row_id):
    car = Automobilis.query.get(row_id)
    if car:
        return render_template("car_info.html", automobilis=car)
    else:
        return "Duomenų nėra"


if __name__ == "__main__":
    app.run()
