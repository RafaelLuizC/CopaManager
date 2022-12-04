import os
import time

#Essa função serve para retirar os arquivos de texto, e transformar em uma lista.
def descompactador_equipes(ordenador): #Esta funcionando perfeitamente! 25\11\2022 Rafael!
    lista = []
    with open ("equipes.txt","r",encoding="utf-8") as banco_de_dados: #Abre o Banco de Dados.
        for linha in banco_de_dados.readlines(): #Percorre o Banco de Dados.
            linha = linha.split('(-)') #Separa os dados do Banco de Dados.
            linha[2] = linha[2][0] #Retira o /n do final da linha
            dicionario = {'equipe':linha[0],'abreviacao':linha[1],'grupo':linha[2]} #Cria um dicionario com os dados do Banco de Dados.
            lista.append(dicionario) #Adiciona o dicionario a lista.
        if ordenador == 1:
            lista = sorted(lista, key=lambda k: k['equipe']) #Ordena a lista pelo nome da equipe.
        elif ordenador == 2:
            lista = sorted(lista, key=lambda k: k['abreviacao']) #Ordena a lista pela abreviação.
        elif ordenador == 3:
            lista = sorted(lista, key=lambda k: k['grupo']) #Ordena a lista pelo grupo.
    return lista #Retorna a lista de dicionarios.

def descompactador_jogos(ordenador): #Esta funcionando perfeitamente! 4\12\2022 Rafael!
    lista = []
    with open ("jogos.txt","r",encoding="utf-8") as banco_de_dados: #Abre o Banco de Dados.
        for linha in banco_de_dados.readlines(): #Percorre o Banco de Dados.
            linha = linha.split('(-)') #Separa os dados do Banco de Dados.
            linha[5] = linha[5][0] #Retira o /n do final da linha
            #Transforma as faltas, e placar em numeros inteiros dentro do dicionario.
            linha[2] = int(linha[2])
            linha[3] = int(linha[3])
            linha[4] = int(linha[4])
            linha[5] = int(linha[5])
            dicionario = {'equipe1':linha[0],'equipe2':linha[1],'placar1':linha[2],'placar2':linha[3],'faltas1':linha[4],'faltas2':linha[5]} #Cria um dicionario com os dados do Banco de Dados.
            lista.append(dicionario) #Adiciona o dicionario a lista.
        if ordenador == 1: #Ordena a lista por maior placar.
            lista = sorted(lista, key=lambda k: k['placar1'], reverse=True)
        elif ordenador == 2:
            lista = sorted(lista, key=lambda k: k['equipe1'])
        elif ordenador == 3:
            lista = sorted(lista, key=lambda k: k['faltas1'])
    return lista #Retorna a lista de dicionarios.

######################################################################################################
#As Funções Acima servem para descompactar os arquivos de texto, e transformar em uma lista de dicionarios.
######################################################################################################

def lista_grupos(): #Esta funcionando perfeitamente! 30\11\2022 Rafael!
    lista = descompactador_equipes(3) #Chama a função descompactador_equipes.
    a = [] #Cria uma lista vazia.
    b = []
    c = []
    d = []
    e = []
    f = []
    g = [] 
    h = []
    for item in lista: #Percorre a lista.
        if item['grupo'] == 'A':  #Verifica se o grupo é igual a A.
            item = item['equipe'],item['abreviacao']
            a.append(item) #Adiciona o item a lista A.
        elif item['grupo'] == 'B':
            item = item['equipe'],item['abreviacao']
            b.append(item)
        elif item['grupo'] == 'C':
            item = item['equipe'],item['abreviacao']
            c.append(item)
        elif item['grupo'] == 'D':
            item = item['equipe'],item['abreviacao']
            d.append(item)
        elif item['grupo'] == 'E':
            item = item['equipe'],item['abreviacao']
            e.append(item)
        elif item['grupo'] == 'F':
            item = item['equipe'],item['abreviacao']
            f.append(item)
        elif item['grupo'] == 'G':
            item = item['equipe'],item['abreviacao']
            g.append(item)
        elif item['grupo'] == 'H':
            item = item['equipe'],item['abreviacao']
            h.append(item)
    return a,b,c,d,e,f,g,h #Retorna as listas A,B,C,D,E,F,G e H.

