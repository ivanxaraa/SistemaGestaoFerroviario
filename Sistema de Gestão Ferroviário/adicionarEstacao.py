from math import sin, cos, sqrt, atan2, radians
import clear as c
from tabulate import tabulate
import random





#-----------------------------Adicionar Estacao---------------------------------

def adicionarEstacao():    
    print("\n" * 35)
    resp = 1

    while(resp == 1): #criar mais estacoes
        
        print("\n\n----------- Adicionar Estacao -----------")        
        nomeEstacao = input("Nome da Estacao: ")
        if(len(nomeEstacao) < 4):
            while(len(nomeEstacao) < 5):
                nomeEstacao = input("Nome da Estacao devera ter pelo menos 5 digitos: ")
        
        codigoEstacao = input("Codigo da Estacao: ")
        acabou = False


        if(len(codigoEstacao) != 4):
            codigoEstacao = input("O Codigo da Estacao devera conter 4 letras: ")
            while(len(codigoEstacao) != 4):
                codigoEstacao = input("O Codigo da Estacao devera conter 4 letras: ")

        
        
        if(codigoEstacao.isnumeric() == True):
            codigoEstacao = input("O Codigo da Estacao nao pode conter numeros: ")
            while(codigoEstacao.isnumeric() == True):
                codigoEstacao = input("O Codigo da Estacao nao pode conter numeros: ")

            if(len(codigoEstacao) != 4):
                codigoEstacao = input("O Codigo da Estacao devera conter 4 letras: ")
                while(len(codigoEstacao) != 4):
                    codigoEstacao = input("O Codigo da Estacao devera conter 4 letras: ")
                
            
        
        
                
                
                    
            
        
        lati = input("Introduza a Latitude: ")
        if(lati.isnumeric()==False):
            while(lati.isnumeric()==False):
                lati = input("Erro! Introduza a Latitude: ")
                
        longi = input("Introduza a Longitude: ")
        if(longi.isnumeric()==False):
            while(longi.isnumeric()==False):
                longi = input("Erro! Introduza a Longitude: ")
        
    
        lista = nomeEstacao+","+codigoEstacao+","+lati+","+longi
        lista = str(lista)

        myFile = open("EstacoesCriadas.txt", "a")
        myFile.write(lista + "\n")
        myFile.close()

        print("\nDeseja Inserir mais Estacoes? ")
        print(" 1 - Sim")
        print(" 2 - Nao")
        resp = int(input("Escolha: "))
    
        if(resp == 2):
            resp += 1
        

        

#-----------------------------Adicionar Ligacao---------------------------------
    
