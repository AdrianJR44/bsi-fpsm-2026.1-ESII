# modelos/assinante.py — quem recebe a newsletter
class Assinante:
    """Contrato: todo assinante diz se pode receber a edição agora (um bool)."""
    def __init__(self, email, confirmado=True):
        self.email = email
        self.confirmado = confirmado

    def pode_receber(self) -> bool:
        ...


class Gratis(Assinante):
    # grátis: só recebe depois de confirmar o e-mail (double opt-in)
    def pode_receber(self):
        return self.confirmado


class Premium(Assinante):
    # premium (conta paga): está sempre ativa
    def pode_receber(self):
        return True
