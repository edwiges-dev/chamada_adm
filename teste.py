import tkinter as tk
from tkinter import ttk

class Aparencer:
    def __init__(self, root):
        self.root = root
        self.root.title("Aparencer")
        self.root.geometry("1080x720") # Set initial window size

        # Create a style object for consistent widget appearance
        self.style = ttk.Style()

        # Configure the style for the main frame, buttons, and labels
        self.style.configure("TFrame", background="lightblue")
        self.style.configure("TButton", background="lightgreen", foreground="black", font=("Arial", 14), padding=10)
        self.style.configure("TLabel", background="lightblue", font=("Arial", 16)) # Ensure labels have consistent background and font

        # Create a main frame that will hold all content
        # This frame is placed in the root window and will expand to fill it
        self.frame = ttk.Frame(self.root, padding=20) # Added padding around the content
        self.frame.grid(row=0, column=0, sticky="nsew") # Make the frame expand with the root window
        self.frame.configure(style="TFrame") # Apply the defined style

        # Configure the root window's grid to make the frame expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Configure the frame's internal grid to centralize content
        # Column 0 and Column 3 are "padding" columns that will expand
        # Column 1 is for labels, Column 2 is for entry fields
        self.frame.grid_columnconfigure(0, weight=1) # Left padding column
        self.frame.grid_columnconfigure(1, weight=0) # Labels column (content-sized, no extra weight)
        self.frame.grid_columnconfigure(2, weight=0) # Entries column (content-sized, no extra weight)
        self.frame.grid_columnconfigure(3, weight=1) # Right padding column

        # Row 0 is a "padding" row that will expand to push content down
        self.frame.grid_rowconfigure(0, weight=1)

        # Main title label for the administrative personnel
        # It spans columns 1 and 2 to be centered above the form fields
        self.admin_label = ttk.Label(self.frame, text="Nome da Pessoal Administrativa do Banco de Dados", anchor="center")
        self.admin_label.grid(row=1, column=1, columnspan=2, pady=(0, 20), sticky="ew") # pady for spacing below title

        # --- Form Fields ---

        # Nome do Aluno (Student Name)
        self.label_nome = ttk.Label(self.frame, text="Nome do Aluno:")
        self.label_nome.grid(row=2, column=1, pady=10, padx=20, sticky="w") # Aligns label to the west (left)
        self.entry_nome = ttk.Entry(self.frame, width=40) # Increased width for entries
        self.entry_nome.grid(row=2, column=2, pady=10, padx=20, sticky="ew") # Expands entry horizontally

        # CPF (Brazilian Individual Taxpayer Registry)
        self.label_cpf = ttk.Label(self.frame, text="CPF:")
        self.label_cpf.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        self.entry_cpf = ttk.Entry(self.frame, width=40)
        self.entry_cpf.grid(row=3, column=2, pady=10, padx=20, sticky="ew")

        # Telefone (Phone Number)
        self.label_telefone = ttk.Label(self.frame, text="Telefone:")
        self.label_telefone.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        self.entry_telefone = ttk.Entry(self.frame, width=40)
        self.entry_telefone.grid(row=4, column=2, pady=10, padx=20, sticky="ew")

        # E-mail
        self.label_email = ttk.Label(self.frame, text="E-mail:")
        self.label_email.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        self.entry_email = ttk.Entry(self.frame, width=40)
        self.entry_email.grid(row=5, column=2, pady=10, padx=20, sticky="ew")

        # Matrícula (Enrollment Number)
        self.label_matricula = ttk.Label(self.frame, text="Matrícula:")
        self.label_matricula.grid(row=6, column=1, pady=10, padx=20, sticky="w")
        self.entry_matricula = ttk.Entry(self.frame, width=40)
        self.entry_matricula.grid(row=6, column=2, pady=10, padx=20, sticky="ew")

        # Cadastrar Button (Register Button)
        # Spans columns 1 and 2 to be centered below the form fields
        self.button = ttk.Button(self.frame, text="Cadastrar", command=lambda: print("Cadastrado!"))
        self.button.grid(row=7, column=1, columnspan=2, pady=(20, 0), sticky="ew") # pady for spacing above button

        # Row after the button will be empty and expand to push content up
        self.frame.grid_rowconfigure(8, weight=1)

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk() # Create the main Tkinter window
    app = Aparencer(root) # Instantiate the Aparencer application
    root.mainloop() # Start the Tkinter event loop