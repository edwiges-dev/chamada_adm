import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TelaCadastroAluno(ttk.Frame):
    """
    Tela para o cadastro de dados de um aluno.
    Esta classe organiza a criação de todos os widgets e a lógica da tela.
    """
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Cadastro de Alunos")
        self.container.geometry("800x600")
        self.container.minsize(600, 500) # Define um tamanho mínimo

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")

        BG_COLOR = "#f0f0f0" # Um cinza bem claro e neutro
        self.style.configure("TFrame", background=BG_COLOR)
        self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        # --- Layout Responsivo ---
        # Faz o frame principal se expandir com a janela
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.configure(style="TFrame")

        # Chama o método que cria e posiciona todos os widgets
        self._criar_widgets()

    def _criar_widgets(self):
        """
        Cria e organiza todos os widgets (labels, entries, button) na tela.
        """
        # --- Configuração do Grid Interno para Centralização ---
        # Colunas 0 e 3 são espaçadores invisíveis que empurram o conteúdo para o centro.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0) # Coluna dos labels
        self.grid_columnconfigure(2, weight=1) # Coluna dos entries (com peso para expandir)
        self.grid_columnconfigure(3, weight=1)

        # --- Título ---
        titulo = ttk.Label(self, text="Dados do Aluno", style="Title.TLabel")
        titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

        # --- Campos do Formulário ---
        # Lista com todos os campos que queremos no formulário.
        # Adicionar ou remover um campo aqui é tudo que você precisa fazer!
        campos_formulario = [
            "Nome do Aluno:", "CPF:", "Telefone:", "E-mail:", "Matrícula:"
        ]

        # Loop para criar cada label e entry de forma automática
        for i, texto_label in enumerate(campos_formulario):
            linha_atual = i + 1

            label = ttk.Label(self, text=texto_label)
            label.grid(row=linha_atual, column=1, padx=(0, 10), pady=5, sticky="w")

            entry = ttk.Entry(self, width=40)
            entry.grid(row=linha_atual, column=2, pady=5, sticky="ew")

            # Guarda uma referência ao entry para poder pegar o valor depois.
            nome_variavel = "entry_" + texto_label.lower().replace(" ", "_").replace(":", "")
            setattr(self, nome_variavel, entry)

        # --- Botão de Cadastro ---
        linha_botao = len(campos_formulario) + 1
        botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_aluno)
        botao_cadastrar.grid(row=linha_botao, column=1, columnspan=2, pady=(30, 20), sticky="ew")

    def cadastrar_aluno(self):
        """
        Função chamada quando o botão 'Cadastrar' é pressionado.
        Coleta os dados de todos os campos e os imprime.
        """
        print("--- Dados do Aluno Cadastrado ---")

        # Exemplo de como pegar os valores dos campos:
        nome_aluno = self.entry_nome_do_aluno.get()
        cpf_aluno = self.entry_cpf.get()

        print(f"Nome: {nome_aluno}")
        print(f"CPF: {cpf_aluno}")
        print("---------------------------------")
        # Aqui viria a lógica para salvar os dados em um banco de dados.
        
    def cadastrar_curso(self):
        """
        Coleta os dados do curso, valida, salva (simulação) e dá feedback ao usuário.
        """
        # 1. Coletar dados de todos os campos
        dados_curso = {}
        for nome, entry in self.entries.items():
            dados_curso[nome] = entry.get()

        # 2. Validação simples (pode ser expandida)
        if not all(dados_curso.values()):
            self.mostrar_mensagem("Por favor, preencha todos os campos.")
            return

        # 3. Simulação de salvamento (aqui você integraria com seu banco de dados)
        print("Curso cadastrado com sucesso:", dados_curso)

        # 4. Feedback ao usuário
        self.mostrar_mensagem("Curso cadastrado com sucesso!")
    
    def mostrar_mensagem(self, mensagem):
        """
        Exibe uma mensagem de feedback ao usuário.
        """
        messagebox.showinfo("Informação", mensagem)

    def _limpar_campos(self):
        """
        Limpa o texto de todos os campos de entrada (Entry).
        """
        for entry in self.entries.values():
            entry.delete(0, tk.END) 
    

if __name__ == "__main__":
    # Cria a janela principal da aplicação
    root = tk.Tk()
    # Cria a nossa tela de cadastro dentro da janela principal
    app = TelaCadastroAluno(root)
    # Inicia o loop principal da aplicação
    root.mainloop()

