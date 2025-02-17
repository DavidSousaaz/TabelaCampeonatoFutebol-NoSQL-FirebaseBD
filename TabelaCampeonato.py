import firebase_admin
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from firebase_admin import credentials, db
import sys

# Caminho para o arquivo JSON da chave privada
cred = credentials.Certificate(r"Digite o diretorio do arquivo aqui!!")

# Inicializar o Firebase com as credenciais
firebase_admin.initialize_app(cred, {
    'databaseURL': 'URL do seu firebase!!'
})

# Referência para a tabela "times"
ref = db.reference("times")


class TabelaClassificacao(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Classificação do Campeonato")
        self.setGeometry(100, 100, 800, 800)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # Criando a tabela
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Sigla (ID)", "Nome", "Vitórias", "Empates", "Derrotas", "Pontos"])

        # Estilizando
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f4f4f4;
                color: #333;
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                border: 1px solid #ddd;
            }
            QTableWidget::item:selected {
                background-color: #c2d3f7;
            }
            QHeaderView::section {
                background-color: #005288;
                color: white;
                font-weight: bold;
                padding: 10px;
            }
        """)

        # Adicionando a tabela ao layout
        layout.addWidget(self.table)
        central_widget.setLayout(layout)

        # Atualiza a tabela ao iniciar
        self.atualizar_tabela()

    def atualizar_tabela(self):
        """Atualiza a exibição da tabela com os dados do Firebase"""
        times = ref.get()

        if not times:
            self.table.setRowCount(0)
            return

        times_ordenados = sorted(times.items(), key=lambda x: (-x[1]['pontos'], -x[1]['vitorias']))

        self.table.setRowCount(len(times_ordenados))

        for i, (sigla, value) in enumerate(times_ordenados):
            self.table.setItem(i, 0, QTableWidgetItem(str(sigla)))
            self.table.setItem(i, 1, QTableWidgetItem(value["nome"]))
            self.table.setItem(i, 2, QTableWidgetItem(str(value["vitorias"])))
            self.table.setItem(i, 3, QTableWidgetItem(str(value["empates"])))
            self.table.setItem(i, 4, QTableWidgetItem(str(value["derrotas"])))
            self.table.setItem(i, 5, QTableWidgetItem(str(value["pontos"])))





def atualizar_pontuacao():
    times = ref.get()
    if not times:
        print("\nNenhuma equipe cadastrada para atualizar!\n")
        return

    sigla = input("Digite a SIGLA do time para atualizar a pontuação: ").upper()

    if sigla not in times:
        print("\nSIGLA não encontrada!\n")
        return

    resultado = input("O time teve (V)itória, (E)mpate ou (D)errota? ").strip().upper()

    if resultado not in ['V', 'E', 'D']:
        print("\nOpção inválida!\n")
        return

    time_ref = ref.child(sigla)
    dados_time = times[sigla]

    if resultado == 'V':
        dados_time['vitorias'] += 1
        dados_time['pontos'] += 3
    elif resultado == 'E':
        dados_time['empates'] += 1
        dados_time['pontos'] += 1
    elif resultado == 'D':
        dados_time['derrotas'] += 1

    time_ref.update(dados_time)
    print("\nPontuação atualizada com sucesso!\n")






def adicionar_equipe():
    sigla = input("Digite uma SIGLA para a equipe (ex: FLA, PAL, COR): ").strip().upper()

    if not sigla or len(sigla) > 5:
        print("\nSigla inválida! Deve ter no máximo 5 caracteres.\n")
        return

    times = ref.get() or {}

    if sigla in times:
        print("\nEssa sigla já está em uso! Escolha outra.\n")
        return

    nome = input("Digite o nome da equipe: ").strip()

    if not nome:
        print("\nNome inválido!\n")
        return

    ref.child(sigla).set({
        "nome": nome,
        "vitorias": 0,
        "empates": 0,
        "derrotas": 0,
        "pontos": 0
    })

    print("\nEquipe adicionada com sucesso!\n")






def remover_equipe():
    times = ref.get()
    if not times:
        print("\nNenhuma equipe cadastrada para remover!\n")
        return

    sigla = input("Digite a SIGLA do time que deseja remover: ").upper()

    if sigla not in times:
        print("\nSIGLA não encontrada!\n")
        return

    ref.child(sigla).delete()
    print("\nEquipe removida com sucesso!\n")





def menu():

    app = QApplication(sys.argv)
    tabela_window = TabelaClassificacao()

    while True:
        print("\n--- MENU ---")
        print("1 - Exibir Classificação")
        print("2 - Atualizar Pontuação")
        print("3 - Adicionar Equipe")
        print("4 - Remover Equipe")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nAbrindo tabela de classificação...\n")
            tabela_window.atualizar_tabela()
            tabela_window.showMaximized()
            app.exec_()
        elif opcao == '2':
            atualizar_pontuacao()
        elif opcao == '3':
            adicionar_equipe()
        elif opcao == '4':
            remover_equipe()
        elif opcao == '5':
            print("\nSaindo...\n")
            sys.exit(0)
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    menu()
