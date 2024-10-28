from flask import Flask, request, jsonify
from flask_cors import CORS
from database import deletar_presente, init_db, adicionar_presente, listar_presentes, adicionar_convidado

app = Flask(__name__)
CORS(app)

# Inicializa o banco de dados
init_db()

@app.route('/api/presentes', methods=['POST'])
def adicionar_presente_route():
    """
    Rota para adicionar um novo presente.
    Recebe dados JSON e adiciona ao banco de dados.
    """
    try:
        data = request.get_json()
        nome = data.get('nome')
        marca = data.get('marca')
        cor = data.get('cor')
        imageUrl = data.get('imageUrl')

        if not all([nome, marca, cor, imageUrl]):
            return jsonify({"error": "Todos os campos são obrigatórios."}), 400

        adicionar_presente(nome, marca, cor, imageUrl)
        return jsonify({"message": "Presente adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/presentes', methods=['GET'])
def listar_presentes_route():
    """
    Rota para listar todos os presentes.
    Retorna todos os presentes armazenados no banco de dados.
    """
    try:
        presentes = listar_presentes()
        return jsonify(presentes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/convidados', methods=['POST'])
def adicionar_convidado_route():
    try:
        data = request.get_json()
        nome = data.get('nome')
        telefone = data.get('telefone')
        email = data.get('email')
        presente_id = data.get('presente_id')

        if not all([nome, telefone, email, presente_id]):
            return jsonify({"error": "Todos os campos são obrigatórios."}), 400

        adicionar_convidado(nome, telefone, email, presente_id)
        return jsonify({"message": "Convidado adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/presentes/<int:presente_id>', methods=['DELETE'])
def deletar_presente_route(presente_id):
    """
    Rota para deletar um presente com base no ID.
    """
    try:
        deletar_presente(presente_id)
        return jsonify({"message": "Presente deletado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
