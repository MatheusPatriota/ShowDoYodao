import tkinter as tk
from platform import python_version


root = tk.Tk()

logo = tk.PhotoImage(file="logo.png")
btJogar = tk.Button(root,text="Jogar")
btIntrucoes = tk.Button(root,text="Instruções")

logo.grid(row=0,column=0, padx= 10, pady=10)
btJogar.grid(row=1,column=1,padx= 10, pady=10)
btIntrucoes.grid(row=2,column=2,padx= 10, pady=10)

root.mainloop()
