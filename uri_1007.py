#Leia quatro valores inteiros chamados A, B, C e D. 
#Calcule e imprima a diferença dos produtos A e B pelo produto de C e D ~
#(A * B - C * D).
#Entrada
#O arquivo de entrada contém 4 valores inteiros.
#Resultado
#Imprima DIFERENCA (DIFERENÇA em português) com todas as letras maiúsculas, conforme exemplo a seguir,
#com espaço em branco antes e depois do sinal de igual.
A = int(input())
B = int(input())
C = int(input())
D = int(input())
SOMA = A * B - C * D
print(f'DIFERENCA = {SOMA}')
