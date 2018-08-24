# ist186415 Francisco Matos

from math import sqrt
from math import ceil 

def gera_chave1(letras): #esta funcao distribui os elementos da cadeia de caracteres em 5 tuplos de 5 elementos cada de modo a formar uma hipotetica matriz quadrada 5*5
    chave=(letras[0:5],letras[5:10],letras[10:15],letras[15:20],letras[20:25]) 
    return chave


def obtem_codigo1(car,chave): #esta funcao devolve ao o numero que corresponde a linha e a coluna do caractere introduzido nos argumentos
    for linha in range(5):
        for coluna in range(5): 
            if car==chave[linha][coluna]:
                codigo=str(linha)+str(coluna)
    return codigo


def codifica1(cad,chave): #esta funcao devolve os numeros que correspondem as linhas e as colunas de todos os caracteres da cadeia utilizando a funcao anterior 
    codigo=''
    for i in cad:
        codigo = codigo + obtem_codigo1(i,chave)
    return codigo 



def obtem_car1(cod,chave): #esta funcao faz o inverso da obtem_codigo1 devolvendo o caracter que esta na linha e coluna introduzidos no argumento da funcao
    for linha in range(5):
        for coluna in range(5):
            if cod==str(linha)+str(coluna):
                caracter=str(chave[linha][coluna])
    return caracter 


def descodifica1(cad_codificada,chave): #esta funcao faz o inverso da codifica1 devolvendo todos os caracteres correspondentes as linhas e colunas introduzidos no argumento
    caracter=''
    for i in range(0,len(cad_codificada),2): #i corresponde as linhas
        j=i+1                                #j corresponde as colunas
        codigo=str(cad_codificada[i])+str(cad_codificada[j])
        caracter=caracter+obtem_car1(codigo,chave)
    return caracter



def gera_chave2(letras): #esta funcao vai agora gerar uma chave partindo de uma sequencia com um numero qualquer de caracteres
    numero_tuplos=ceil(sqrt(len(letras))) #numero de tuplos deve ser a raiz quadrada do menor quadrado perfeito não inferior ao comprimento da sequencia
    numero_elementos_tuplos=ceil(len(letras)/numero_tuplos) #numero de elementos de cada tuplo (exceto o ultimo) deve ser o numero inteiro mais aproximado e nao inferior ao quociente da divisao entre o tamanho da sequencia e o numero de tuplos
    chave=()
    for i in range(0,len(letras),numero_elementos_tuplos):
        chave=chave+((letras[i:i+numero_elementos_tuplos]),)
    return chave
        

    
def obtem_codigo2(car,chave): #esta funcao faz o mesmo que a obtem_codigo1 mas tem em conta o numero de tuplos da chave e se o argumento introduzido pertence a chave
    for linha in range(0,len(chave)):
        for coluna in range(0,len(chave[linha])):
            if car==chave[linha][coluna]:
                codigo=str(linha)+str(coluna)
                return codigo           
    for linha in range(0,len(chave)):
        for coluna in range(0,len(chave[linha])):
            if car!=chave[linha][coluna]:
                return 'XX'

def codifica2(cad,chave): #esta funcao faz o mesmo que a codifica1 mas utiliza a obtem_codigo2
    codigo=''
    for i in cad:
        codigo=codigo+obtem_codigo2(i,chave)
    return codigo
            

def obtem_car2(cod,chave): #esta funcao faz o mesmo que a obtem_car1 mas tem em conta o numero de tuplos da chave e se o argumento introduzido pertence a chave
    for linha in range(len(chave)):
        for coluna in range(len(chave[linha])):
            if cod == str(linha)+str(coluna):
                caracter = str(chave[linha][coluna])
                return caracter
    for linha in range(len(chave)):
        for coluna in range(len(chave[linha])):
            if cod == 'XX':
                return '?'
            
def descodifica2(cad_codificada,chave): #esta funcao faz o mesmo que a descodifica1 mas utiliza a obtem_car2
    caracter=''
    for i in range(0,len(cad_codificada),2): #i corresponde as linhas
        j=i+1                                #j corresponde as colunas
        codigo=str(cad_codificada[i])+str(cad_codificada[j])
        caracter=caracter+obtem_car2(codigo,chave)
    return caracter