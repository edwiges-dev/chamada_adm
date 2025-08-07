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
        self.dados_cursos()
        # Create a frame with the configured style
        # self.frame = ttk.Frame(root)
        # self.frame.grid(row=0, column=0, sticky="nsew")
        # self.style.configure("TFrame", background="red")

        
       

    def dados_cursos(self):

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.style.configure("TFrame", background="red")

    
        label_titulo = ttk.Label(self.frame, text="Titulo da pagina ",bg="red", anchor="center", font=("Arial", 16))
        label_titulo.grid(row=0, column=0, sticky="ew") 

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

if __name__ == "__main__":
    root = tk.Tk() # Create the main Tkinter window
    app = cadastrar_curso(root) # Instantiate the Aparencer application
    root.mainloop()