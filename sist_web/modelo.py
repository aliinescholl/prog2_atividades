import email
from config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    def json(self):
        return{
            "id":self.id,
            "nome":self.nome,
            "email":self.email,
            "telefone":self.telefone
        }
db.create_all()
p = {"id":1, "nome":"João", "email":"jp@gmail.com", "telefone":"543214321"}
print(p.json())