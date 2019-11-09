from tkinter import *

janela  = Tk()

janela.title("Show do Yodão")
janela["bg"] = "#051023"

logo = PhotoImage(file="logo.png")
logo = logo.subsample(2, 2)

espaco1 = Label(janela)
espaco2 = Label(janela)
espaco3 = Label(janela)

w = Label(janela, image=logo)
w.logo = logo
espaco1.pack()
espaco1["bg"] = "#051023"
w.pack()
w["pady"] = 10
# participante = Entry(janela)
# participante.place(x=150,y=50)

btJogar = Button(janela,text="Jogar")
btIntrucoes = Button(janela,text="Instruções")


btJogar.place()
btIntrucoes.place()

espaco2.pack()
espaco2["bg"] = "#051023"

btJogar.pack(anchor="center")
btJogar["width"] =10
btJogar["pady"] = 10

espaco3.pack()
espaco3["bg"] = "#051023"

btIntrucoes.pack(anchor="center")
btIntrucoes["width"] =10
btIntrucoes["pady"] = 10

janela.geometry("500x500+200+200")
janela.mainloop()