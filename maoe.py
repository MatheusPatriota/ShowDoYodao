# Alunos: Matheus da Silva Coimbra Patriota
#        Clênio Borges Barboza Filho
# Curso: Engenharia de Software
# Matricula: 20192EWBJ0027
#            20192EWBJ0221

# O programa consiste em três rodadas e uma pergunta final:
# a primeira contém 5 perguntas, cada uma valendo mil reais cumulativos.
# A segunda rodada, de 5 perguntas valendo R$ 10 mil cumulativos cada. 
# A terceira, de 5 perguntas de R$100 mil reais cumulativos cada. 
# A última pergunta vale R$ 1 milhão.

# 16 perguntas
# Acertar - A proxima quantia
# Parar - A quantia anterior
# Erar - A metada da Quantia que garanharia se parase

# 	    Acertar	    Parar	    Errar
# 1	    R$ 1 mil	R$ 1 mil	R$ 500
# 2	    R$ 2 mil	R$ 1 mil	R$ 500
# 3	    R$ 3 mil	R$ 2 mil	R$ 1 mil
# 4	    R$ 4 mil	R$ 3 mil	R$ 1.500
# 5	    R$ 5 mil	R$ 4 mil	R$ 2 mil
# 6	    R$ 10 mil	R$ 5 mil	R$ 2.500
# 7	    R$ 20 mil	R$ 10 mil	R$ 5 mil
# 8	    R$ 30 mil	R$ 20 mil	R$ 10 mil
# 9	    R$ 40 mil	R$ 30 mil	R$ 15 mil
# 10	R$ 50 mil	R$ 40 mil	R$ 20 mil
# 11	R$ 100 mil	R$ 50 mil	R$ 25 mil
# 12	R$ 200 mil	R$ 100 mil	R$ 50 mil
# 13	R$ 300 mil	R$ 200 mil	R$ 100 mil
# 14	R$ 400 mil	R$ 300 mil	R$ 150 mil
# 15	R$ 500 mil	R$ 400 mil	R$ 200 mil
# 16	R$ 1 milhão	R$ 500 mil	R$ 0

import  random
import os


def removeQuebraLinha(lista):   
    for i in range(len(lista)):
        lista[i] = lista[i].replace('\n',"")
    return lista

def quantia(acertos,condicao):
    valor = "0"
    if acertos == 1:
        if condicao == 'n':
            print("Primeira Rodada")
            print("Valendo R$ 1000 reais ")
        valor = "1.000"
    elif acertos == 2:
        if condicao == 'n':
            print("Valendo R$ 2000 reais ")
        valor = "2.000"
    elif acertos == 3:
        if condicao == 'n':
            print("Valendo R$ 3000 reais ")
        valor = "3.000"
    elif acertos == 4:
        if condicao == 'n':
            print("Valendo R$ 4000 reais ")
        valor = "4.000"
    elif acertos == 5:
        if condicao == 'n':
            print("Valendo R$ 5000 reais ")
        valor = "5.000"
    elif acertos == 6:
        if condicao == 'n':
            print("Segunda Rodada")
            print("Valendo R$ 10 mil reais ")
        valor = "10.000"
    elif acertos == 7:
        if condicao == 'n':
            print("Valendo R$ 20 mil reais ")
        valor = "20.000"
    elif acertos == 8:
        if condicao == 'n':
            print("Valendo R$ 30 mil reais ")
        valor = "30.000"
    elif acertos == 9:
        if condicao == 'n':
            print("Valendo R$ 40 mil reais ")
        valor = "40.000"
    elif acertos == 10:
        if condicao == 'n':
            print("Valendo R$ 50 mil reais ")
        valor = "50.000"
    elif acertos == 11:
        if condicao == 'n':
            print("Terceira Rodada")
            print("Valendo R$ 100 mil reais ")
        valor = "100.000"
    elif acertos == 12:
        if condicao == 'n':
            print("Valendo R$ 200 mil reais ")
        valor = "200.000"
    elif acertos == 13:
        if condicao == 'n':
            print("Valendo R$ 300 mil reais ")
        valor = "300.000"
    elif acertos == 14:
        if condicao == 'n':
            print("Valendo R$ 400 mil reais ")
        valor = "400.000"
    elif acertos == 15:
        if condicao == 'n':
            print("Valendo R$ 500 mil reais ")
        valor = "500.000"
    elif acertos == 16:
        if condicao == 'n':
            print("Pergunta Final")
            print("Valendo R$ 1 milhão de Reais ")
        valor = "1.000.000"
    return valor

def sorteiaQuestoes(lista1,lista2):
    for i in range(5):
            selecionado = random.choice(lista1)
            while selecionado in lista2:
                selecionado = random.choice(lista1)
            lista2.append(selecionado)

# abertura de arquivos
perguntas = os.listdir('Perguntas')
aux = []

for i in perguntas:
    arquivo = open('Perguntas/'+i,"r")
    aux.append(arquivo.readlines())


for indice,linha in enumerate(aux):
    aux[indice] = removeQuebraLinha(linha)

perguntasFaceis = []
perguntasDificeis = []
perguntasMedias = []
perguntasFinais = []

# encontra e insere as perguntas de acordo com seu grau de dificuladade
for i in aux:
    if i[0] == '0':
        perguntasFaceis.append(i)
    elif i[0] == '1':
        perguntasMedias.append(i)
    elif i[0] == '2':
        perguntasDificeis.append(i)
    else:
        perguntasFinais.append(i)


