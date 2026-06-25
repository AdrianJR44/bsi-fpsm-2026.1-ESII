# main.py — ponto de entrada
from modelos.ingresso import Inteira, Meia, VIP
from servico.bilheteria import total


if __name__ == "__main__":
    venda = [Inteira(), Meia(), VIP()]
    for i in venda:
        print(f"{i.__class__.__name__}: R${i.preco():.2f}")
    print(f"Total: R${total(venda):.2f}")   # deve ser R$65.00

    # Depois de criar a classe Cortesia (em modelos/ingresso.py),
    # inclua um Cortesia() na lista venda acima e rode de novo:
    # o total continua R$65.00 e você NÃO precisou mexer no total().
