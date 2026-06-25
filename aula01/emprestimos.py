import datetime
from abc import ABC, abstractmethod

class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

class Equipamento(ABC):
    """Classe base abstrata para todos os equipamentos."""
    def __init__(self, id_equipamento: int, nome: str):
        self.id = id_equipamento
        self.nome = nome
        self.disponivel = True

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        """Método abstrato: cada subclasse deve implementar sua própria regra de multa."""
        pass

class Notebook(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 10.0 if dias_atraso > 0 else 0.0

class Projetor(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 15.0 if dias_atraso > 0 else 0.0

class Cabo(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 2.0 if dias_atraso > 0 else 0.0

class Emprestimo:
    def __init__(self, id_emprestimo: int, equipamento: Equipamento, usuario: Usuario, dias: int):
        self.id = id_emprestimo
        self.equipamento = equipamento
        self.usuario = usuario
        self.data_emprestimo = datetime.date.today()
        self.data_devolucao = self.data_emprestimo + datetime.timedelta(days=dias)
        self.devolvido = False

    def calcular_atraso(self, data_atual: datetime.date) -> int:
        if data_atual > self.data_devolucao and not self.devolvido:
            return (data_atual - self.data_devolucao).days
        return 0

    def valor_multa_atual(self, data_atual: datetime.date) -> float:
        atraso = self.calcular_atraso(data_atual)
        # Polimorfismo em ação: não importa qual é o equipamento, ele sabe calcular sua multa
        return self.equipamento.calcular_multa(atraso)

class ServicoNotificacao:
    """Classe responsável apenas por enviar notificações (separando a lógica de negócio)."""
    @staticmethod
    def enviar_email(email: str, mensagem: str):
        print(f"[EMAIL] {email} — {mensagem}")

class SistemaGerenciamento:
    """Classe que gerencia as operações do sistema."""
    def __init__(self):
        # Atributos encapsulados na instância do sistema (sem variáveis globais)
        self.equipamentos = []
        self.emprestimos_registrados = []
        self.notificador = ServicoNotificacao()
        self._proximo_id_emprestimo = 1

    def cadastrar_equipamento(self, equipamento: Equipamento):
        self.equipamentos.append(equipamento)

    def buscar_equipamento(self, id_equipamento: int) -> Equipamento:
        for e in self.equipamentos:
            if e.id == id_equipamento:
                return e
        return None

    def registrar_emprestimo(self, equipamento_id: int, nome_usuario: str, email_usuario: str, dias: int) -> bool:
        equipamento = self.buscar_equipamento(equipamento_id)

        if not equipamento or not equipamento.disponivel:
            print("Equipamento inválido ou indisponível.")
            return False

        usuario = Usuario(nome_usuario, email_usuario)
        emprestimo = Emprestimo(self._proximo_id_emprestimo, equipamento, usuario, dias)
        
        self.emprestimos_registrados.append(emprestimo)
        self._proximo_id_emprestimo += 1
        equipamento.disponivel = False

        self.notificador.enviar_email(usuario.email, f"Empréstimo registrado até {emprestimo.data_devolucao}")
        return True

    def devolver_emprestimo(self, emprestimo_id: int):
        emprestimo = next((e for e in self.emprestimos_registrados if e.id == emprestimo_id), None)

        if not emprestimo or emprestimo.devolvido:
            print("Empréstimo inválido ou já devolvido.")
            return

        hoje = datetime.date.today()
        multa = emprestimo.valor_multa_atual(hoje)

        emprestimo.devolvido = True
        emprestimo.equipamento.disponivel = True

        mensagem_multa = f"Multa de R${multa:.2f}" if multa > 0 else "Devolvido no prazo."
        self.notificador.enviar_email(emprestimo.usuario.email, f"Devolução confirmada. {mensagem_multa}")
        print(f"Devolução registrada. Multa: R${multa:.2f}")

    def listar_atrasados(self):
        hoje = datetime.date.today()
        houve_atraso = False

        for e in self.emprestimos_registrados:
            atraso = e.calcular_atraso(hoje)
            if atraso > 0:
                houve_atraso = True
                multa = e.valor_multa_atual(hoje)
                print(f"{e.usuario.nome} — {atraso} dias de atraso — R${multa:.2f}")
                self.notificador.enviar_email(e.usuario.email, "Você está em atraso!")
        
        if not houve_atraso:
            print("Nenhum empréstimo em atraso.")

def main():
    sistema = SistemaGerenciamento()
    
    # Populando o sistema com as classes específicas
    sistema.cadastrar_equipamento(Notebook(1, "Notebook Dell"))
    sistema.cadastrar_equipamento(Projetor(2, "Projetor Epson"))
    sistema.cadastrar_equipamento(Cabo(3, "Cabo HDMI"))

    while True:
        print("\n--- SISTEMA DE EMPRÉSTIMOS ---")
        print("1- Registrar | 2- Devolver | 3- Atrasados | 0- Sair")
        op = input("Opção: ")
        
        if op == "1":
            try:
                equip_id = int(input("ID equipamento: "))
                nome = input("Nome do usuário: ")
                email = input("Email do usuário: ")
                dias = int(input("Dias de empréstimo: "))
                sistema.registrar_emprestimo(equip_id, nome, email, dias)
            except ValueError:
                print("Por favor, insira valores numéricos válidos para ID e Dias.")
                
        elif op == "2":
            try:
                emp_id = int(input("ID do empréstimo: "))
                sistema.devolver_emprestimo(emp_id)
            except ValueError:
                print("Por favor, insira um ID válido.")
                
        elif op == "3":
            sistema.listar_atrasados()
            
        elif op == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
