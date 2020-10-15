#A fórmula para calcular a área de uma circunferência é definida como A = π. R 2 .
#  Considerando este problema que π = 3,14159 :
#Calcule a área usando a fórmula fornecida na descrição do problema.
#Entrada
#A entrada contém um valor de ponto flutuante (precisão dupla), que é a variável R .
#Resultado
#Apresente a mensagem "A =" seguida do valor da variável, como no exemplo abaixo,
#  com quatro casas decimais após a vírgula. Use todas as variáveis ​​de precisão dupla.
#  Como todos os problemas,
#  não se esqueça de imprimir o final da linha após o resultado, caso contrário,
#  receberá "Erro de apresentação".
#Amostras de entrada	Amostras de saída
#2.00
#A=12.5664
#100.64
#A=31819.3103
#150.00
#A=70685.7750

R = float(input())
n = 3.14159
A = n * R ** 2
print(f'A={A:.4f}')
