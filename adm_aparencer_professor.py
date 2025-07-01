import tkinter as tk
from tkinter import ttk 

class Aparencer:
    def __init__(self, root):
        self.root = root
        self.root.title("Aparencer")
        self.root.geometry("1080x720")

        # Create a style object
        self.style = ttk.Style()

        # Configure the style for the main window
        self.style.configure("TFrame", background="lightblue")
        self.style.configure("TButton", background="lightgreen", foreground="black")

        # Create a frame with the configured style
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="nome da pessoal admitrativa do banco de dados  ", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Nome do professor", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)    
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="CPF", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)    
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Telefone", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)    
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="E-mail", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)    
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Matricula", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)    
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 1", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 2", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 3", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 4", font=("Arial", 16))
        self.label.pack(pady=20) 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)
        
        # Add a button to the frame
        self.button = ttk.Button(self.frame, text="Cadastrar", command=lambda: print("Cadastrado!"))
        self.button.pack(pady=20)
        
           
        
        
        
        
        
        
        
        
        
        
root = tk.Tk()
app = Aparencer(root)
root.mainloop()
