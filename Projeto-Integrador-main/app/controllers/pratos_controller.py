
from flask import Blueprint

from app.models.repositorio import listar_pratos, buscar_prato
from app.views.respostas import resposta_sucesso, resposta_erro


pratos_bp = Blueprint("pratos", __name__, url_prefix="/api/pratos")


@pratos_bp.route("", methods=["GET"])
def obter_pratos():
    pratos = listar_pratos()

    dados = [
        prato.para_dict()
        for prato in pratos
        if prato.ativo
    ]

    return resposta_sucesso(dados)


@pratos_bp.route("/<int:identificador>", methods=["GET"])
def obter_prato(identificador):
    prato = buscar_prato(identificador)

    if prato is None or not prato.ativo:
        return resposta_erro("Prato não encontrado.", 404)

    return resposta_sucesso(prato.para_dict())