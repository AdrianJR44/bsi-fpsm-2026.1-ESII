# enviador/enviador.py — a abstracao + uma implementacao real
from abc import ABC, abstractmethod


class Enviador(ABC):
    """Contrato minimo: todo enviador sabe enviar(para, texto)."""
    @abstractmethod
    def enviar(self, para, texto): ...


class ServidorSMTP(Enviador):
    def enviar(self, para, texto):
        print(f"[SMTP] enviando para {para}: {texto}")