def adicionarLigacao():
    myfile = open("EstacoesCriadas.txt", "r")    
    myData = myfile.readlines()
    data = myfile.read()
    myfile.close()
    

    linhas = len(myData)
    
    
    myList = []

    for i in myData:
        myList += [i[:-1].split(",")]    
    
    print("\n" *37)        

    headers=("Numero", "Estacao", "Codigo Estacao", "Latitude", "Longitude")
    
    
    
    print("\n-------------------------------- Estaçoes --------------------------------")
    numeros=[]
    for n in range(1,len(myList)+1):
        myList[n-1]=[n]+myList[n-1]
    print(tabulate(myList,headers,tablefmt="fancy_grid"))
    print("\n---------------------------------------------------------------------------")
    
    num1 = int(input("\nIntroduza o numero da 1º Estacao para a conexao: "))
    numeroEscolhido1 = num1
    num1 -= 1
    
    if(num1 >= linhas or num1 <0):
        while(num1>=linhas or num1 <0):
            num1 = int(input("\nIntroduza o numero da 1º Estacao para a conexao: "))
            
    
    

    
    nome1 = myList[num1][1]    
    codEstacao1 = myList[num1][2]
    
   

    print("\n-------------------------------- Estaçoes --------------------------------")

    
    print(tabulate(myList,headers,tablefmt="fancy_grid"))
    print("\n---------------------------------------------------------------------------")
    
    num2 = int(input("\nIntroduza o numero da 2º estacao: "))
    
    

    
    
    if(num2 >= linhas or num2 <0 or numeroEscolhido1 == num2):
        while(num2>=linhas or num2 <0 or numeroEscolhido1 == num2):
            num2 = int(input("\nIntroduza o numero da 2º estacao: "))    
        
    
    
    nome2 = myList[num2-1][1]   
    codEstacao2 = myList[num2-1][2]
    

    
    
    
    
    myfile = open("EstacoesConexoes.txt", "a")    
    myfile.close()

    myfile = open("EstacoesConexoes.txt", "r") 
    myData2 = myfile.readlines()
    
    lista2 = []
    myList2 = []

    

    R = 6373.0

       
    lat1 = radians(float(myList[num1][3]))    
    lon1 = radians(float(myList[num1][4]))
    
    lat2 = radians(float(myList[num2-1][3]))
    lon2 = radians(float(myList[num2-1][4]))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c    
    
    
    
    codconexao = codEstacao1 + "_" + codEstacao2
    codconexao = str(codconexao)

    lista2 = codconexao
    
    
    print("\n" * 37)

    print("\n\n-------------------------------------------------------")
    velocidadeMax = input("Introduza a velocidade maxima permitida: ")
    if(velocidadeMax.isnumeric()==False):
            while(velocidadeMax.isnumeric()==False):
                velocidadeMax = input("Erro! Introduza a velocidade maxima permitida: ")
    print("-------------------------------------------------------\n\n\n")

    distance = str(round(distance, 2)) + " km"
    velocidadeMax = str(velocidadeMax) + " km/h"
    
    lista2 += "," + nome1 + "," + nome2 + "," + str(distance) + "," + str(velocidadeMax)

    

    myfile = open("EstacoesConexoes.txt", "a")
    myfile.write(lista2 + "\n")
    myfile.close()

    myfile = open("EstacoesConexoes.txt", "r") 
    myData2 = myfile.readlines()

    for i in myData2:
        myList2 += [i[:-1].split(",")]
    
    headers=("CodigoConexao", "Estacao1", "Estacao2", "Distancia", "Velocidade Maxima")
    print("\n\n\n\n\n---------------------- Conexoes Criadas ----------------------")
    print(tabulate(myList2,headers,tablefmt="fancy_grid"))
    print("------------------------------------------")







#----------------------------- Listar Estacoes ---------------------------------

def listarEstacoes():

    try:
            f = open("EstacoesCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Estacoes Criadas!")
            print("-------------------------")
    
    
    if(ficheiro == True):
        myfile = open("EstacoesCriadas.txt", "r")
        myData = myfile.readlines()
        myList = []

        for i in myData:
            myList += [i[:-1].split(",")] 
    
        headers=("Estacao", "Codigo Estacao", "Latitude", "Longitude")
        print("\n"*27)
        print("-------------------------- Estacoes --------------------------")
        print(tabulate(myList,headers,tablefmt="fancy_grid"))
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")



#----------------------------- Adicionar Comboio ---------------------------------



