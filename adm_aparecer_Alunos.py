import tkinter as tk
from tkinter import ttk 

class Aparencer:
    def __init__(self, root):
        self.root = root
        self.root.title("Aparencer")
        self.root.geometry("1080x720")
        

        # Create a style object
        self.style = ttk.Style()

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


        # Create a frame with the configured style
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.style.configure("TFrame", background="red")

        
       

        
        self.label = ttk.Label(self.frame, text="nome da pessoal administrativa do banco de dados", anchor="center", font=("Arial", 16))
        self.label.grid(row=0, column=0, sticky="ew") 
        
        # # Add a text entry field to the frame
        
        # # Add a label to the frame
        # self.label = ttk.Label(self.frame, text="Nome do Alunos", font=("Arial", 16))
        # self.label.pack(pady=20) 
        
        # # Add a text entry field to the frame
        # self.entry = ttk.Entry(self.frame, width=30)
        # self.entry.pack(pady=10)    
         
        # # Add a label to the frame
        # self.label = ttk.Label(self.frame, text="CPF", font=("Arial", 16))
        # self.label.pack(pady=20) 
        
        # # Add a text entry field to the frame
        # self.entry = ttk.Entry(self.frame, width=30)
        # self.entry.pack(pady=10)    
         
        # # Add a label to the frame
        # self.label = ttk.Label(self.frame, text="Telefone", font=("Arial", 16))
        # self.label.pack(pady=20) 
        
        # # Add a text entry field to the frame
        # self.entry = ttk.Entry(self.frame, width=30)
        # self.entry.pack(pady=10)    
         
        # # Add a label to the frame
        # self.label = ttk.Label(self.frame, text="E-mail", font=("Arial", 16))
        # self.label.pack(pady=20) 
        
        # # Add a text entry field to the frame
        # self.entry = ttk.Entry(self.frame, width=30)
        # self.entry.pack(pady=10)    
         
        # # Add a label to the frame
        # self.label = ttk.Label(self.frame, text="Matricula", font=("Arial", 16))
        # self.label.pack(pady=20) 
        
        # # Add a text entry field to the frame
        # self.entry = ttk.Entry(self.frame, width=30)
        # self.entry.pack(pady=10)    
        
        # # Add a button to the frame
        # self.button = ttk.Button(self.frame, text="Cadastrar", command=lambda: print("Cadastrado!"))
        # self.button.pack(pady=20)
        
           
        
        
        
        
        
        
        
        
        
        
root = tk.Tk()
app = Aparencer(root)
root.mainloop()
