from dataclasses import dataclass, field

from modelos.item import Item


@dataclass
class Pedido:
    """Entidade de domínio: um pedido e suas regras próprias."""
    id: int
    cliente: str
    itens: list[Item] = field(default_factory=list)
    fechado: bool = False

     def adicionar(self, item: Item) -> None:
        # TODO: acrescentar o item à lista self.itens
        self.itens.append(item)
    def total(self) -> float:
        # TODO: somar o subtotal() de cada item
        return sum(i.subtotal() for i in self.itens)