def adicionarComboio():
    print("\n" * 35)
    resp = 1

    while(resp == 1):
        
        try:
            f = open("ComboiosCriados.txt")
            f.close()
            podeVerificar = True;
        except:
            podeVerificar = False;
            

        
        print("\n\n--------------------- Adicionar Comboio ---------------------")
        
        myList =[]
        
        if(podeVerificar == True):
            myfile = open("ComboiosCriados.txt", "r")
            myData = myfile.readlines()
                    
        
            for i in myData:
                myList += [i[:-1].split(",")]

            
        myList = str(myList)
        numSerie = str(random.randint(10000,99999))
        numSerie = str(numSerie)

        if(numSerie in myList):
            while(numSerie in myList):
                numSerie = str(random.randint(10000,99999))
        
        
        
                
        print("Numero de Serie: " + numSerie)
        modelo = input("Modelo: ")
        vel = input("Velocidade Maxima: ")
        cap = input("Numero Maximo de Passageiros: ")
        resp = 0

        while(resp != "1" and resp != "2" and resp != "3" and resp != "4"):
            print("\n---- Tipo de Serviço do Comboio ----")
            print("1 - Urbano")
            print("2 - Regional")
            print("3 - Inter-Cidades")
            print("4 - Alfa Pendular")
            print("-------------------------------------")        
            resp = input("Escolha: ")      
            if(resp == "1"):
                servico = "Urbano"
            elif(resp == "2"):
                servico = "Regional"
            elif(resp == "3"):
                servico = "Inter-Cidades"
            elif(resp == "4"):
                servico = "Alfa Pendular"           
        
        print("Tipo de Servico: " ,servico)
        
        
    
        
        lista = numSerie +  "," + modelo +  "," + vel +  "," + cap +  "," + servico

        

        myfile = open("ComboiosCriados.txt", "a")
        myfile.write(lista + "\n")
        myfile.close()

        print("\nDeseja Inserir mais Comboios? ")
        print(" 1 - Sim")
        print(" 2 - Nao")
        resp = int(input("Escolha: "))    
    
        if(resp == 2):
            resp += 1




    
#----------------------------- Listar Comboios ---------------------------------
            
    
def listarComboios():

    try:
            f = open("ComboiosCriados.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Comboios Criados!")
            print("-------------------------")

    if(ficheiro == True):
        myfile = open("ComboiosCriados.txt", "r")    
        myData = myfile.readlines()
        myList = []
        linhas = len(myData)

        for i in myData:
            myList += [i[:-1].split(",")] 
    
        headers=("Numero Serie", "Modelo", "Velocidade Max", "Capacidade", "Servico")
        print("\n"*27)
        print("---------------------------------- Comboios ----------------------------------")
        print(tabulate(myList,headers,tablefmt="fancy_grid"))
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")



#----------------------------- Adicionar Linhas ---------------------------------


