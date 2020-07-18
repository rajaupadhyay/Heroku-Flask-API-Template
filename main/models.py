from main import db

class DBTemplate(db.Model):
    __tablename__ = 'db_template'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        