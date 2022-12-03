#Produzido por Kaian Vinicius, @Kaian32

#LIGA ISSO DEPOIS
import boot
from os import system #fazer certo em linux depois
import os #importando o OS como um todo logo
import time #importando o tempo
system('cls') #limpando comandos anteriores
print("Olá, seja bem vindo ao Copa Manager!") #mensagem de boas vindas

#open ("equipes.equipes", "a+") #SUBSTITUIDO POR FILECHECK#puxando o arquivo de equipes, caso não exista, ele será criado.
#open ("jogos.jogos", "a+") #SUBSTITUIDO POR FILECHECK#puxando o arquivo de jogos, caso não exista, ele será criado.

def leitor_equipes(): #faz a leitura do arquivo de equipes e monta uma lista a partir da mesma
    with open ("equipes.equipes", "r+") as valor:
        lista = []
        for equipes in valor:
            lista.append(equipes)
        return len(lista)

def leitor_jogos(): #faz a leitura do arquivo de jogos e monta uma lista a partir da mesma
    with open ("jogos.jogos", "r+") as valor:
        lista = []
        for equipes in valor:
            lista.append(equipes)
        return len(lista)

def nova_equipe(): #a def contém o processo de criação e salvamento de uma nova equipe
    system("cls")
    confirma = input("Deseja Realmente adicionar uma nova equipe?\n1) Sim\n2) Não\n")
    if (confirma == "1"):
        with open ("equipes.equipes", "a+") as equipes:
            equipes.write(str(input("Insira o nome da equipe: ").upper()))
            equipes.write("\n")
    system("cls")

def novo_jogo():
    system("cls")
    confirma = input("Deseja Realmente adicionar um novo jogo?\n1) Sim\n2) Não\n")
    if (confirma == "1"):
        with open ("jogos.jogos", "a+") as equipes:
            equipes.write(str(input("Insira o nome da equipe 1: ").upper()))
            equipes.write(str("(|)"))
            equipes.write(str(input("Insira o nome da equipe 2: ").upper()))
            equipes.write(str("(|)"))
            equipes.write(str(input("Insira a quantidade de gols da equipe 1: ").upper()))
            equipes.write(str("(|)"))
            equipes.write(str(input("Insira a quantidade de gols da equipe 2: ").upper()))
            equipes.write(str("(|)"))
            equipes.write(str(input("Insira a quantidade total de faltas: ").upper()))
            equipes.write(str("(|)"))
    system("cls")

def todos_jogos():
    system("cls")
    jogos_file = open("jogos.jogos","r")
    jogos = jogos_file.read()
    jogos_lista = [jogos.split("(|)")]
    for jogos_lista in range(4):
        print(jogos_lista(1))
        print(jogos_lista(2))
        print(jogos_lista(3))
        print(jogos_lista(4))
    print(jogos_lista)
    escolha = input("\nAperte qualquer botão para retornar ao menu principal. ")
    escolha = escolha.strip()
    match escolha:
        case other:
            system("cls")
            return
    
def todas_equipes():
    system("cls")
    
    escolha = input("\nAperte qualquer botão para retornar ao menu principal. ")
    escolha = escolha.strip()
    match escolha:
        case other:
            system("cls")
            return

while True:
    print("Selecione uma das opções abaixo:")
    print("1) SAIR\nFecha o aplicativo.")
    print("2) Nova Equipe\nAdiciona uma nova equipe ao dados.")
    print("3) Novo Jogo\nAdiciona um novo jogo aos dados.")
    print("4) Todos os jogos\nAbre uma tela detalhada com todos os jogos gravados.")
    print("5) Todas as equipes\nAbre uma tela detalhada com todos os jogos gravados.")
    print(f'\n\nTotal de Jogos = {leitor_jogos()}')
    print(f'Total de Equipes = {leitor_equipes()}')


    escolha = input("Selecione uma opção: ")
    escolha = escolha.strip()

    match escolha:
        case "1":
            system("cls")
            break
        case "2":
            nova_equipe()
        case "3":
            novo_jogo()
        case "4":
            todos_jogos()
        case "5":
            todos_jogos()
        case other:
            system("cls")
            print("Esta opção não é válida! Tente novamente!")
            time.sleep(1)
            system("cls")