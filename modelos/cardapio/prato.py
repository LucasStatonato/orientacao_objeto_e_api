from modelos.cardapio.item_cardapio import ItemCardpio


class Prato(ItemCardpio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