def excluir_equipes(equipe): #Esta funcionando perfeitamente! 25\11\2022 Rafael!
    lista_equipes = descompactador_equipes(1) #Chama a função descompactador_equipes.
    with open ("equipes.txt","w",encoding="utf-8") as jogos: #Abre o Banco de Dados.
        for item in lista_equipes:
            if item['equipe'] != equipe: #Verifica se o nome da equipe é diferente do nome da equipe que o usuario deseja excluir.
                jogos.write(f"{item['equipe']}(-){item['abreviacao']}(-){item['grupo']}(-)\n") #Escreve no Banco de Dados.
    lista_jogos = descompactador_jogos(2)
    lista_temp = []
    for item in lista_jogos:
        if item['equipe1'] == equipe:
            item['equipe1'] = "EQUIPE EXCLUIDA"
        elif item['equipe2'] == equipe:
            item['equipe2'] = "EQUIPE EXCLUIDA"
        lista_temp.append(item)
    with open ("jogos.txt","w",encoding="utf-8") as jogos: #Abre o Banco de Dados.
        for item in lista_temp:
            if item['equipe1'] == "EQUIPE EXCLUIDA" and item['equipe2'] == "EQUIPE EXCLUIDA":
                continue
            jogos.write(f"{item['equipe1']}(-){item['equipe2']}(-){item['placar1']}(-){item['placar2']}(-){item['faltas1']}(-){item['faltas2']}(-)\n")
    return (print("Equipe excluida com sucesso!"))

def excluir_jogos(jogo_excluir):
    lista = descompactador_jogos(2)
    lista2 = []
    for item in lista:
        if item['equipe1'] == jogo_excluir['equipe1'] and item['equipe2'] == jogo_excluir['equipe2']:
            pass    
        else:
            lista2.append(item)
    with open ("jogos.txt","w",encoding="utf-8") as banco_de_dados:
        for item in lista2:
            banco_de_dados.write(f'{item["equipe1"]}(-){item["equipe2"]}(-){item["placar1"]}(-){item["placar2"]}(-){item["faltas1"]}(-){item["faltas2"]}\n')

def editar_jogos(jogo_editar): 
    lista = descompactador_jogos(2) # Recebe uma lista para comparação.
    lista2 = [] #Cria uma lista que será editada.
    for item in lista: #Percorre a lista de comparação.
        if item['equipe1'] == jogo_editar['equipe1'] and item['equipe2'] == jogo_editar['equipe2']: #Encontra a informação a ser editada.
            print ("Digite o novo placar do jogo entre",item['equipe1'],"e",item['equipe2'])
            placar1 = validaplacar() #Valida o placar.
            placar2 = validaplacar() #Valida o placar.
            print ("Digite o numero de faltas do jogo entre",item['equipe1'],"e",item['equipe2'])
            faltas1 = validaplacar() 
            faltas2 = validaplacar() 
            item['placar1'] = placar1
            item['placar2'] = placar2
            item['faltas1'] = faltas1
            item['faltas2'] = faltas2
            lista2.append(item) #Adiciona o item editado a lista2.
        else:
            lista2.append(item) #Adiciona o item não editado a lista2.
    with open ("jogos.txt","w",encoding="utf-8") as banco_de_dados:
        for item in lista2:
            banco_de_dados.write(f'{item["equipe1"]}(-){item["equipe2"]}(-){item["placar1"]}(-){item["placar2"]}(-){item["faltas1"]}(-){item["faltas2"]}\n')

