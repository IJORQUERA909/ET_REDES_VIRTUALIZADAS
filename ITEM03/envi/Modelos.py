from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class usuarios(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    rut = db.Column(db.Integer)

    def __init__(self, name, rut):
        super().__init__()
        self.nombre = name
        self.rut = rut

    def __str__(self):
        return "Nombre: {}. Rut: {}".format(
            self.nombre,
            self.rut
        )
    def serial(self):
        return {
            "rowid": self.rowid,
            "nombre": self.nombre,
            "rut": self.rut
        }
