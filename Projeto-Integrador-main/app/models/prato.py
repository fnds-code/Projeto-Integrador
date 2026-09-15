class Prato:
    def __init__(self, identificador, nome, descricao, preco, ativo=True):
        self.identificador = identificador
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.ativo = ativo

    def para_dict(self):
        return {
            "id": self.identificador,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "ativo": self.ativo
        }