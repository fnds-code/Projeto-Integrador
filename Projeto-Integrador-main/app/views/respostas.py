
from flask import jsonify


def resposta_sucesso(dados, status=200):
    return jsonify({
        "sucesso": True,
        "dados": dados
    }), status


def resposta_erro(mensagem, status=400):
    return jsonify({
        "sucesso": False,
        "erro": mensagem
    }), status