# main.py — versao 1.0
from servico.newsletter import ServicoNewsletter


if __name__ == "__main__":
    servico = ServicoNewsletter()
    servico.enviar_edicao("Edicao #42 no ar!")