def adicionarLinhas():
    print("\n"*37)
    myfile = open("EstacoesCriadas.txt", "r")    
    myData = myfile.readlines()    
    myfile.close()        
    linhas = len(myData)
    podeVerificar = True
    try:
            f = open("LinhasCriadas.txt")            
            f.close()            
    except:            
            podeVerificar = False
            codLinha = str(random.randint(0,999))  

    if(podeVerificar == True):
        myList2 = []

        myfile2 = open("LinhasCriadas.txt", "r")    
        myData2 = myfile2.readlines()    
        myfile2.close() 

        for i in myData2:
            myList2 += [i[:-1].split(",")] 
        
        codLinha = str(random.randint(0,999))        
        myList2 = str(myList2)
        
        if(codLinha in myList2):
            while(codLinha in myList2):
                print("lixoo")
                codLinha = str(random.randint(0,999))
                print(codLinha)
            
                

        
    print("\n\n--------------------- Adicionar Linha ---------------------")
    print("Codigo Linha: ", codLinha)
    nomeLinha = input("Introduza o nome da Linha: ")

    
    
    
  
    #editado

    
    
    myfile = open("EstacoesConexoes.txt", "r")
    myData2 = myfile.readlines()
    myfile.close()    
 
    myListConexoes = []
    myList = []
    myList2 = []

    
    
    for i in myData2:        
        myListConexoes += [i[:-1].split(",")]
        
   
        
   

    for n in myListConexoes:        
        myList += [[n[1]]]

    for n in range(1,len(myList)+1):        
        myList[n-1]=[n]+myList[n-1]

    print("\n" * 35)
    print("-------------------------- Estacao de Partida --------------------------")
    print(tabulate(myList,headers=["Numeros", "Estacao Partida"],tablefmt="fancy_grid"))
    


    op = 3
    print("\n--------------------------")
    print("Não encontra a sua estacao?")
    print("1 - Mudar de Estacoes")
    print("2 - Continuar")
    print("--------------------------")
    op = input("Escolha: ")

    

    if(op == 1):
        for n in myListConexoes:        
            myList2 += [[n[2]]]

        for num in range(1,len(myList)+1):
            myList[num-1]=[num]+myList[num-1]

        for num in range(1,len(myList2)+1):
            myList2[num-1]=[num]+myList2[num-1]


        #--------------------------- 2 -----------------------------------------

        print("--------------------")
        print(myList)
        print("--------------------")
        
        print("\n"*27)
        print("-------------------------- Estacao de Partida (2) --------------------------")        
        print(tabulate(myList2,headers=["Numeros", "Estacao Partida"],tablefmt="fancy_grid"))
        num2 = int(input("\nIntroduza o numero da estacao de Partida: "))
        
        if(num2 <= 0 or num2 > len(myList2)):        
            while(num2 <= 0 or num2 > len(myList2)):                
                num2 = int(input("\nIntroduza o numero da estacao de Partida: "))

        num2Real = num2 
            
        estacaoPartida = myList2[num2-1][0]    
        estacaoPartida_Linhas = myList2[num2-1][1]
        estacaoPartida_Nome = myList2[num2-1][1]
        estacaoPartida_Nome = str(estacaoPartida_Nome)
        
        
        myList = []
        
        print("estacao ->", estacaoPartida_Nome)
        
        for n in myListConexoes:            
            if(estacaoPartida_Nome in n[2]):
                myList += [[n[1]]]     
        
        for num in range(1,len(myList)+1):
            myList[num-1]=[num]+myList[num-1]
        
        
            
        print("\n"*27)
        print("-------------------------- Estacao de Chegada (2) --------------------------")
                
           
        print(tabulate(myList,headers=["Numeros", "Estacao Chegada"],tablefmt="fancy_grid"))
        num1 = int(input("\nIntroduza o numero da estacao de Chegada: "))

        if(num1 <= 0 or num1 > len(myList)):            
            while(num1 <= 0 or num1 > len(myList)):                
                num1 = int(input("\nIntroduza o numero da estacao de Chegada: "))

        estacaoChegada = myList[num1-1][0]
        estacaoChegada_Nome = myList[num1-1][1]
        estacaoChegada_Nome = str(estacaoChegada_Nome)
        print(estacaoChegada)



    #-----------------------------------------------------------------------

   
    
           
    else:

        
        myList = []
        for num in range(1,len(myList)+1):
            myList[num-1]=[num]+myList[num-1]

        for num in range(1,len(myList2)+1):
            myList2[num-1]=[num]+myList2[num-1]
            
        for n in myListConexoes:        
            myList += [[n[1]]]

        print("\n"*27)        
        print("-------------------------- Estacao de Partida --------------------------")
    
        for n in range(1,len(myList)+1):        
            myList[n-1]=[n]+myList[n-1]
            
        print(tabulate(myList,headers=["Numeros", "Estacao Partida"],tablefmt="fancy_grid"))
        num1 = int(input("\nIntroduza o numero da estacao de Partida: "))

        if(num1 <= 0 or num1 > len(myList)):        
            while(num1 <= 0 or num1 > len(myList)):
                num1 = int(input("\nIntroduza o numero da estacao de Partida: "))
    
        
        estacaoPartida = myList[num1-1][1]    
        estacaoPartida_Linhas = myList[num1-1][1]
        estacaoPartida_Nome = myList[num1-1][1]
        estacaoPartida_Nome = str(estacaoPartida_Nome)     
        
       
    
        for n in myListConexoes:            
            if(estacaoPartida_Nome in n[1]): #conexoes                     
                myList2 += [[n[2]]]
            
            
        
    
             
        print("\n"*27)
        print("-------------------------- Estacao de Chegada --------------------------")
        
        for n in range(1,len(myList2)+1):
            myList2[n-1]=[n]+myList2[n-1]
    
        print(tabulate(myList2,headers=["Numeros", "Estacao Chegada"],tablefmt="fancy_grid"))
        num2 = int(input("\nIntroduza o numero da estacao de Chegada: "))

        if(num2 <= 0 or num2 > len(myList2)):            
            while(num2 <= 0 or num2 > len(myList2)):                
                num2 = int(input("\nIntroduza o numero da estacao de Chegada: "))

        estacaoChegada = myList2[num1-1][0]
        estacaoChegada_Nome = myList2[num1-1][1]
        estacaoChegada_Nome = str(estacaoChegada_Nome)
        print(estacaoChegada)

    




    print("\n" * 27)
    print("------------------------")
    print("Estacao de Partida: ", estacaoPartida_Nome)
    print("Estacao de Chegada: ", estacaoChegada_Nome)
    print("------------------------\n\n\n")
    resp = 0

    while(resp != "1" and resp != "2" and resp != "3" and resp != "4"):
        print("\n---- Tipo de Serviço do Comboio ----")
        print("1 - Urbano")
        print("2 - Regional")
        print("3 - Inter-Cidades")
        print("4 - Alfa Pendular")
        print("-------------------------------------")        
        resp = input("Escolha: ")      
        if(resp == "1"):
            servico = "Urbano"
        elif(resp == "2"):
            servico = "Regional"
        elif(resp == "3"):
            servico = "Inter-Cidades"
        elif(resp == "4"):
            servico = "Alfa Pendular"           
        
    print("Tipo de Servico: " + servico)
    
    
    
    
    
    lista = codLinha + "," + nomeLinha + "," + estacaoPartida_Nome + "," + estacaoChegada_Nome + "," + servico
    lista = str(lista)

    
    
    myfile = open("LinhasCriadas.txt", "a")
    myfile.write(lista + "\n")    
    myfile.close()    
    

    