def janela_partida(lista):
    os.system('cls')
    #Vai começçar a interface que apresenta os dados da partida.
    print ("\n\n\n")
    #Aqui vai ser apresentado o nome das equipes que Jogaram a partida, de um lado a Equipe 1 e do outro a Equipe 2.
    print (f'SELEÇÕES\n'.center(80))
    print (lista['equipe1'].center(40),lista['equipe2'].center(40))
    print (f'GOLS MARCADOS\n'.center(80))
    print (str(lista['placar1']).center(40),str(lista['placar2']).center(40))
    print (f'FALTAS COMETIDAS\n'.center(80))
    print (str(lista['faltas1']).center(40),str(lista['faltas2']).center(40))
    print (f'VENCEDOR\n'.center(80))
    placar = lista['equipe1'] if lista['placar1'] > lista['placar2'] else lista['equipe2']
    print (placar.center(80))
    print ("\n\n\n")
    acao = input('Pressione enter para voltar ao menu').upper()
    match acao:
        case "EXCLUIR":
            print ("Tem certeza que deseja excluir a equipe? [S] Para Excluir, [N] Para Voltar ao Menu")
            acao = input().upper()
            if acao == "S":
                excluir_jogos(lista)
                janela_jogos()
        case "EDITAR":
            editar_jogos(lista)
            janela_jogos()

def janela_jogos():
    ordenacao = 3
    lista1 = separador(descompactador_jogos(3))#Por padrão deixei em 3, que representa a separação por grupo.
    x = 0
    mensagem = ''
    while True:
        os.system('cls')
        print (f'\n{mensagem.center(80)}\n')
        mensagem = ''
        #Montando uma Janela para essa lista.
        for i in range(len(lista1[x])):
            print (f'Jogo numero {i+1+(5*x)}'.center(80))
            print (f"{lista1[x][i]['equipe1']:>20} {lista1[x][i]['placar1']:>3} x {lista1[x][i]['placar2']:<3} {lista1[x][i]['equipe2']:<20}".center(80))
            #Printa uma linha de acordo com o tamanho dos times.
        print ("\n\n")
        print (f'[ORDENAR] - [SAIR] = [VOLTAR] para voltar a Pagina [AVANÇAR] para ir para a proxima Pagina'.center(80))
        print (f'Voce esta na Pagina {x} de {len(lista1)-1}'.center(80))
        print ("\n\n")
        opcao = input ("Digite o Valor Desejado: ").upper()
        #Aqui verifica se a opcao escolhida é um nome presente na lista que esta sendo apresentada.
        if opcao == "SAIR": #Sai do programa.
            break
        elif opcao == "VOLTAR": #Volta para a pagina anterior.
            x = x - 1 if x > 0 else 0
        elif opcao == "AVANCAR":
            x = x + 1 if x < len(lista1)-1 else len(lista1)-1
        elif opcao == "ORDENAR":
            ordenacao -= 1
            if ordenacao == 0:
                ordenacao = 3
            lista1 = separador(descompactador_jogos(ordenacao))
        elif (opcao.isdigit()) == True:
            opcao = int(opcao)
            if opcao == ((x*5+1)):
                janela_partida(lista1[x][0])
            elif opcao == (x*5+2):
                janela_partida(lista1[x][1])
            elif opcao == (x*5+3):
                janela_partida(lista1[x][2])
            elif opcao == (x*5+4):
                janela_partida(lista1[x][3])
            elif opcao == (x*5+5):
                janela_partida(lista1[x][4])
            else:
                mensagem = ("Opção Invalida")
        
