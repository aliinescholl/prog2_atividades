from config import *
from modelo import Pessoa

@app.route("/")
def inicio():
    return("Backend funcionando!")

@app.route("/retornar_pessoas")
def retornar_pessoas:
    pessoas = db.session.query(Pessoa).all()
    pessoas_em_json = [x.json() for x in pessoas]
    resposta = jsonify(pessoas_em_json)
    resposta.headers.add("Acess-Control-Allow-Origin", "*")
    [{
        "id":self.id,
        "nome":self.nome,
        "email":self.email,
        "telefone":self.telefone
    }]
    return resposta

app.run()