#----------------------------- Listar Linhas ---------------------------------



def listarLinhas():

    try:
            f = open("LinhasCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Linhas Criadas!")
            print("-------------------------")
    

    if(ficheiro == True):
        myfile = open("LinhasCriadas.txt", "r")    
        myData = myfile.readlines()
        myList = []
    

        for i in myData:
            myList += [i[:-1].split(",")] 
    
        headers=("Codigo Linha", "Nome Linha", "Estacao1", "Estacao2", "Servico")
        print("\n"*27)
        print("-------------------------------- Linhas --------------------------------")
        print(tabulate(myList,headers,tablefmt="fancy_grid"))
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")


#----------------------------- Adicionar Viagem ---------------------------------
    

def adicionarViagem():
    
    

    try:
            f = open("LinhasCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Linhas Criadas!")
            print("-------------------------")
    

    if(ficheiro == True):
        myfile = open("LinhasCriadas.txt", "r")    
        myData = myfile.readlines()
        myfile.close()

        myList = []        
            
        for i in myData:
            myList += [i[:-1].split(",")]

        for n in range(1,len(myList)+1):
            myList[n-1]=[n]+myList[n-1]

        

    
        idViagem = str(random.randint(0,9999))
        idViagem = str(idViagem)

        if(idViagem in myList):
            while(idViagem in myList):
                idViagem = str(random.randint(10000,99999))

        
        
        
        headers=("Numeros", "Codigo Linha", "Nome Linha", "Estacao1", "Estacao2", "Servico")
        print("\n"*27)
        print("-------------------------------- Linhas --------------------------------")
        print(tabulate(myList,headers,tablefmt="fancy_grid"))

        print("\n---------------------------\n")
        num = int(input("Introduza o numero para selecionar o Codigo da Linha: "))

        CodigoLinhaSelected = myList[num-1][1]
        servicoLinhaSelected = myList[num-1][5]
        print(servicoLinhaSelected)

        print("\n" * 27)
        print("-----------------------------\n")
        print("Codigo Linha Selecionado: ", CodigoLinhaSelected)
        print("\n-----------------------------\n")
        
        myList = []
        myListComboios = []
        
        myfile = open("ComboiosCriados.txt", "r")
        myData = myfile.readlines()
        myfile.close()
        
        
        for i in myData:            
            myListComboios += [i[:-1].split(",")]
        

        
       
        
        for i in myListComboios:
            if(str(servicoLinhaSelected) in str(i)):                
                myList += [i]

        for n in range(1,len(myList)+1):
            myList[n-1]=[n]+myList[n-1]

        
            
        print("--> ", str(myList))

        if(str(myList) == "[]"):
            print("\n" * 37)
            print("-----------------------------------------------")
            print("Nao tem Comboios disponiveis para esse Servico")
            print("-----------------------------------------------\n\n\n")
            voltarMenu = input("\n\nDigite algo para voltar ao menu...")
        else:
        
            headers=("Numero", "Numero Serie", "Modelo", "Velocidade Max", "Capacidade", "Servico")
            print("\n"*6)
            print("-------------------------------- Comboios --------------------------------")
            print(tabulate(myList,headers,tablefmt="fancy_grid"))

            print("\n---------------------------\n")
            num = int(input("Introduza o numero para selecionar o Numero de Serie do Comboio: "))

            total = 0
        
            numSerieSelected = myList[num-1][1]
            print("\n" * 40)
            print("---------------------------------\n")
            print("Identificador de Viagem: ", idViagem)
            print("Codigo Linha Selecionado: ", CodigoLinhaSelected)
            print("Codigo Serie do comboio Selecionado: ", numSerieSelected)
            horaPartida = input("Introduza a Hora de Partida (00:00): ")             
            horaChegada = input("Introduza a Hora de Chegada (00:00): ")
            dia = input("Introduza o dia da viagem (00): ")
            mes = input("Introduza o mes da viagem (00): ")
            ano = input("Introduza o ano da viagem (0000): ")
            NumeroPassageiros = int(input("Introduza a lotacao atual da viagem: "))
            print("\n--------------------------------\n")
        
            diaViagem = dia + "/" + mes + "/" + ano
        
            lista  =str(idViagem) + "," + str(CodigoLinhaSelected) + "," + str(numSerieSelected) + "," + str(horaPartida) + "," + str(horaChegada) + "," + str(diaViagem) + "," + str(NumeroPassageiros)
            lista = str(lista)
        
            myfile = open("ViagensCriadas.txt", "a")
            myfile.write(lista + "\n")
            myfile.close()
    
        








