""" Calcule o consumo médio de um carro levando em consideração a distância total percorrida (em Km)
e o total de combustível gasto (em litros).
Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total
(em Km) e o segundo é um número de ponto flutuante Y  representando o total de combustível gasto,
com um dígito após a casa decimal.
Resultado
Apresente um valor que represente o consumo médio de um carro com 3 dígitos após a vírgula,
seguido da mensagem “km / l”. """

###################################################
"""round serve para arendondar um valor: no primeiro parametro
recebe a conta, e no segundo recebe a quantidade de digitos apos a virgula."""
##########################################################

def main():
    km = float(input())
    litros = float(input())
    consumo = round(km / litros, 3)
    print(f'{consumo} km/l')


if __name__ == "__main__":
    main()

