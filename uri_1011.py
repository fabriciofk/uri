""" Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).
A fórmula para calcular o volume é: (4/3) * pi * R 3 . Considere (atribua) para pi o valor 3,14159.
Dica: Use (4 / 3.0) ou (4.0 / 3) em sua fórmula, porque algumas linguagens (incluindo C ++) assumem que
o resultado da divisão entre dois inteiros é outro inteiro. :)
Entrada
A entrada contém um valor de ponto flutuante (precisão dupla).
Resultado
A saída deve ser uma mensagem "VOLUME" como o exemplo a seguir com um espaço antes e depois 
do sinal de igual. O valor deve ser apresentado com 3 dígitos após a vírgula decimal. """

R = float(input())
pi = 3.14159
calculo = (4/3) * pi * R **3
print('VOLUME = {:.3f}'.format(calculo))

