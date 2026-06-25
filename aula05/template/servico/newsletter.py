# servico/newsletter.py — Forma News (com DIP)
#
# Agora o servico RECEBE o repositorio e o enviador por construtor.
# Ele nao cria mais nada por dentro — so usa o que recebeu.
class ServicoNewsletter:
    def __init__(self, repo, email):
        self.repo = repo
        self.email = email

    def enviar_edicao(self, texto):
        for a in self.repo.listar():
            if a.pode_receber():
                self.email.enviar(a.email, texto)
