""" Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer
 no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a 
 vírgula, segundo a fórmula:
Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois
 valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.
Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal. """

""" inha1 = input().split(" ")
linha2 = input().split(" ")
x1,y1 = linha1
x2,y2 = linha2
distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1))
 *(float(y2)-float(y1))))
print("%0.4f" %distancia)"""

x1,y1 = input().split()
x2,y2 = input().split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print("{:.4f}".format(distancia))
 

""" distancia1 = (**(x1/y1))
distancia2= (**(x2/y2))
total = distancia1 - distancia2
print(f'diatancia{total:.4}')
 """