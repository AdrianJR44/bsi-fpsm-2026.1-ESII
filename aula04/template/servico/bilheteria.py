# servico/bilheteria.py — agora com OCP (sem if/elif!)
#
# O serviço não sabe (nem precisa saber) o tipo de cada ingresso:
# cada objeto responde a preco() do seu jeito. Isto é polimorfismo.


def total(venda):
    """Soma os preços de todos os ingressos da venda."""
    return sum(i.preco() for i in venda)