def editar_equipes(equipe): #Esta funcionando perfeitamente! 25\11\2022 Rafael!
    lista_equipes = [] #Lista que vai receber os dados editados das equipes.
    while True: #Loop para editar os dados da equipe.
        selecao_editada = input("Digite o nome da seleção que deseja editar: ").upper() #Recebe o novo nome da seleção
        if subsubvalidaSelecao(selecao_editada) == False: #Verifica se o nome da seleção é valido.
            print("Digite um nome válido!")
            continue
        else:
            break
    for linha in descompactador_equipes(3): #Recebe uma lista para comparação.
        if linha['equipe'] == equipe:
            linha['equipe'] = selecao_editada
            linha['abreviacao'] = selecao_editada[0:3].upper()
            lista_equipes.append(linha)
        else:
            lista_equipes.append(linha)
        print (lista_equipes)
    with open ("equipes.txt","w",encoding="utf-8") as jogos: #Abre o Banco de Dados.
        for item in lista_equipes:
            jogos.write(f"{item['equipe']}(-){item['abreviacao']}(-){item['grupo']}(-)\n") #Escreve no Banco de Dados.
    with open ("jogos.txt","r",encoding="utf-8") as banco_de_dados: #Abre o Banco de Dados.
        lista_jogos = []
        for linha in banco_de_dados.readlines(): #Percorre o Banco de Dados.
            linha = linha.split('(-)') #Separa os dados do Banco de Dados.
            linha[5] = linha[5][0] #Retira o /n do final da linha
            if linha[0] == equipe:
                linha[0] = selecao_editada
            elif linha[1] == equipe:
                linha[1] = selecao_editada
            lista_jogos.append(linha)
    with open ("jogos.txt","w",encoding="utf-8") as jogos: #Abre o Banco de Dados.
        for item in lista_jogos:
            jogos.write(f"{item[0]}(-){item[1]}(-){item[2]}(-){item[3]}(-){item[4]}(-){item[5]}(-)\n")
    return (print("Seleção editada com sucesso!"))

def subsubvalidaSelecao(checagem): # Essa função serve para checar se os valores inseridos no cadastro são caracteres especiais
    checagem = checagem.replace(" ","") # Retira os Espaços
    if checagem.isalpha() == False: # Verifica se o valor é alfabético
        return False

def separador(lista):
    lista_separada = []
    #Essa função é responsavel por criar uma lista com 5 sublistas.
    for x in range(len(lista)):
        if x % 5 == 0: #Se o resto da divisão de x por 5 for igual a 0, então... 
### PARA ALTERARA O TAMANHO DA LISTA, BASTA ALTERAR O NUMERO 5 PARA O NUMERO DESEJADO. ###
            lista_separada.append([]) #Adiciona uma lista vazia a lista1.
            lista_separada[-1].append(lista[x]) #Adiciona o item da lista na ultima posição da lista1.
        else:
            lista_separada[-1].append(lista[x]) #Caso o Resto da Divisão não seja 0 adiciona o item da lista na ultima posição da lista1.
    return lista_separada #Retorna a lista1.

def janelaselecoes(selecao): #Esta funcionando perfeitamente! 01\12\2022 Rafael!
    valores = [[],[],[],[],[],[],[]] #Valores[0] = Gols Marcados, Valores[1] = Gols Sofridos, Valores[2] = Faltas Cometidas, Valores[3] = Faltas Sofridas
    #Valores[4] = Vitorias S2 , Valores[5] = Derrotas , Valores[6] = Empates
    for item in descompactador_jogos(3): #Percorre a lista de dicionarios.
        if selecao == item["equipe1"]: #Se a seleção for igual a equipe1, então...
            valores[0].append(int(item["placar1"]))
            valores[1].append(int(item["placar2"]))
            valores[2].append(int(item["faltas1"]))
            valores[3].append(int(item["faltas2"]))
            if item["placar1"] > item["placar2"]:
                valores[4].append(f'O time {item["equipe1"]} venceu o time {item["equipe2"]} por {item["placar1"]}x{item["placar2"]}')
            elif item["placar1"] == item["placar2"]:
                valores[6].append(f'O time {item["equipe2"]} empatou com o time {item["equipe1"]} por {item["placar2"]}x{item["placar1"]}')            
            else:
                valores[5].append(f'O time {item["equipe1"]} perdeu para o time {item["equipe2"]} por {item["placar1"]}x{item["placar2"]}')
        elif selecao == item["equipe2"]: #Caso a seleção seja a equipe2.
            valores[0].append(int(item["placar2"]))
            valores[1].append(int(item["placar1"]))
            valores[2].append(int(item["faltas2"]))
            valores[3].append(int(item["faltas1"]))
            if item["placar1"] < item["placar2"]:
                valores[4].append(f'O time {item["equipe2"]} venceu o time {item["equipe1"]} por {item["placar2"]}x{item["placar1"]}')
            elif item["placar1"] == item["placar2"]:
                valores[6].append(f'O time {item["equipe2"]} empatou com o time {item["equipe1"]} por {item["placar2"]}x{item["placar1"]}')
            else:
                valores[5].append(f'O time {item["equipe2"]} perdeu para o time {item["equipe1"]} por {item["placar2"]}x{item["placar1"]}')
    print (f'Gols marcados: {sum(valores[0])}')
    print (f'Gols sofridos: {sum(valores[1])}')
    print (f'Saldo de Gols: {sum(valores[0]) - sum(valores[1])}')
    print (f'Faltas cometidas: {sum(valores[2])}')
    print (f'Faltas sofridas: {sum(valores[3])}')
    if len(valores[4]) == 0:
        print ("Nenhuma vitória")
    else:
        for item in valores[4]:
            print (item)
    if len(valores[6]) == 0:
        print ("Nenhum empate")
    else:
        for item in valores[6]:
            print (item)
    if len(valores[5]) == 0:
        print ('Nenhuma derrota')
    else:
        for item in valores[5]:
            print (item)            
    acao = input('Pressione enter para voltar ao menu').upper()
    match acao:
        case "EXCLUIR":
            print ("Tem certeza que deseja excluir a equipe? [S] Para Excluir, [N] Para Voltar ao Menu")
            acao = input().upper()
            if acao == "S":
                excluir_equipes(selecao)
                janela()
        case "EDITAR":
            editar_equipes(selecao)
            janela()