#----------------------------- Listar Viagens ---------------------------------


def listarViagens():

    try:
            f = open("ViagensCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Viagens Criadas!")
            print("-------------------------")
    

    if(ficheiro == True):
        myfile = open("ViagensCriadas.txt", "r")    
        myData = myfile.readlines()
        myList = []
    

        for i in myData:
            myList += [i[:-1].split(",")] 
    
        headers=("Id Viagem", "Codigo Linha", "Numero Comboio", "Partida", "Chegada", "Dia", "Passageiros")
        print("\n"*37)
        print("-------------------------------- Viagens --------------------------------")
        print(tabulate(myList,headers,tablefmt="fancy_grid"))
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")






#----------------------------- Listar Viagens Linha ------------------------------
        

def listarViagensPorLinha():

    try:
            f = open("ViagensCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Viagens Criadas!")
            print("-------------------------")
    
    try:
            f = open("LinhasCriadas.txt")
            f.close()
            ficheiro2 = True;
    except:
            ficheiro2 = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Linhas Criadas!")
            print("-------------------------")

    if(ficheiro2 == True and ficheiro == True):
        myfile = open("LinhasCriadas.txt", "r")    
        myData = myfile.readlines()
        myList = []

        
        for i in myData:
            myList += [i[:-1].split(",")]

        for n in range(1,len(myList)+1):
            myList[n-1]=[n]+myList[n-1]
        
        headers=("Numero", "Codigo Linha", "Nome Linha", "Estacao1", "Estacao2", "Servico")
        print("\n"*27)
        print("---------------------- Procurar Viagens por Linhas ----------------------")
        print(tabulate(myList,headers,tablefmt="fancy_grid"))
        print("--------------------------------------------------------------------------\n\n")

        num1 = int(input("Introduza o numero para selecionar o codigo de linha: "))
        
        if(num1 <= 0 or num1 > len(myList)):            
            while(num1 <= 0 or num1 > len(myList)):                
                num1 = int(input("\nIntroduza o numero para selecionar o codigo de linha: "))

        codLinhaSelected = myList[num1-1][1]
        print(codLinhaSelected)
        
        myList = []

        myfile = open("ViagensCriadas.txt", "r")    
        myData = myfile.readlines()
        myList = []
        myList2 = []

        for i in myData:
            myList += [i[:-1].split(",")]

        for n in myList:
            if(codLinhaSelected in n):
                myList2 += [n]
        
        
        headers=("Id Viagem", "Codigo Linha", "Numero Comboio", "Partida", "Chegada", "Dia", "Passageiros")
        print("\n"*37)
        print("------------------------------------ Viagens da Linha ------------------------------------")
        print(tabulate(myList2,headers,tablefmt="fancy_grid"))
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")
        




