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
    paieskos_tekstas = request.args.get("searchlaukelis")
    if paieskos_tekstas:
        search_text = request.args.get("searchlaukelis")
        paieskos_rez = Automobilis.query.filter(Automobilis.gamintojas.ilike(f"{search_text}%"))
        return render_template("index.html", automobiliai=paieskos_rez)

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


@app.route("/automobilis/redaguoti/<int:row_id>", methods=["get", "post"])
def update_car_info(row_id):
    car = Automobilis.query.get(row_id)
    if not car:
        return f"Automobilis su id. {row_id} neegzistuoja"

    if request.method == "GET":
        return render_template("update_car_info_form.html", automobilis=car)

    elif request.method == "POST":
        make = request.form.get("gamintojaslaukelis")
        model = request.form.get("modelislaukelis")
        color = request.form.get("spalvalaukelis")
        country = request.form.get("salislaukelis")
        price = request.form.get("kainalaukelis")

        car.gamintojas = make
        car.modelis = model
        car.spalva = color
        car.salis = country
        car.kaina = float(price)

        db.session.commit()
        return redirect(url_for("home"))  # nukreipimas i home funkcijos endpointa


@app.route("/automobilis/trinti/<int:row_id>", methods=["post"])
def delete_car(row_id):
    project = Automobilis.query.get(row_id)
    if not project:
        return "Duomenų nėra"
    else:
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/automobilis/naujas", methods=["get", "post"])
def create_car():
    if request.method == "GET":
        return render_template("create_car_form.html")
    if request.method == "POST":
        make = request.form.get("gamintojaslaukelis")
        model = request.form.get("modelislaukelis")
        color = request.form.get("spalvalaukelis")
        country = request.form.get("salislaukelis")
        price = request.form.get("kainalaukelis")
        print(make, model, color, country, price)
        if make and price:
            new_car = Automobilis(gamintojas=make, modelis=model, spalva=color, salis=country, kaina=price)
            db.session.add(new_car)
            db.session.commit()
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=5003, debug=True)