def janela():
    ordenacao = 3
    lista1 = separador(descompactador_equipes(ordenacao))#Por padrão deixei em 3, que representa a separação por grupo.
    x = 0
    while True:
        os.system('cls')
        print ("\n\n\n")
        #Montando uma Janela para essa lista.
        for i in range(len(lista1[x])):
            #Printa os dados da lista1, 'equipe' no canto esquerdo, 'abreviacao' no centro e 'grupo' no canto direito.
            print (f"{lista1[x][i]['equipe']:<20}{lista1[x][i]['abreviacao']:^10}{lista1[x][i]['grupo']:^10}".center(80))
            print (("-"*40).center(80))
        print ("\n\n")
        print (f'Você está na página {x} de {len(lista1)-1}'.center(80))
        print ("\n\n")
        print (f'[ORDENAR] - [SAIR] = [VOLTAR] para voltar a Pagina [AVANÇAR] para ir para a proxima Pagina'.center(80))
        opcao = input ("Digite o Valor Desejado: ").upper()
        #Aqui verifica se a opcao escolhida é um nome presente na lista que esta sendo apresentada.
        if opcao in [lista1[x][i]["equipe"] for i in range(len(lista1[x]))]: #CHORA BOY ESSA AQUI FUNCIONOU!!!!!!!!!!!!!
            if opcao == (lista1[x][0]["equipe"]):
                janelaselecoes(lista1[x][0]["equipe"])
            elif opcao == (lista1[x][1]["equipe"]):
                janelaselecoes(lista1[x][1]["equipe"])
            elif opcao == (lista1[x][2]["equipe"]):
                janelaselecoes(lista1[x][2]["equipe"])
            elif opcao == (lista1[x][3]["equipe"]):
                janelaselecoes(lista1[x][3]["equipe"])
            elif opcao == (lista1[x][4]["equipe"]):
                janelaselecoes(lista1[x][4]["equipe"])
        elif opcao == "SAIR": #Sai do programa.
            break
        elif opcao == "VOLTAR": #Volta para a pagina anterior.
            x = x - 1 if x > 0 else 0
        elif opcao == "AVANCAR":
            x = x + 1 if x < len(lista1)-1 else len(lista1)-1
        elif opcao == "ORDENAR":
            ordenacao -= 1
            if ordenacao == 0:
                ordenacao = 3
            lista1 = separador(descompactador_equipes(ordenacao))

