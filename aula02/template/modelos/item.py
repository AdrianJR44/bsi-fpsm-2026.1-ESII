from dataclasses import dataclass


@dataclass
class Item:
    """Entidade de domínio: um item do pedido."""
    nome: str
    preco: float
    qtd: int = 1

    def subtotal(self) -> float:
        # TODO: retornar preço × quantidade
        return self.preco * self.qtd
