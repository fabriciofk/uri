""" Faça um programa que leia três valores de ponto flutuante: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem base A e altura C.
b) a área do círculo do raio C. (pi = 3,14159)
c) a área do trapézio que tem A e B por base e C por altura.
d) a área do quadrado que possui o lado B.
e) a área do retângulo que possui os lados A e B.

Entrada
O arquivo de entrada contém três valores duplos com um dígito após o ponto decimal.

Resultado
O arquivo de saída deve conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
 sempre com uma mensagem correspondente (em português) e um espaço entre os dois pontos e o valor.
 O valor calculado deve ser apresentado com 3 dígitos após a casa decimal. """

valor = input().split()
valor_de_A = float(valor[0])
valor_de_b = float(valor[1])
valor_de_c = float(valor[2])

triangulo = (valor_de_A * valor_de_c) / 2
circulo = (3.14159 * valor_de_c**2)
trapezio = ((valor_de_A + valor_de_b) * valor_de_c) / 2
quadrado = valor_de_b**2
retangulo =valor_de_A * valor_de_b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