def janela_jogos():
    ordenacao = 3
    lista1 = separador(descompactador_jogos(3))#Por padrão deixei em 3, que representa a separação por grupo.
    x = 0
    mensagem = ''
    while True:
        os.system('cls')
        print (f'\n{mensagem.center(80)}\n')
        mensagem = ''
        #Montando uma Janela para essa lista.
        for i in range(len(lista1[x])):
            print (f'Jogo numero {i+1+(5*x)}'.center(80))
            print (f"{lista1[x][i]['equipe1']:>20} {lista1[x][i]['placar1']:>3} x {lista1[x][i]['placar2']:<3} {lista1[x][i]['equipe2']:<20}".center(80))
            #Printa uma linha de acordo com o tamanho dos times.
        print ("\n\n")
        print (f'[ORDENAR] - [SAIR] = [VOLTAR] para voltar a Pagina [AVANÇAR] para ir para a proxima Pagina'.center(80))
        print (f'Voce esta na Pagina {x} de {len(lista1)-1}'.center(80))
        print ("\n\n")
        opcao = input ("Digite o Valor Desejado: ").upper()
        #Aqui verifica se a opcao escolhida é um nome presente na lista que esta sendo apresentada.
        if opcao == "SAIR": #Sai do programa.
            break
        elif opcao == "VOLTAR": #Volta para a pagina anterior.
            x = x - 1 if x > 0 else 0
        elif opcao == "AVANCAR":
            x = x + 1 if x < len(lista1)-1 else len(lista1)-1
        elif opcao == "ORDENAR":
            ordenacao -= 1
            if ordenacao == 0:
                ordenacao = 3
            lista1 = separador(descompactador_jogos(ordenacao))
        elif (opcao.isdigit()) == True:
            opcao = int(opcao)
            if opcao == ((x*5+1)):
                janela_partida(lista1[x][0])
            elif opcao == (x*5+2):
                janela_partida(lista1[x][1])
            elif opcao == (x*5+3):
                janela_partida(lista1[x][2])
            elif opcao == (x*5+4):
                janela_partida(lista1[x][3])
            elif opcao == (x*5+5):
                janela_partida(lista1[x][4])
            else:
                mensagem = ("Opção Invalida")

def validagrupo(): #Esta Funcionando Perfeitamente! 25\11\2022 Rafael!
    while True:  #Loop infinito.
        grupo = input ("Digite o Grupo da Seleção: ").upper() #Pede para o usuário digitar o grupo da seleção.
        if len(grupo) != 1: 
            print ("O Grupo do Time deve ter apenas um Caracter.") #Verifica se o grupo possui apenas um caracter.
            continue 
        if grupo in 'ABCDEFGH': #Verifica se o grupo é valido. 
            if contador(grupo) == True: #Verifica se o grupo já possui 4 seleções. 
                return grupo
            elif contador(grupo) == False: 
                print ("Esse Grupo já esta cheio, tente outro.") #Caso o grupo já esteja cheio, ele pergunta se o usuário quer cadastrar outro grupo.
                continue
        else:
            print ("Grupo Invalido, tente novamente.") 
            continue
                
def contador(pesquisa):
    cont = 0 #Contador
    for item in descompactador_equipes(3): #Percorre o Banco de Dados.
        if cont == 3: #Verifica se o contador é igual a x, o Limite é 4 pois é o total que cabem de grupo -1.
            return False #Retorna False caso o contador chegue ao valor de X.   
        elif item['grupo'] == pesquisa: #Verifica se o item da coluna é igual ao item buscado.
            cont += 1
    return True #Retorna True caso o contador não chegue ao valor de X.
            
def validaabreviacao(): #Esta Funcionando Perfeitamente! 01\12\2022 Rafael! \\\ Valida se a Abreviação esta preenchida corretamente.
    while True: #Loop infinito.
        abrev = input ("Digite a Abreviação da Seleção: ").upper() #Pede para o usuário digitar a abreviação da seleção.
        if len(abrev) != 3: # Verifica se a abreviação possui 3 caracteres
            print ("Abreviação Invalida, tente novamente.")
        else:
            if subabreviacao(abrev) == False: #Verifica se a abreviação já existe no Banco de Dados.
                print ("Essa Abreviação já esta cadastrada, tente outra.")
                continue #Caso a abreviação já exista, ele volta para o usuário cadastrar outra.
            if subabreviacao(abrev) == True:
                return abrev #Retorna a abreviação caso ela não exista no Banco de Dados.

