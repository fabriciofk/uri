""" Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.
Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”. """

valor = int(input())
valor2 = valor

c100 = valor // 100
valor -=c100 * 100
c50 = valor // 50
valor -= c50 * 50

c20 = valor // 20
valor -=c20 * 20

c10 = valor // 10
valor -= c10 * 10

c5 = valor // 5
valor -= c5 * 5

c2 = valor // 2
valor -= c2 * 2

print(f'{valor2}')
print(f'{c100} nota(s) de R$ 100,00')
print(f'{c50} nota(s) de R$ 50,00')
print(f'{c20} nota(s) de R$ 20,00')
print(f'{c10} nota(s) de R$ 10,00')
print(f'{c5} nota(s) de R$ 5,00')
print(f'{c2} nota(s) de R$ 2,00')
print(f'{valor} nota(s) de R$ 1,00')