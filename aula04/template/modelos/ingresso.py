# modelos/ingresso.py — as classes de domínio (a hierarquia de ingressos)
#
# Cada tipo de ingresso é uma classe que sabe calcular o seu próprio preço.
# A classe base Ingresso é o "contrato": todo ingresso responde a preco().


class Ingresso:
    """Contrato: todo ingresso sabe dizer o seu preço."""
    def preco(self) -> float:
        ...


class Inteira(Ingresso):
    def preco(self):
        return 20.0


class Meia(Ingresso):
    def preco(self):
        return 10.0


class VIP(Ingresso):
    def preco(self):
        return 35.0


# ---------------------------------------------------------------
# TODO (Parte B): adicione aqui a classe Cortesia
#
#   class Cortesia(Ingresso):
#       def preco(self):
#           return ???   # ingresso gratuito — qual é o valor?
#
# Depois, inclua um Cortesia() na venda do main.py e confira o total.
# ---------------------------------------------------------------
