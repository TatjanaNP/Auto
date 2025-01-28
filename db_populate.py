from models import db, Automobilis
from app import app

with app.app_context():
    automobiliai = [
        Automobilis(gamintojas="Volvo", modelis="EM80", spalva="mėlyna", salis="Švedija", kaina=12000),
        Automobilis(gamintojas="Volkswagen", modelis="Golf", spalva="daudona", salis="Vokietija", kaina=10000),
        Automobilis(gamintojas="Toyota", modelis="Camry", spalva="pilka", salis="Vokietija", kaina=10000),
        Automobilis(gamintojas="Volkswagen", modelis="Passat", spalva="raudona", salis="Vokietija", kaina=10000),
        Automobilis(gamintojas="Toyota", modelis="Camry", spalva="pilka", salis="Vokietija", kaina=13000),
        Automobilis(gamintojas="Volkswagen", modelis="Caddy", spalva="balta", salis="Vokietija", kaina=10000),
        Automobilis(gamintojas="Toyota", modelis="Corolla", spalva="pilka", salis="Vokietija", kaina=50000),
        Automobilis(gamintojas="Volkswagen", modelis="Tiguan", spalva="pilka", salis="Vokietija", kaina=10000),
        Automobilis(gamintojas="Volvo", modelis="EC40", spalva="pilka", salis="Švedija", kaina=10000),
        Automobilis(gamintojas="Toyota", modelis="Hilux", spalva="pilka", salis="Vokietija", kaina=2300),
        Automobilis(gamintojas="Toyota", modelis="RAV4", spalva="pilka", salis="Vokietija", kaina=42000),
    ]

    db.session.add_all(automobiliai)
    db.session.commit()
