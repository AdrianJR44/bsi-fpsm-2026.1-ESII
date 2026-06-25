# servico/newsletter.py — Forma News (versao 1.0)
#
# Repare: o servico CRIA o repositorio e o servidor de e-mail dentro de si.
# Por isso ele e dificil de testar — rodar um teste mandaria e-mail de verdade.
from repositorio.assinantes import RepositorioAssinantes
from enviador.smtp import ServidorSMTP


class ServicoNewsletter:
    def __init__(self):
        self.repo = RepositorioAssinantes()   # cria sozinho
        self.email = ServidorSMTP()            # cria sozinho

    def enviar_edicao(self, texto):
        for a in self.repo.listar():
            if a.pode_receber():               # so envia a quem esta ativo
                self.email.enviar(a.email, texto)
