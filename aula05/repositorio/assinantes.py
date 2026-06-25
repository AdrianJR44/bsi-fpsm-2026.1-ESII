# repositorio/assinantes.py — guarda os assinantes (em memória)
from modelos.assinante import Gratis, Premium


class RepositorioAssinantes:
    def __init__(self):
        self._assinantes = [
            Gratis("ana@exemplo.com"),
            Premium("bia@exemplo.com"),
        ]

    def listar(self):
        return self._assinantes
