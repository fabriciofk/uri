""" #Faça um programa que leia o nome do vendedor, seu salário fixo e o
 valor total da venda feita por ele mesmo no mês (em dinheiro).
#Considerando que esse vendedor recebe 15% sobre todos os produtos vendidos,
#  escreva o vencimento final (total) desse vendedor no
#final do mês,
#com duas casas decimais.
#Não se esqueça de imprimir o final da linha após o resultado, caso contrário você receberá 
# “ Erro de apresentação ”.
#Não se esqueça dos espaços em branco.
#Entrada
#O arquivo de entrada contém um texto (nome do funcionário) e dois valores de precisão dupla,
#que são o salário do vendedor e o valor total vendido por ele.
#Resultado
#Imprime o salário total do vendedor, conforme o exemplo dado.
 """

nome_vendedor= input()
salario= float(input())
total_venda = float(input())
comicao = total_venda * (15/100)
salario_total = salario + comicao
print(f'TOTAL = R$ {salario_total:.2f}')
