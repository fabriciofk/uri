#############################################
#valor inicial = 3
#115380
#2819311
#23456
##################################################
numero = int(input())#pegando um valor:

for i in range(1,numero+1):# vai pega o valor e somar
    leds = 0
    x = input()
    for i in range(0,len(x)):
        if x[i] == '1':
            leds = leds + 2
        if x[i] == '2':
            leds = leds + 5
        if x[i] == '3':
            leds = leds + 5
        if x[i] == '4':
            leds = leds + 4
        if x[i] == '5':
            leds = leds + 5
        if x[i] == '6':
            leds = leds + 6
        if x[i] == '7':
            leds = leds + 3
        if x[i] == '8':
            leds = leds + 7
        if x[i] == '9':
            leds = leds + 6
        if x[i] == '0':
            leds = leds + 6
    print('{} leds'.format(leds))