from calendar import month
from config import *
from datetime import date


class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    data = db.Column(db.Date)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        s = f"{self.id}, {self.nome}, {self.email}, {self.telefone}, "
        s += f"{self.data.day}/{self.data.month}/{self.data.year}"
        return s
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "data": self.data
        }


# teste
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p1 = Pessoa(nome="João da Silva", email="josilva@gmail.com",
                telefone="47 99012 3232", data=date(2020, 10, 5))
    p2 = Pessoa(nome="Maria Oliveira", email="molive@gmail.com",
                telefone="47 98822 2531", data=date(2014, 5, 10))

    # persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    # exibir a pessoa
    print(p2)

    # exibir a pessoa no format json
    print(p2.json())