s = open("participantes.txt","w")

# variaveis
sair = "sim"
erros = 0
valorGanho = "0"

print("Bem vindo ao Yoda do Milhão")

while True:
    if sair.lower() == "nao":
        break
    else:

        # sorteio arquvios de Perguntas
        # lista com todas os arquivos de perguntas, alternativas e respostas 


        perguntasFaceisSelecionadas = []
        perguntasDificeisSelecionadas = []
        perguntasMediasSelecionadas = []
        perguntasFinalSelecionada = []

        sorteiaQuestoes(perguntasFaceis,perguntasFaceisSelecionadas)
        sorteiaQuestoes(perguntasMedias,perguntasMediasSelecionadas)
        sorteiaQuestoes(perguntasDificeis,perguntasDificeisSelecionadas)
        perguntasFinalSelecionada.append(random.choice(perguntasFinais))

        valorGanho = "0"
        numeroSortado =random.randint(0,2)
        pontuacao = 0
        contagem = 0
        participante = input("Informe o nome do participante: ")
        for i in range(16):

            if i == 0 or i == 5 or i == 10 or i == 15 or i == 16:
                apontador = 0
                
            if i  >= 0 and i < 5:
                pergunta = perguntasFaceisSelecionadas[apontador][1]
                alternativas = perguntasFaceisSelecionadas[apontador][2:6]
                resposta = perguntasFaceisSelecionadas[apontador][6]
                del(perguntasFaceisSelecionadas[apontador])
            elif i >= 5 and i < 10:
                pergunta = perguntasMediasSelecionadas[apontador][1]
                alternativas = perguntasMediasSelecionadas[apontador][2:6]
                resposta = perguntasMediasSelecionadas[apontador][6]
                del(perguntasMediasSelecionadas[apontador])
            elif i >= 10 and i < 15:
                pergunta = perguntasDificeisSelecionadas[apontador][1]
                alternativas = perguntasDificeisSelecionadas[apontador][2:6]
                resposta = perguntasDificeisSelecionadas[apontador][6]
                del(perguntasDificeisSelecionadas[apontador])
            else:
                pergunta = perguntasFinalSelecionada[apontador][1]
                alternativas = perguntasFinalSelecionada[apontador][2:6]
                resposta = perguntasFinalSelecionada[apontador][6]
                del(perguntasFinalSelecionada[apontador])
            #pegando pergunta a pergunta 
            cont = 1
            print()
            quantia(pontuacao+1,'n')
            print()
            print(pergunta)
            print("Alternativas: ")
            #exbibindo alternativas
            for j in alternativas:
                print(cont," - ",j)
                cont +=1
            print()
            print("Deseja")
            print("1 - Tentar")
            print("2 - Parar")
            opcao = input("Escolha sua ação: ")

            # tratamento de opcao invalida
            while opcao != '1' and opcao != '2':
                print()
                print("Opção inválida, tente novamente!")
                opcao = input("Escolha sua ação: ")

            if opcao == '1':        
                resp = input("Informe a resposta do participante: ")
                #    tratamento de resposta invalida
                while resp != '1' and resp != '2' and resp != '3' and resp != '4':
                    print("Reposta Invalida, tente Novamente!")
                    print()
                    resposta = input("Informe a resposta do participante: ")
                
                if resp == resposta:
                    print()
                    print("Acertar você conseguiu!")
                    print("Yoda Orgulhoso está!")
                    print()

                    pontuacao += 1
                    valorGanho = quantia(pontuacao,'s')
                    contagem += 1
                else:
                    print("Errouuuuuuuuuuuu")
                    # valorGanho = str(float(quantia(pontuacao,'s'))/2)
                    valorGanho = (float(valorGanho)/2)*1000
                    print("O valor Total ganho por {:} foi de {:} ".format(participante,valorGanho))
                    break
            elif opcao == '2':
                print("Você decidiu por parar")
                print("O valor Total ganho por {:} foi de {:} reais".format(participante,valorGanho))
                break

    s.write(participante + " " + str(pontuacao) + "\n ")
    sair = input("Deseja Continuar jogando (sim ou nao)? ")

s.close()
s = open("participantes.txt","r")

participantes = s.read()
participantes = participantes.split(" ")
participantes = removeQuebraLinha(participantes)
participantesOrdenados = []

for i in range(len(participantes)):
    if participantes[i] == "":
        del participantes[i]


while len(participantes) != 0:
    maior = 0
    indiceMaior = 0
    for i in range(len(participantes)):
        if not(i % 2 == 0):
            if int(participantes[i]) > maior :
                maior = int(participantes[i])
                indiceMaior = i
    
    participantesOrdenados.append(participantes[indiceMaior-1] + " - " + participantes[indiceMaior]) 
    del participantes[indiceMaior]
    del participantes[indiceMaior-1]


# escrevendo os participantes ordenados
so = open("participantesOrdenados.txt","w")
for  i in participantesOrdenados:
    so.write(i + "\n")
so.close()

# abrindo arquivo de participantes ordenados e removendo os \n
so = open("participantesOrdenados.txt","r")
participantesOrdenados = removeQuebraLinha(so.readlines())

# exibindo participantes ordenados ao final do jogo
print("Pontuação Final dos Participantes: ")
for linha in participantesOrdenados:
    print(linha + " Pontos")

so.close()    
s.close() 
