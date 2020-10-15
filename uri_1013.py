""" Faça um programa que leia 3 valores inteiros e apresente o maior deles seguido da mensagem 
"eh o maior". Use a seguinte fórmula:
Entrada
O arquivo de entrada contém 3 valores inteiros.
Resultado
Imprima o maior destes três valores seguido de um espaço e da mensagem “eh o maior”. """
##################################################
""" valores = input().split()
for i in range(4):
    valores_de_a = int(valores[0])
    valores_de_b = int(valores[1])
    valores_de_c = int(valores[2])
valores2 = valores_de_a,valores_de_b,valores_de_c
numero_maior = max(valores2)
print('{} eh o maior',numero_maior)
 """
 ######################################################

""" A, B, C = map(int,input().split( ))
total = max([A,B,C])
print('{} eh o maior'.format(total)) """

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
TOTAL = (max(a,b,c))
print('{} eh o maior'.format(TOTAL)) 