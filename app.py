from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

#Devolve um dev pelo id, também altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro','mensagem':'Dev não existe'}
            
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Foi excluido'})


#Lista todos dev e inclui novo dev
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)