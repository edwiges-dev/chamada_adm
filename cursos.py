import tkinter as tk
from tkinter import ttk

class cadastrar_curso(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Aparencer")
        self.root.geometry("1080x720") # Set initial window size

        # Create a style object for consistent widget appearance
        self.style = ttk.Style()

        # Configure the style for the main frame, buttons, and labels
        self.style.configure("TFrame", background="lightblue")
        self.style.configure("TButton", background="lightgreen", foreground="black", font=("Arial", 14), padding=10)
        self.style.configure("TLabel", background="darkred",fg="white", font=("Arial", 16)) # Ensure labels have consistent background and font

        # Create a main frame that will hold all content
        # This frame is placed in the root window and will expand to fill it
        self.frame = ttk.Frame(self.root, padding=20) # Added padding around the content
        self.frame.grid(row=0, column=0, sticky="nsew") # Make the frame expand with the root window
        self.frame.configure(style="TFrame") # Apply the defined style

        # Configure the root window's grid to make the frame expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.dados_cursos()
        
        
       

    def dados_cursos(self):

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.style.configure("TFrame", background="darkred",fg="white")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1) # Left padding column
        self.frame.grid_columnconfigure(1, weight=0) # Labels column (content-sized, no extra weight)
        self.frame.grid_columnconfigure(2, weight=0) # Entries column (content-sized, no extra weight)
        self.frame.grid_columnconfigure(3, weight=1)


    
        self.admin_label = ttk.Label(self.frame, text="titulo da pagina", anchor="center")
        self.admin_label.grid(row=1, column=1, columnspan=2, pady=(0, 20), sticky="ew")

        # self.label = ttk.Label(self.frame, text="nome da pessoal administrativa do banco de dados", anchor="center", font=("Arial", 16))
        # self.label.grid(row=1, column=0, sticky="ew") 
    
        self.label_curso = ttk.Label(self.frame, text="Nome do curso:")
        self.label_curso.grid(row=2, column=1, pady=10, padx=20, sticky="w") 
        self.entry_curso = ttk.Entry(self.frame, width=40) 
        self.entry_curso.grid(row=2, column=2, pady=10, padx=20, sticky="ew")
    
        self.label_codigo = ttk.Label(self.frame, text="codigo do curso:")
        self.label_codigo.grid(row=3, column=1, pady=10, padx=20, sticky="w") 
        self.entry_codigo = ttk.Entry(self.frame, width=40) 
        self.entry_codigo.grid(row=3, column=2, pady=10, padx=20, sticky="ew")

        self.label_carga_horaria = ttk.Label(self.frame, text="Carga horaria do curso:")
        self.label_carga_horaria.grid(row=4, column=1, pady=10, padx=20, sticky="w") 
        self.entry_carga_horaria = ttk.Entry(self.frame, width=40) 
        self.entry_carga_horaria.grid(row=4, column=2, pady=10, padx=20, sticky="ew")

        self.label_data_inicio = ttk.Label(self.frame, text="data de inicio do curso:")
        self.label_data_inicio.grid(row=5, column=1, pady=10, padx=20, sticky="w") 
        self.entry_data_inicio = ttk.Entry(self.frame, width=40) 
        self.entry_data_inicio.grid(row=5, column=2, pady=10, padx=20, sticky="ew")

        self.label_data_fim = ttk.Label(self.frame, text="data de fim do curso:")
        self.label_data_fim.grid(row=6, column=1, pady=10, padx=20, sticky="w") 
        self.entry_data_fim = ttk.Entry(self.frame, width=40) 
        self.entry_data_fim.grid(row=6, column=2, pady=10, padx=20, sticky="ew")

        self.label_tipo_curso = ttk.Label(self.frame, text="tipo do curso:")
        self.label_tipo_curso.grid(row=7, column=1, pady=10, padx=20, sticky="w") 
        self.entry_tipo_curso = ttk.Entry(self.frame, width=40) 
        self.entry_tipo_curso.grid(row=7, column=2, pady=10, padx=20, sticky="ew")

        self.label_modalidade = ttk.Label(self.frame, text="modalidade do curso:")
        self.label_modalidade.grid(row=8, column=1, pady=10, padx=20, sticky="w") 
        self.entry_modalidade = ttk.Entry(self.frame, width=40) 
        self.entry_modalidade.grid(row=8, column=2, pady=10, padx=20, sticky="ew")

        self.label_turno = ttk.Label(self.frame, text="turno do curso:")
        self.label_turno.grid(row=9, column=1, pady=10, padx=20, sticky="w") 
        self.entry_turno = ttk.Entry(self.frame, width=40) 
        self.entry_turno.grid(row=9, column=2, pady=10, padx=20, sticky="ew")




        self.button = ttk.Button(self.frame, text="Cadastrar", command=lambda: print("Cadastrado!"))
        self.button.grid(row=10, column=1, columnspan=2, pady=(20,0), sticky="ew")

        self.frame.grid_rowconfigure(12, weight=1) 
if __name__ == "__main__":
    root = tk.Tk() # Create the main Tkinter window
    app = cadastrar_curso(root) # Instantiate the Aparencer application
    root.mainloop()