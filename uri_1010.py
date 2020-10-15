""" Neste problema, a tarefa é ler o código de um produto 1, o número de unidades do produto 1,
 o preço de uma unidade do produto 1, o código de um produto 2, o número de unidades do produto 2 e
 o preço para uma unidade do produto 2. Após, calcule e mostre o valor a pagar.
Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores:
 dois inteiros e um valor flutuante com 2 dígitos após o ponto decimal.
Resultado
O arquivo de saída deve ser uma mensagem como o exemplo a seguir, onde "Valor a pagar"
 significa Valor a pagar . Lembre-se do espaço após ":" e após o símbolo "R $". O valor deve ser 
 apresentado com 2 dígitos após o ponto. """
###########################################################
""" numero_unidades = []
for i in range(2):
    numeros = input().split()
    quantidade = int(numeros[1])
    preco = float(numeros[2])
    numero_unidades.append([quantidade,preco])
total = 0
print(numero_unidades)
for peca in numero_unidades:
    print(peca)
    total = total + peca[0]*peca[1]
print(f'valor a pagar {total:.2f}')
 """
##################################################################
sub = input().split()
quantidade = int(sub[0])
numero = int(sub[1])
valores = float(sub[2])
total1 = numero * valores

sub2 = input().split()
quantidade2 = int(sub2[0])
numero2 = int(sub2[1])
valores2 = float(sub2[2])
total2 = numero2 * valores2

resultado = total1 + total2
print('VALOR A PAGAR: R$ {:.2F}'.format(resultado))

