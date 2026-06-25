import datetime
from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome: str, email: str):
        if not nome or not email:
            raise ValueError("Nome e e-mail são obrigatórios para Pessoa.")
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"

class Equipamento(ABC):
    def __init__(self, id: int, nome: str, tipo: str):
        if not id or not nome or not tipo:
            raise ValueError("ID, nome e tipo são obrigatórios para Equipamento.")
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.disponivel = True

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        pass

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id}] {self.nome} ({self.tipo.capitalize()}) - {status}"

class Notebook(Equipamento):
    def __init__(self, id: int, nome: str):
        super().__init__(id, nome, "notebook")

    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 10.0 if dias_atraso > 0 else 0.0

class Projetor(Equipamento):
    def __init__(self, id: int, nome: str):
        super().__init__(id, nome, "projetor")

    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 15.0 if dias_atraso > 0 else 0.0

class CaboHDMI(Equipamento):
    def __init__(self, id: int, nome: str):
        super().__init__(id, nome, "cabo_hdmi")

    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 2.0 if dias_atraso > 0 else 0.0

class Emprestimo:
    def __init__(self, id: int, equipamento: Equipamento, solicitante: Pessoa, data_emprestimo: datetime.date, dias_emprestimo: int):
        if not id or not equipamento or not solicitante or not data_emprestimo or dias_emprestimo <= 0:
            raise ValueError("Dados de empréstimo incompletos ou inválidos.")
        self.id = id
        self.equipamento = equipamento
        self.solicitante = solicitante
        self.data_emprestimo = data_emprestimo
        self.data_devolucao_prevista = data_emprestimo + datetime.timedelta(days=dias_emprestimo)
        self.data_devolucao_real = None
        self.devolvido = False
        self.multa = 0.0

    def calcular_atraso(self, hoje: datetime.date) -> int:
        if self.devolvido:
            return 0 # Já devolvido, não há atraso atual
        
        atraso = (hoje - self.data_devolucao_prevista).days
        return max(0, atraso)

    def registrar_devolucao(self, data_devolucao: datetime.date):
        if self.devolvido:
            raise ValueError("Empréstimo já devolvido.")
        
        self.data_devolucao_real = data_devolucao
        self.devolvido = True
        dias_atraso = self.calcular_atraso(data_devolucao)
        self.multa = self.equipamento.calcular_multa(dias_atraso)
        self.equipamento.disponivel = True

    def __str__(self):
        status = "Devolvido" if self.devolvido else "Ativo"
        return (
            f"[{self.id}] Equipamento: {self.equipamento.nome} | Solicitante: {self.solicitante.nome} | "
            f"Empréstimo: {self.data_emprestimo} | Devolução Prevista: {self.data_devolucao_prevista} | "
            f"Status: {status} | Multa: R${self.multa:.2f}"
        )



class Notificador:
    def enviar_email(self, destinatario: str, assunto: str, corpo: str):
        # Simula o envio de e-mail. Em um sistema real, integraria com um serviço de e-mail.
        print(f"\n--- SIMULANDO ENVIO DE E-MAIL ---")
        print(f"Para: {destinatario}")
        print(f"Assunto: {assunto}")
        print(f"Corpo: {corpo}")
        print(f"-----------------------------------")