def subabreviacao(abreviacao): #Essa função testa os valores digitados no cadastro de Abreviações
    for linhas in descompactador_equipes(2): #Percorre o Banco de Dados.
        if abreviacao == linhas['abreviacao']: #Verifica se a abreviação já esta cadastrada.
            return False #Retorna False caso a abreviação já esteja cadastrada.
    return True #Retorna True caso a abreviação não esteja cadastrada.

def validaselecao(): #Essa função serve para Validar os dados informados para os nomes dos times.
    while True:
        selecao = input ("Digite o Nome da Seleção: ").upper()
        if len(selecao) < 3: #Verifica se o nome da seleção possui algum caracter.
            print ("O Nome de um Pais precisa ter ao menos 3 Caracteres.")
            continue
        elif subsubvalidaSelecao(selecao) == False:
            print ("O Nome de um Pais não pode conter números, ou caracteres especiais.")
            continue
        else:
            if subvalidaselecao(selecao) == True:
                return selecao
            elif subvalidaselecao(selecao) == False:
                print ("Essa Seleção já esta cadastrada, tente outra.")
                continue

def subvalidaselecao(selecao): #Esta Funcionando Perfeitamente! 25\11\2022 Rafael!
    for linhas in descompactador_equipes(3):
        if selecao == linhas['equipe']: #Verifica se o nome da seleção já existe no banco de dados.
            return False
    return True
def subsubvalidaSelecao(checagem): # Essa função serve para checar se os valores inseridos no cadastro são caracteres especiais
    checagem = checagem.replace(" ","") # Retira os Espaços
    if checagem.isalpha() == False: # Verifica se o valor é alfabético
        return False

def cadastroequipes():                  #Esta Funcionando Perfeitamente! 25\11\2022 Rafael!
    selecao = validaselecao()           #Chama a função ValidaSelecao para validar o nome da seleção.
    abrev = validaabreviacao()          #Chama a função ValidaAbreviacao para validar a abreviação da seleção.
    grupo = validagrupo()               #Chama a função ValidaGrupo para validar o grupo da seleção.
    with open ("equipes.txt","a+",encoding="utf-8") as equipes: #Abre o Banco de Dados.
        equipes.write(f"{selecao}(-){abrev}(-){grupo}\n")       #Escreve no Banco de Dados.
        print ("Equipe Cadastrada com Sucesso!")
        return {'equipe':selecao,'abreviacao':abrev,'grupo':grupo} #Retorna um dicionario com os dados da seleção.

def validaplacar(): #Esta Funcionando Perfeitamente! 30\11\2022 Rafael!
    while True:
        placar = input ("Digite o Placar: ") #Pede para o usuário digitar o placar.
        if placar.isnumeric() == False: #Verifica se o placar é um valor numérico.
            print ("Placar Invalido, tente novamente.")
            continue
        if len(placar) > 2: #Verifica se o placar possui mais de 2 caracteres.
            print ("Valor Invalido, Tente Novamente.")
            continue #Caso o placar possua mais de 2 caracteres, ele volta para o usuário digitar novamente.
        else:
            return placar #Retorna o placar caso ele seja um valor numérico e possua no máximo 2 caracteres.

