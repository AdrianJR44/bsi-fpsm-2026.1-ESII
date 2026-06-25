# main.py — o ponto de entrada monta tudo (composition root)
from repositorio.assinantes import RepositorioAssinantes
from enviador.enviador import ServidorSMTP
from servico.newsletter import ServicoNewsletter


if __name__ == "__main__":
    repo = RepositorioAssinantes()
    email = ServidorSMTP()                     # o e-mail "de verdade"
    servico = ServicoNewsletter(repo, email)   # injeta as pecas
    servico.enviar_edicao("Edicao #42 no ar!")