class SistemaEmprestimos:
    def __init__(self, equipamentos_iniciais: list[Equipamento], notificador: Notificador):
        self._equipamentos = {eq.id: eq for eq in equipamentos_iniciais}
        self._emprestimos = {}
        self._proximo_id_emprestimo = 1
        self._notificador = notificador

    def _gerar_id_emprestimo(self) -> int:
        new_id = self._proximo_id_emprestimo
        self._proximo_id_emprestimo += 1
        return new_id

    def registrar_emprestimo(self, equipamento_id: int, nome_solicitante: str, email_solicitante: str, dias_emprestimo: int) -> bool:
        try:
            equipamento = self._equipamentos.get(equipamento_id)
            if not equipamento or not equipamento.disponivel:
                print("ERRO: Equipamento inválido ou indisponível para empréstimo.")
                return False

            if dias_emprestimo <= 0:
                print("ERRO: O prazo mínimo de empréstimo é de 1 dia.")
                return False

            solicitante = Pessoa(nome_solicitante, email_solicitante)
            data_emprestimo = datetime.date.today()
            
            emprestimo_id = self._gerar_id_emprestimo()
            novo_emprestimo = Emprestimo(emprestimo_id, equipamento, solicitante, data_emprestimo, dias_emprestimo)
            
            self._emprestimos[emprestimo_id] = novo_emprestimo
            equipamento.disponivel = False

            self._notificador.enviar_email(
                solicitante.email,
                "Confirmação de Empréstimo de Equipamento",
                f"Olá {solicitante.nome},\n\nSeu empréstimo do equipamento {equipamento.nome} foi registrado com sucesso.\nData prevista para devolução: {novo_emprestimo.data_devolucao_prevista}.\n\nAtenciosamente,\nEquipe de TI UFRA São Miguel"
            )
            print(f"SUCESSO: Empréstimo do {equipamento.nome} para {solicitante.nome} registrado. Devolução prevista: {novo_emprestimo.data_devolucao_prevista}.")
            return True
        except ValueError as e:
            print(f"ERRO: {e}")
            return False

    def registrar_devolucao(self, emprestimo_id: int):
        try:
            emprestimo = self._emprestimos.get(emprestimo_id)
            if not emprestimo:
                print("ERRO: Empréstimo não encontrado.")
                return
            if emprestimo.devolvido:
                print("ERRO: Este empréstimo já foi devolvido.")
                return

            emprestimo.registrar_devolucao(datetime.date.today())
            
            mensagem_multa = f"Multa: R${emprestimo.multa:.2f}" if emprestimo.multa > 0 else "Sem multa."
            self._notificador.enviar_email(
                emprestimo.solicitante.email,
                "Confirmação de Devolução de Equipamento",
                f"Olá {emprestimo.solicitante.nome},\n\nSeu equipamento {emprestimo.equipamento.nome} foi devolvido com sucesso.\n{mensagem_multa}\n\nAtenciosamente,\nEquipe de TI UFRA São Miguel"
            )
            print(f"SUCESSO: Devolução do empréstimo {emprestimo_id} registrada. {mensagem_multa}")
        except ValueError as e:
            print(f"ERRO: {e}")

    def listar_emprestimos_atrasados(self):
        hoje = datetime.date.today()
        atrasados = []
        for emp_id, emprestimo in self._emprestimos.items():
            if not emprestimo.devolvido and emprestimo.data_devolucao_prevista < hoje:
                atrasados.append(emprestimo)
        
        if not atrasados:
            print("Nenhum empréstimo em atraso no momento.")
            return

        print("\n--- EMPRÉSTIMOS EM ATRASO ---")
        for emprestimo in atrasados:
            dias_atraso = emprestimo.calcular_atraso(hoje)
            multa_acumulada = emprestimo.equipamento.calcular_multa(dias_atraso)
            print(
                f"ID: {emprestimo.id} | Solicitante: {emprestimo.solicitante.nome} | "
                f"Equipamento: {emprestimo.equipamento.nome} | Dias em Atraso: {dias_atraso} | "
                f"Multa Acumulada: R${multa_acumulada:.2f}"
            )
            self._notificador.enviar_email(
                emprestimo.solicitante.email,
                "Notificação de Atraso de Equipamento",
                f"Olá {emprestimo.solicitante.nome},\n\nSeu equipamento {emprestimo.equipamento.nome} está em atraso!\nDias em atraso: {dias_atraso}. Multa acumulada: R${multa_acumulada:.2f}.\nPor favor, regularize a situação o mais breve possível.\n\nAtenciosamente,\nEquipe de TI UFRA São Miguel"
            )
        print("-----------------------------")


def exibir_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Registrar Empréstimo")
    print("2 - Registrar Devolução")
    print("3 - Listar Empréstimos em Atraso")
    print("0 - Sair")
    print("----------------------")

def main():
   
    equipamentos_iniciais = [
        Notebook(1, "Notebook Dell XPS 15"),
        Projetor(2, "Projetor Epson PowerLite"),
        CaboHDMI(3, "Cabo HDMI 2m"),
        Notebook(4, "Notebook Lenovo ThinkPad"),
    ]
    notificador = Notificador()
    sistema = SistemaEmprestimos(equipamentos_iniciais, notificador)

    print("\nSistema de Gestão de Empréstimos de Equipamentos (v2.0 - Refatorado)")
    print("Equipamentos disponíveis:")
    for eq in equipamentos_iniciais:
        print(f"  - {eq}")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                equipamento_id = int(input("ID do Equipamento: "))
                nome_solicitante = input("Nome do Solicitante: ")
                email_solicitante = input("Email do Solicitante: ")
                dias_emprestimo = int(input("Dias de Empréstimo (mín. 1): "))
                sistema.registrar_emprestimo(equipamento_id, nome_solicitante, email_solicitante, dias_emprestimo)
            except ValueError:
                print("ERRO: Entrada inválida. Certifique-se de digitar números para IDs e dias.")
        elif opcao == "2":
            try:
                emprestimo_id = int(input("ID do Empréstimo a ser devolvido: "))
                sistema.registrar_devolucao(emprestimo_id)
            except ValueError:
                print("ERRO: Entrada inválida. Certifique-se de digitar um número para o ID do empréstimo.")
        elif opcao == "3":
            sistema.listar_emprestimos_atrasados()
        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("ERRO: Opção inválida. Por favor, escolha uma opção do menu (0-3).")

if __name__ == "__main__":
    main()
