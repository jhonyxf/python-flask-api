from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome': 'Sidney',
    'habilidades': ['Python','Flask','PHP']
    },
    {'nome': 'Camila',
    'habilidades': ['C#','sql']
    },
    {'nome': 'Jow',
    'habilidades': ['Java','Javascript']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro','mensagem':'Dev não existe'}
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso','mensagem':'Foi excluido'}


#Lista todos dev e inclui novo dev
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

#Inserir dev
class InserirDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return {'status':'sucesso', 'mensagem':'Registro inserido'}

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(InserirDesenvolvedores, '/dev/inserir/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == "__main__":
    app.run(debug=True)