#----------------------------- Procurar Comboio Por modelo ou Passageiros ------------------------------




def procurarComboios():

    try:
            f = open("ComboiosCriados.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Comboios Criados!")
            print("-------------------------")

    if(ficheiro == True):
        myfile = open("ComboiosCriados.txt", "r")    
        myData = myfile.readlines()
        myList = []
        linhas = len(myData)

        for i in myData:
            myList += [i[:-1].split(",")]

        print("-----------------------------------")
        print("Como Deseja Procurar o seu Comboio?")
        print("1 - Modelo")
        print("2 - Numero de Passageiros")
        print("-----------------------------------")
        op = int(input("Escolha: "))

        if(op >2 or op<1):
            while(op >2 or op<1):
                op = int(input("Escolha: "))
        print("\n"*37)

        
        if(op == 1):
            print("---------- Modelo ----------")
            procura = str(input("Introduza o Modelo do comboio: "))

            if(procura not in str(myList)):
                while(procura not in str(myList)):
                    procura = str(input("O modelo " + procura + " nao existe: "))
            
            myList2 = []
            
            for no in myList:                
                if(procura in str(no[1])):                   
                   myList2 += [no]

            
            
        if(op == 2):
            print("---------- Numero de Passageiros ----------")
            procura = str(input("Introduza o numero de passageiros: "))

            if(procura not in str(myList)):
                while(procura not in str(myList)):
                    procura = str(input("Nao existe nenhum comboio com um maximo de " + procura +" passageiros: "))

            myList2 = []
            
            for no in myList:                
                if(procura in str([no[3]])):                   
                   myList2 += [no]

            
                           
            
                   
        headers=("Numero Serie", "Modelo", "Velocidade Max", "Capacidade", "Servico")
        print("\n"*27)
        print("---------------------------------- Comboios ----------------------------------")
        print(tabulate(myList2,headers,tablefmt="fancy_grid"))        
        print("------------------------------------------------------------------------------\n\n")
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")





#----------------------------- Procurar Viagens por Estacoes ------------------------------




