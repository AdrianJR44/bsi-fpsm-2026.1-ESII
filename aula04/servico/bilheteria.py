# servico/bilheteria.py — Bilheteria CineForma (versão 1.0)
#
# Repare: o cálculo do preço aparece em DOIS lugares (vender e total).
# Se o preço de um tipo mudar, é preciso lembrar de corrigir nos DOIS!


def vender(tipo):
    # decide o preço olhando o tipo:
    if tipo == "inteira":
        preco = 20.0
    elif tipo == "meia":
        preco = 10.0
    elif tipo == "vip":
        preco = 35.0
    else:
        print(f"Tipo desconhecido: {tipo}")
        return 0.0
    print(f"Ingresso {tipo}: R${preco:.2f}")
    return preco


def total(venda):
    s = 0.0
    for tipo in venda:
        if tipo == "inteira":
            s += 20.0
        elif tipo == "meia":
            s += 10.0
        elif tipo == "vip":
            s += 35.0
    return s
