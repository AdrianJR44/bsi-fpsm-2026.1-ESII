# main.py — ponto de entrada (versão 1.0)
from servico.bilheteria import vender, total


if __name__ == "__main__":
    venda = ["inteira", "meia", "vip"]
    for tipo in venda:
        vender(tipo)
    print(f"Total: R${total(venda):.2f}")   # R$65.00