def cadastrojogos(): #Esta Funcionando Perfeitamente! 30\11\2022 Rafael!
    pais = subcadastrojogos() #Chama a função subCadastroJogos para validar o nome da seleção.
    pais2 = subcadastrojogos()
    if pais['grupo'] != pais2['grupo']: #Verifica se as seleções estão no mesmo grupo.
        print ("As Seleções não estão no mesmo Grupo, continuar mesmo assim?") #Caso as seleções não estejam no mesmo grupo, ele pergunta se o usuário deseja continuar.
        opcao = input ("Digite S para Sim e N para Não: ").upper() 
        match opcao: 
            case 'S':
                pass
            case 'N':
                return print ("Cadastro Cancelado.")
    placar = validaplacar() 
    placar2 = validaplacar()
    faltas = validaplacar()
    faltas2 = validaplacar()
    with open ("jogos.txt","a+",encoding="utf-8") as jogos: #Abre o Banco de Dados.
        jogos.write(f"{pais['equipe']}(-){pais2['equipe']}(-){placar}(-){placar2}(-){faltas}(-){faltas2}\n") #Escreve no Banco de Dados.
        return print ("Jogo Cadastrado com Sucesso!") #Retorna uma mensagem de sucesso.

def subcadastrojogos(): 
    while True: #Loop para validar o nome da seleção.
        busca = input ("Digite o Nome da Seleção: ").upper() #Pede o nome da seleção.
        for item in descompactador_equipes(3): #Percorre o Banco de Dados.
            if item['equipe'] == busca: #Verifica se o nome da seleção existe no Banco de Dados.
                return item #Retorna o nome da seleção.
        print ("Seleção não cadastrada, Gostaria de tentar novamente, ou cadastrar outra?") 
        opcao = input ("Digite S para Sim e N para Não: ").upper() #Pergunta se o usuário quer tentar novamente ou cadastrar outra seleção.
        match opcao:
            case 'S':
                continue
            case 'N':
                return cadastroequipes() #Chama a função cadastroequipes para cadastrar uma nova seleção.

def janela_grupos():
    os.system('cls')
    print ("\n\n\n\n")
    print (f'''GRUPO A = {lista_grupos()[0]}\nGRUPO B = {lista_grupos()[1]}\nGRUPO C = {lista_grupos()[2]}\nGRUPO D = {lista_grupos()[3]}\nGRUPO E = {lista_grupos()[4]}\nGRUPO F = {lista_grupos()[5]}\nGRUPO G = {lista_grupos()[6]}\nGRUPO H = {lista_grupos()[7]}'''.format(end='-').center(80))
    print ("\n\n\n")
    print (f'Total de Equipes: {len(descompactador_equipes(3))}'.center(80))
    print ("\n\n\n")
    input ("Pressione Enter para Voltar ao Menu Principal.")

def pesquisa_equipe():
    os.system('cls')
    print ("\n\n\n\n")
    busca = input ("Digite o Nome da Seleção: ").upper()
    for item in descompactador_equipes(3):
        if item['equipe'] == busca:
            janelaselecoes(item['equipe'])
            return
    print ("Seleção não cadastrada.")
    print ("\n\n\n")
    input ("Pressione Enter para Voltar ao Menu Principal.")

def menu():
    mensagem = "Menu Principal"
    while True:
        os.system('cls')
        print("\n\n")
        print (f'{mensagem}'.center(80))
        print ("Digite 1 para sair do Programa.\n".center(80))
        print ("Digite 2 para cadastrar uma nova Equipe.\n".center(80))
        print ("Digite 3 para cadastrar um novo Jogo.\n".center(80))
        print ("Digite 4 para ver o total de Jogos salvos.\n".center(80))
        print ("Digite 5 para ver o numero total de Equipes.\n".center(80))
        print ("Digite 6 para ver o numero total de Equipes.\n".center(80))
        print ("Digite 7 para fazer uma pesquisa pelo nome da Equipe.\n".center(80))
        print("Digite a opção desejada:".center(80))
        print ("\n\n")
        opcao = input()
        if len(opcao) <= 0 or opcao.isnumeric() == False:
            mensagem = ("Opção Invalida, tente novamente.")
            continue
        else:
            opcao = int(opcao)
            match opcao:
                case 1:
                    print ("Obrigado por usar o Programa.")
                    break
                case 2:
                    cadastroequipes()
                case 3:
                    cadastrojogos()
                case 4:
                    janela()
                case 5:
                    janela_jogos()
                case 6:
                    janela_grupos()
                case 7:
                    pesquisa_equipe()
                case other:
                    print ("Opção Invalida, tente novamente.")
                    continue
menu()
