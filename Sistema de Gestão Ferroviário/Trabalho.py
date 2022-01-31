import adicionarEstacao as f;
import clear as c
import math;


menu = True

while(menu == True):
    
    print("\n\n\n\n============= Menu =============\n")
    print(" --------- Estacoes ---------\n ")
    print(" 1 - Adicionar Estacao")
    print(" 2 - Adicionar Ligacoes entre estacoes")
    print(" 3 - Ver Estaçoes")
    print("\n")
    print(" --------- Comboios ---------\n ")    
    print(" 4 - Adicionar Comboios")    
    print(" 5 - Ver Comboios")
    print("\n")
    print(" --------- Linhas ---------\n ")
    print(" 6 - Adicionar Linha")    
    print(" 7 - Ver Linha")    
    print("\n")
    print(" --------- Viagens ---------\n ")
    print(" 8 - Adicionar Viagem")
    print(" 9 - Ver Viagem")
    print(" 10 - Ver Viagem por linha")
    print("\n")
    print(" --------- Procurar ---------\n ")
    print(" 11 - Comboios por Modelo/Passageiros")
    print(" 12 - Viagens por Estacoes")
    print(" 13 - Linhas por Estacoes")
    print(" 0 - Sair")
    print("\n")
    print("================================")
    op = int(input("Escolha: "))

    if(op == 1):    
        f.adicionarEstacao();
    elif(op == 2):
        f.adicionarLigacao();
    elif(op == 3):
        f.listarEstacoes();
    elif(op == 4):
        f.adicionarComboio();    
    elif(op==5):
        f.listarComboios();
    elif(op==6):
        f.adicionarLinhas();
    elif(op==7):
        f.listarLinhas();
    elif(op==8):
        f.adicionarViagem();
    elif(op==9):
        f.listarViagens();
    elif(op==10):
        f.listarViagensPorLinha();
    elif(op==11):
        f.procurarComboios();
    elif(op==12):
        f.procurarViagens();
    elif(op==13):
        f.procurarLinhas(); 
    elif(op == 0):
        menu = False
        