def procurarViagens():

    try:
            f = open("LinhasCriadas.txt")
            f.close()
            ficheiro2 = True;
    except:
            ficheiro2 = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Linhas Criadas!")
            print("-------------------------")


    try:
            f = open("ViagensCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Viagens Criadas!")
            print("-------------------------")
    

    if((ficheiro == True) and (ficheiro2 == True)):
        myfile = open("LinhasCriadas.txt", "r")    
        myData = myfile.readlines()
        myList = []
        
        for i in myData:
            myList += [i[:-1].split(",")]


        
        myfile = open("ViagensCriadas.txt", "r")    
        myData = myfile.readlines()
        myList2 = []
        newLista = []

        for i in myData:
            myList2 += [i[:-1].split(",")]
        

        
        print("\n" *37)
        print("----------------------------------------\n")
        
        estacaoPartida = str(input("Introduza o nome da Estacao de Partida: "))


        listaPartida = []
        listaChegada = []
    
        for i in myList:
            listaPartida += [i[2]]
            listaChegada += [i[3]]

        
        
        if(estacaoPartida not in str(listaPartida)):
            while(estacaoPartida not in str(listaPartida)):
                estacaoPartida = str(input("A Estacao de Partida introduzida nao existe ou nao tem linha: "))
        
        estacaoChegada = str(input("Introduza o nome da Estacao de Chegada: "))
        
        if(estacaoChegada not in str(listaChegada)):
            while(estacaoChegada not in str(listaChegada)):
                estacaoChegada = str(input("A Estacao de Chegada introduzida nao existe ou nao tem linha: "))

        for no in myList:            
            if((estacaoPartida in str(no[2])) and (estacaoChegada in str(no[3]))):
                newLista += [no]
        

        listaCodLinhas = []
        lista = []
        lista2 = []

        for i in newLista:
            listaCodLinhas += [i]            
                
        
        for i in listaCodLinhas:            
            idLinha = i[0]            
            for no in myList2:                
                if(str(idLinha) in str([no[1]])):                  
                    lista += [no]
                    
                    for i in lista:
                        if(i not in lista2):
                            lista2 += [no]
                            
                            
        
        
        
        print("\n" * 37)
        headers=("Id Viagem", "Codigo Linha", "Numero Comboio", "Partida", "Chegada", "Dia", "Passageiros")
        print("----------------------------------------------- Comboios -----------------------------------------------")
        print(tabulate(lista2,headers,tablefmt="fancy_grid")) 
        print("-------------------------------------------------------------------------------------------------------\n\n")
        voltarMenu = input("\n\nDigite algo para voltar ao menu...")
        


#--------------------------------------- Procurar Linhas ----------------------------------------






def procurarLinhas():

    try:
            f = open("LinhasCriadas.txt")
            f.close()
            ficheiro = True;
    except:
            ficheiro = False;
            print("\n\n\n\n-------------------------")
            print("Não tem Linhas Criadas!")
            print("-------------------------")


    
    

    if((ficheiro == True)):
        myfile = open("LinhasCriadas.txt", "r")    
        myData = myfile.readlines()
        myList = []
        myList2 = []


        for i in myData:
            myList += [i[:-1].split(",")]

        print("\n" *37)
        print("----------------------------------------------\n")
        estacao = str(input("Introduza o nome da estacao que quer procurar: "))

        for i in myList:
            if(estacao in str(i)):
                myList2 += [i]

        
        myList2.sort(key=lambda x:int(x[0]))

        if(str(myList2) == "[]"):
            print("\n" * 37)
            print("-----------------------------------------------")
            print("Nao tem Linhas disponiveis")
            print("-----------------------------------------------\n\n\n")
            voltarMenu = input("\n\nDigite algo para voltar ao menu...")
        else:
        
            headers=("Codigo Linha", "Nome Linha", "Estacao1", "Estacao2", "Servico")
            print("\n"*27)
            print("-------------------------------- Linhas --------------------------------")
            print(tabulate(myList2,headers,tablefmt="fancy_grid"))
            print("------------------------------------------------------------------------\n\n")

            print("-------------------------------------")
            print("Deseja mostrar na forma descendente?")
            print("1 - Sim")
            print("2 - Nao")
            print("-------------------------------------")

            reverse = int(input("Escolha: "))

            if(reverse >2 or reverse<=0):
                while(reverse >2 or reverse<=0):
                    reverse = int(input("Escolha: "))

            if(reverse == 1):
                myList2.reverse()
                print("\n"*37)
                print("-------------------------------- Linhas --------------------------------")
                print(tabulate(myList2,headers,tablefmt="fancy_grid"))
                print("------------------------------------------------------------------------\n\n")
        

            voltarMenu = input("\n\nDigite algo para voltar ao menu...")
