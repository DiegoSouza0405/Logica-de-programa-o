#Condicionais
"""
1)If (se)
2)else (então)
3)elif (else + if) (senão)
"""
#Exemplo
# informacao_usuario = str(input('Você deseja "Entrar"ou "Sair"do programa?'))
# if informacao_usuario == "Entrar":
# print ("Sistema acessado com sucesso!")
# else:
# print("Você não acessou o sistema!")

# entrada_usuario = str(input('Digite "E" para entrar' 'ou "S" para sair:'))
# if entrada_usuario == "E":
#     print("Bem vindo ao Sistema!")
# elif entrada_usuario == "S":
#     print("Você saiu do Sistema!")
# else:
#     print('Você não digitou nem "E" e nem "S".')

"""
Operadores Relacionais (de comparação).
1) Igual: ==
2) Maior: >
3) Menor: <
4) Maior ou igual : >=
5) Menor ou igual: <=
6) Diferente: !=
"""
# #Exemplo
# #Igual
# igual = "a" == "a"
# print(igual)
# igual = 1 == "1"
# print(igual)
# maior  = 2 > 1
# print(maior)
# #menor
# menor = 4 < 1
# print(menor)
# #Maior ou igual
# maior_ou_igual = 6 >= 4
# print(maior_ou_igual)
# #Diferente
# diferente = 1 != "1"
# print(diferente)

"""
Operadores Lógicos

e (and)
X (True) and Y (False) = False
x (False) and Y ( True) = False
X (False) and Y (False) = False
X (True) and Y (True) = True

ou (or)

X (True) or Y (False) = True
X (False) or Y (True) = True
X (True) or Y (True) = True
X (False) or  Y (False) = False

Negação (not)

X (True) not X = False
X (False) not X = True
"""
#and
X = True
Y = True
resultado = X and Y
print(resultado)

#or
X = False
Y = False
resultado = X  or Y
print(resultado)

#not
x = True
x1 = not x
print(x1)

# Passo a Passo

"""
O = é para atribuição
Int - é para numeros inteiros
Float - numeros quebrados
Input - Serve para impultar o programa
C: Os dois pontos servem para dar ponto final


