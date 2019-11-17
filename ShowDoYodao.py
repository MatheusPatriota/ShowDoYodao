from tkinter import *
from future.moves.tkinter import scrolledtext
from PIL import Image, ImageTk
import pygame
import os
import cv2
import time
import sys
import  random
import tkinter.scrolledtext as tkst
import tkinter.messagebox as tkmsg

class Interface:

    # =============================== logica de sorteio de perguntas ==========================================
    def logicaSorteioPerguntas(self):   

        self.perguntas = os.listdir('Perguntas')
        self.aux = []

        for i in self.perguntas:
            self.arquivo = open('Perguntas/'+i,"r")
            self.aux.append(self.arquivo.readlines())


        for indice,linha in enumerate(self.aux):
            self.aux[indice] = self.removeQuebraLinha(linha)

        self.perguntasFaceis = []
        self.perguntasDificeis = []
        self.perguntasMedias = []
        self.perguntasFinais = []

        # encontra e insere as perguntas de acordo com seu grau de dificuladade
        for i in self.aux:
            if i[0] == '0':
                self.perguntasFaceis.append(i)
            elif i[0] == '1':
                self.perguntasMedias.append(i)
            elif i[0] == '2':
                self.perguntasDificeis.append(i)
            else:
                self.perguntasFinais.append(i)


        self.perguntasFaceisSelecionadas = []
        self.perguntasDificeisSelecionadas = []
        self.perguntasMediasSelecionadas = []
        self.perguntasFinalSelecionada = []

        self.sorteiaQuestoes(self.perguntasFaceis,self.perguntasFaceisSelecionadas)
        self.sorteiaQuestoes(self.perguntasMedias,self.perguntasMediasSelecionadas)
        self.sorteiaQuestoes(self.perguntasDificeis,self.perguntasDificeisSelecionadas)
        self.perguntasFinalSelecionada.append(random.choice(self.perguntasFinais))


    # ==================================== Remover \n das strings ===========================
    def removeQuebraLinha(self, lista):   
        for i in range(len(lista)):
            lista[i] = lista[i].replace('\n',"")
        return lista

    #  ================================== Sortear as questões ==============================
    def sorteiaQuestoes(self, lista1,lista2):
        for i in range(5):
            selecionado = random.choice(lista1)
            while selecionado in lista2:
                selecionado = random.choice(lista1)
            lista2.append(selecionado)

    def __init__(self,tela):
        
        pygame.mixer.music.load("Audios/trilha.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
        
        op = open('Participantes/participantesOrdenados.txt','r')
        op = op.readlines()
        op = op[0].split("-")

        self.logicaSorteioPerguntas()

        self.acertos = 0
        self.maiorPontuacao = int(op[1])
        self.pontuacao = 0
        self.telaInicial = tela
        self.telaInicial.title("Show do Yodão")
        self.frame1 = Frame(tela)
        self.frame2 = Frame(tela)
        self.frame3 = Frame(tela)
        self.frame4 = Frame(tela)
        self.frame5 = Frame(tela)
       
        self.frame1['bg'] = "#051023"
        self.frame2['bg'] = "#051023"
        self.frame3['bg'] = "#051023"
        self.frame4['bg'] = "#051023"
        self.frame5['bg'] = "#051023"

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        
        image = Image.open("Imagens/logo.png")
        image = image.resize((400, 250), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image)
        
        self.label = Label(self.frame1, image=photo)
        self.label.image = photo
        self.label.grid(row=2, column=0)
        self.label.pack(padx=10,pady=10)
       
        self.btJogar = Button(self.frame2,text="Jogar",command=self.particpante)
        self.btIntrucoes = Button(self.frame3,text="Instruções", command=self.instrucoes)
        self.btRank = Button(self.frame4,text="Rank", command=self.ranking)
        self.btSair = Button(self.frame5,text="Sair",command= self.sair)

        self.btJogar.pack(padx=5, pady=7)
        self.btJogar["width"] = 10
        self.btIntrucoes.pack(padx=5, pady=7)
        self.btIntrucoes["width"] =10
        self.btRank.pack(padx=5, pady=7)
        self.btRank["width"] = 10
        self.btSair.pack(padx=5, pady=7)
        self.btSair["width"] =10

    def sair(self):
        self.telaInicial.destroy()

    # ============================================= Participante ============================================

    def particpante(self):

        self.telaInicial.destroy()

        self.telaParticipante = Tk()
        self.telaParticipante.title("Informe o nome do participante")
        self.telaParticipante["bg"] = "#051023"

        self.btEntrar = Button(self.telaParticipante, text='Entrar', command=self.pergunta)
        self.nomeParticipante = Entry(self.telaParticipante)
        
        self.nomeParticipante.pack(padx=5,pady=5,side=LEFT)
        self.btEntrar.pack(padx=5,pady=5,side=LEFT)
        self.cond = True

        self.telaParticipante.mainloop()


    # ============================================= Perguntas ==============================================
    def pergunta(self):

        if self.cond == True:
            self.participante = self.nomeParticipante.get()
            self.telaParticipante.destroy()
            self.cond = False

        self.telaPergunta = Tk()
        self.telaPergunta.title("Responda a Pergunta")
        self.telaPergunta["bg"] = "#051023"
        
        if self.acertos== 0 or self.acertos== 5 or self.acertos== 10 or self.acertos== 15 or self.acertos== 16:
            self.apontador = 0
            
        if self.acertos >= 0 and self.acertos< 5:
            self.perg = self.perguntasFaceisSelecionadas[self.apontador][1]
            self.alternativas = self.perguntasFaceisSelecionadas[self.apontador][2:6]
            self.resposta = self.perguntasFaceisSelecionadas[self.apontador][6]
            del(self.perguntasFaceisSelecionadas[self.apontador])
        elif self.acertos>= 5 and self.acertos< 10:
            self.perg = self.perguntasMediasSelecionadas[self.apontador][1]
            self.alternativas = self.perguntasMediasSelecionadas[self.apontador][2:6]
            self.resposta = self.perguntasMediasSelecionadas[self.apontador][6]
            del(self.perguntasMediasSelecionadas[self.apontador])
        elif self.acertos>= 10 and self.acertos< 15:
            self.perg = self.perguntasDificeisSelecionadas[self.apontador][1]
            self.alternativas = self.perguntasDificeisSelecionadas[self.apontador][2:6]
            self.resposta = self.perguntasDificeisSelecionadas[self.apontador][6]
            del(self.perguntasDificeisSelecionadas[self.apontador])
        else:
            self.perg = self.perguntasFinalSelecionada[self.apontador][1]
            self.alternativas = self.perguntasFinalSelecionada[self.apontador][2:6]
            self.resposta = self.perguntasFinalSelecionada[self.apontador][6]
            del(self.perguntasFinalSelecionada[self.apontador])


        # =================================================== botoes e labels =====================================
        
        self.labelPergunta = Label(self.telaPergunta)
        self.labelPergunta['text'] = self.perg
        self.labelPergunta.pack()

        self.btResponder = Button(self.telaPergunta,text="Responder",command=self.responder)
        # self.btParar = Button(self.telaPergunta,text="Parar")

        self.MODES = [
        (self.alternativas[0], "1"),
        (self.alternativas[1], "2"),
        (self.alternativas[2], "3"),
        (self.alternativas[3], "4"),
        ]

        self.v = StringVar()
        self.v.set("A") # initialize

        for text, mode in self.MODES:
            self.b = Radiobutton(self.telaPergunta, text=text,
                            variable=self.v, value=mode)
            self.b.pack(anchor=W)

        self.btResponder.pack()
        self.telaPergunta.mainloop()


    def responder(self):
        self.resp = self.v.get()
        if self.resp == self.resposta:
            self.acertou()
        else:
            self.errou()


    def acertou(self):
        
        pygame.mixer.music.load("Audios/acertou.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

        self.acertos += 1
        self.pontuacao +=1

        if self.acertos == 16:
            arquivo = open('Participantes/participantes.txt', 'r') # Abra o arquivo (leitura)
            arquivoParticipante = arquivo.readlines()
            arquivoParticipante.append(" " + self.participante + " " + str(self.pontuacao)+ "\n")   # insira seu conteúdo

            arquivo = open('Participantes/participantes.txt', 'w') # Abre novamente o arquivo (escrita)
            arquivo.writelines(arquivoParticipante)    # escreva o conteúdo criado anteriormente nele.

            arquivo.close()

            self.ordenaParticipantes()

            if self.pontuacao >= self.maiorPontuacao:
                result= tkmsg.askquestion(title='Você quebrou o Recorde!!', message='Deseja tirar uma foto?')
                if result == 'yes':
                    sys.exit(self.tirarFotoCampeao(sys.argv))

            # ================== mensagem de saida do programa após fim do jogo ============================
            result= tkmsg.askquestion(title='Deseja Jogar Novamente?', message='Confirma sair do programa?')
            if result == 'yes':
                self.telaPergunta.destroy()
                tela = Tk()
                tela["bg"] = "#051023"
                tela.geometry("500x500+200+200")
                Interface(tela)
                tela.mainloop()
            else:
                self.telaPergunta.destroy()

        self.telaPergunta.destroy()
        self.pergunta()

        
    def errou(self):
        
        pygame.mixer.music.load("Audios/errou.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

        arquivo = open('Participantes/participantes.txt', 'r') # Abra o arquivo (leitura)
        arquivoParticipante = arquivo.readlines()
        arquivoParticipante.append(" " + self.participante + " " + str(self.pontuacao)+ "\n")   # insira seu conteúdo

        arquivo = open('Participantes/participantes.txt', 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(arquivoParticipante)    # escreva o conteúdo criado anteriormente nele.

        arquivo.close()

        self.ordenaParticipantes()

        if self.pontuacao >= self.maiorPontuacao:
            result= tkmsg.askquestion(title='Você quebrou o Recorde!!', message='Deseja tirar uma foto?')
            if result == 'yes':
                sys.exit(self.tirarFotoCampeao(sys.argv))

        # ================== mensagem de saida do programa após fim do jogo ============================
        result= tkmsg.askquestion(title='Deseja Jogar Novamente?', message='Confirma sair do programa?')
        if result == 'yes':
            self.telaPergunta.destroy()
            tela = Tk()
            tela["bg"] = "#051023"
            tela.geometry("500x500+200+200")
            Interface(tela)
            tela.mainloop()
        else:
            self.telaPergunta.destroy()
            
                
    def ordenaParticipantes(self):
        s = open("Participantes/participantes.txt","r")

        participantes = s.read()
        participantes = participantes.split(" ")
        participantes = self.removeQuebraLinha(participantes)
        participantesOrdenados = []

        del participantes[0]


        while len(participantes) != 0:
            maior = 0
            indiceMaior = 0
            for i in range(len(participantes)):
                if not(i % 2 == 0):
                    if int(participantes[i]) >= maior :
                        maior = int(participantes[i])
                        indiceMaior = i
            
            participantesOrdenados.append(participantes[indiceMaior-1] + " - " + participantes[indiceMaior]) 
            del participantes[indiceMaior]
            del participantes[indiceMaior-1]


        # escrevendo os participantes ordenados
        so = open("Participantes/participantesOrdenados.txt","w")
        for  i in participantesOrdenados:
            so.write(i + "\n")

        so.close()  
    # ============================================= Rank ===========================================
    def exibeFotoCampeao(self):
        self.ftc = Toplevel()
        self.ftc.title("Foto Campeão")
        self.ftc["bg"] = "#051023"
        self.ftc.geometry("700x500+200+200")
        
        self.image = Image.open("Imagens/Campeao.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(self.ftc, image=self.photo)
        self.label.image = self.photo
        self.label.grid(row=2, column=0)
        self.label.pack()

        self.ftc.mainloop()

    def ranking(self):
        
        self.rankTk = Tk()
        self.rankTk.title("Ranking")
        self.rankTk["bg"] = "#051023"
        self.rankTk.geometry("700x500+200+200")

        # participantes
        self.textParticipantes = scrolledtext.ScrolledText(self.rankTk,width=30,height=15)

        # area Campeao
        self.labelCampeao = Label(self.rankTk,text="Campeão: ")
        self.nomeCampeao = Label(self.rankTk)
        self.btCampeao = Button(self.rankTk,text="Visualizar Foto",command=self.exibeFotoCampeao)

        self.so = open("Participantes/participantesOrdenados.txt","r")
        self.so = self.so.readlines()
        self.nc = self.so[0]
        self.nc = self.nc.split('-')
        self.nomeCampeao['text'] = self.nc[0]

        for i in self.so:
            self.textParticipantes.insert(INSERT,i)
        
        self.textParticipantes.pack(padx=10, pady=0,side=LEFT)
        self.labelCampeao.pack(padx=5, pady=15,side=LEFT)
        self.nomeCampeao.pack(padx=5, pady=15,side=LEFT)
        self.btCampeao.pack()
        
        self.rankTk.mainloop()


    # ============================================= Instruções ===========================================
    def instrucoes(self):  
     
        self.instrucoesTk = Tk()
        self.instrucoesTk.title("Instruções")
        self.instrucoesTk["bg"] = "#051023"

        # texto explicacao
        self.texto = scrolledtext.ScrolledText(self.instrucoesTk,width=70,height=7)
        self.texto.insert(INSERT, "O programa consiste em três rodadas e uma pergunta final:\n" )
        self.texto.insert(INSERT, "A primeira contém 5 perguntas, cada uma valendo mil reais cumulativos.\n" )
        self.texto.insert(INSERT, "A segunda rodada, de 5 perguntas valendo R$ 10 mil cumulativos cada.\n" )
        self.texto.insert(INSERT, "A terceira, de 5 perguntas de R$100 mil reais cumulativos cada.\n" )
        self.texto.insert(INSERT, "A última pergunta vale R$ 1 milhão.") 
        self.texto.pack(padx=5, pady=15)

        self.conteudoPremiacao = "        Acertar	 Parar	     Errar\n" + \
                            "1	    R$ 1 mil	R$ 1 mil	R$ 500\n" + \
                            "2	    R$ 2 mil	R$ 1 mil	R$ 500\n" + \
                            "3	    R$ 3 mil	R$ 2 mil	R$ 1 mil\n" + \
                            "4	    R$ 4 mil	R$ 3 mil	R$ 1.500\n" + \
                            "5	    R$ 5 mil	R$ 4 mil	R$ 2 mil\n" + \
                            "6	    R$ 10 mil	R$ 5 mil	R$ 2.500\n" + \
                            "7	    R$ 20 mil	R$ 10 mil	R$ 5 mil\n" + \
                            "8	    R$ 30 mil	R$ 20 mil	R$ 10 mil\n" + \
                            "9	    R$ 40 mil	R$ 30 mil	R$ 15 mil\n" + \
                            "10	    R$ 50 mil	R$ 40 mil	R$ 20 mil\n" + \
                            "11	    R$ 100 mil	R$ 50 mil	R$ 25 mil\n" + \
                            "12	    R$ 200 mil	R$ 100 mil	R$ 50 mil\n" + \
                            "13	    R$ 300 mil	R$ 200 mil	R$ 100 mil\n" + \
                            "14	    R$ 400 mil	R$ 300 mil	R$ 150 mil\n" + \
                            "15	    R$ 500 mil	R$ 400 mil	R$ 200 mil\n" + \
                            "16	    R$ 500 mil	R$ 400 mil	R$ 200 mil\n";
                        
        self.textoPremiacao = scrolledtext.ScrolledText(self.instrucoesTk,width=70,height=18)
        self.textoPremiacao.insert(INSERT,self.conteudoPremiacao)

        self.textoPremiacao.pack(pady= 2)

        self.instrucoesTk.geometry("700x500+200+200")
        self.instrucoesTk.mainloop()   


    # =========================================== Tirar Foto =======================================
    def tirarFotoCampeao(self, args):

        self.camera_port = 0
    
        self.nFrames = 30
    
        self.camera = cv2.VideoCapture(self.camera_port)
        
        self.file = "Imagens/Campeao.png"
            
        print ("Digite <ESC> para sair / <s> para Salvar")
        
        self.emLoop= True
        
        while(self.emLoop):
        
            self.retval, self.img = self.camera.read()
            cv2.imshow('Foto',self.img)
        
            self.k = cv2.waitKey(100)
        
            if self.k == 27:
                self.emLoop= False
            
            elif self.k == ord('s'):
                cv2.imwrite(self.file, self.img)
                self.emLoop= False
        
        cv2.destroyAllWindows()
        self.camera.release()
        return 0


pygame.init()
tela = Tk()
tela["bg"] = "#051023"
tela.geometry("500x500+200+200")
Interface(tela)
tela.mainloop()