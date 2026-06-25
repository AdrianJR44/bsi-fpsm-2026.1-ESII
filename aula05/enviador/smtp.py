# enviador/smtp.py — manda e-mail "de verdade"
# (aqui simulado com print; na vida real abriria conexao com um servidor SMTP)
class ServidorSMTP:
    def enviar(self, para, texto):
        print(f"[SMTP] enviando para {para}: {texto}")
