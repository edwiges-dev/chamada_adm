import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TelaCadastroProfessor(ttk.Frame):
    """
    Tela para o cadastro de dados de um professor.
    A classe organiza a criação de todos os widgets e a lógica da tela.
    """
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # --- Configuração da Janela Principal ---
        self.container.title("Cadastro de Professores")
        self.container.geometry("1080x720")
        self.container.minsize(700, 550) # Tamanho mínimo ajustado

        # --- Configuração de Estilos ---
        self.style = ttk.Style(self.container)
        self.style.theme_use("clam")

        BG_COLOR = "#e0e8f0" # Um azul acinzentado claro
        self.style.configure("TFrame", background=BG_COLOR)
        self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 18, "bold"))
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)
        # Adicionado estilo para o Combobox para manter a consistência
        self.style.configure("TCombobox", font=("Arial", 12), padding=5)

        # --- Layout Responsivo ---
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.configure(style="TFrame")

        # Chama o método que cria e posiciona todos os widgets
        self._criar_widgets()

    def _criar_widgets(self):
        """
        Cria e organiza todos os widgets (labels, entries, combobox, button) na tela.
        """
        # --- Configuração do Grid Interno para Centralização ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0) # Coluna dos labels
        self.grid_columnconfigure(2, weight=1) # Coluna dos widgets de entrada
        self.grid_columnconfigure(3, weight=1)

        # --- Título ---
        titulo = ttk.Label(self, text="Cadastro de Pessoal Administrativo", style="Title.TLabel")
        titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

        # --- Campos do Formulário ---
        # *** ALTERAÇÃO 1: Atualizamos a lista de campos. ***
        # Removemos os 4 campos de curso e adicionamos um único campo "Curso".
        campos_formulario = [
            "Nome do Professor:", "CPF:", "Telefone:", "email:", "Matrícula:", "Cursos:"
        ]

        # Lista de opções para o nosso Combobox
        opcoes_cursos = ["Cursos 1", "Cursos 2", "Cursos 3", "Cursos 4", "Cursos 5"]

        # Loop para criar cada label e widget de entrada
        for i, texto_label in enumerate(campos_formulario):
            linha_atual = i + 1

            label = ttk.Label(self, text=texto_label)
            label.grid(row=linha_atual, column=1, padx=(0, 10), pady=5, sticky="w")
            
            # Transforma o texto do label em um nome de variável para o widget
            # Ex: "Nome do Professor:" vira "entry_nome_do_professor"
            nome_variavel = "widget_" + texto_label.lower().replace(" ", "_").replace(":", "")

            # *** ALTERAÇÃO 2: Criar Combobox para o campo "Cursos" e Entry para os outros. ***
            if texto_label == "Cursos:":
                # Cria o Combobox
                combobox = ttk.Combobox(self, values=opcoes_cursos, state="readonly", width=38)
                combobox.grid(row=linha_atual, column=2, pady=5, sticky="ew")
                # Armazena a referência do Combobox
                setattr(self, nome_variavel, combobox)
            else:
                # Cria o Entry para todos os outros campos
                entry = ttk.Entry(self, width=40)
                entry.grid(row=linha_atual, column=2, pady=5, sticky="ew")
                # Armazena a referência do Entry
                setattr(self, nome_variavel, entry)

        # --- Botão de Cadastro ---
        linha_botao = len(campos_formulario) + 1
        botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_professor)
        botao_cadastrar.grid(row=linha_botao, column=1, columnspan=2, pady=(30, 20), sticky="ew")

    def cadastrar_professor(self):
        """
        Coleta os dados dos campos, valida e simula o cadastro.
        """
        # *** ALTERAÇÃO 3: Atualizamos a coleta de dados. ***
        # Coleta os dados de todos os campos
        dados_professor = {
            "nome": self.widget_nome_do_professor.get(),
            "cpf": self.widget_cpf.get(),
            "telefone": self.widget_telefone.get(),
            "email": self.widget_email.get(),
            "matricula": self.widget_matricula.get(),
            "cursos": self.widget_curso.get() # Pega o valor do Combobox
        }

        # Validação simples: Verifica se o nome, CPF e curso estão preenchidos
        if not dados_professor["nome"] or not dados_professor["cpf"]:
            self._mostrar_notificacao("Nome e CPF são obrigatórios!", "Error")
            return
        
        if not dados_professor["cursos"]:
            self._mostrar_notificacao("Por favor, selecione um curso!", "Error")
            return

        # Simulação de cadastro
        print("--- Dados do Professor para Salvar ---")
        for campo, valor in dados_professor.items():
            print(f"{campo.replace('_', ' ').title()}: {valor}")
        print("---------------------------------")

        # Feedback ao usuário e limpeza dos campos
        self._mostrar_notificacao("Professor cadastrado com sucesso!", "Success")
        self._limpar_campos()
        
    def _mostrar_notificacao(self, mensagem, tipo):
        """
        Exibe uma mensagem para o usuário.
        'tipo' pode ser "Success" ou "Error".
        """
        if tipo == "Success":
            messagebox.showinfo("Sucesso", mensagem)
        elif tipo == "Error":
            messagebox.showerror("Erro", mensagem)
        
    def _limpar_campos(self):
        """
        Limpa o texto de todos os campos de entrada (Entry e Combobox).
        """
        # *** ALTERAÇÃO 4: Atualizamos a lista de campos para limpar. ***
        campos_para_limpar = [
            "nome_do_professor", "cpf", "telefone", "email", "matricula"
        ]
        
        for campo in campos_para_limpar:
            widget = getattr(self, f"widget_{campo}", None)
            if widget:
                widget.delete(0, tk.END)

        # Limpa a seleção do Combobox
        self.widget_curso.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroProfessor(root)
    root.mainloop()
    