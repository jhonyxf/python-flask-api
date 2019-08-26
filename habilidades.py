from flask_restful import Resource

lista_habilidades = ['Python', 'java', 'php', 'flask']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
