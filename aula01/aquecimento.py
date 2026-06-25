class Pessoa:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def dizer_oi(self) -> str:
        return f"Oi, sou o Ádrian {self.nome}"

class Aluno(Pessoa):
    def __init__(self, nome: str, email: str, matricula: str):
        super().__init__(nome, email)
        self.matricula = matricula

    def dizer_oi(self) -> str:
        return f"Oi, sou o Ádrian {self.nome} (matrícula {self.matricula})"

if __name__ == "__main__":
    pessoas: list[Pessoa] = [
        Pessoa("Ádrian Vidinha", "Ádrian@exemplo.com"),
        Aluno("Ádrian Gomes", "Ádrian@ufra.edu.br", "202601001")
    ]

    for pessoa in pessoas:
        print(pessoa.dizer_oi())
  
