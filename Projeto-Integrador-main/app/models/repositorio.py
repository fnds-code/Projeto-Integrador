
from app.models.prato import Prato


_pratos = [
    Prato(
        identificador=1,
        nome="Marmita Executiva",
        descricao="Arroz, feijão, carne e salada.",
        preco=25.90
    ),
    Prato(
        identificador=2,
        nome="Macarrão Artesanal",
        descricao="Macarrão com molho de tomate caseiro.",
        preco=22.50
    ),
    Prato(
        identificador=3,
        nome="Frango Grelhado",
        descricao="Frango grelhado com arroz e legumes.",
        preco=28.00
    )
]


def listar_pratos():
    return _pratos


def buscar_prato(identificador):
    for prato in _pratos:
        if prato.identificador == identificador:
            return prato

    return None