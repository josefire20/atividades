list = []
cotinua = True

while cotinua:
    nome = input('Informe seu nome:')
    peso = float(input('Informe seu peso:'))
    idade = int(input('Informe sua idade:'))
    altura = float(input('informe sua altura:'))

    imc = peso / (altura * altura)

    print('%.2f' %imc)

    resutado = ''

    if imc < 16:
       resutado = 'Baixo peso Grau I'
    elif imc < 16.99:
        resutado = 'Baixo peso Grau II'
    elif imc < 18.49:
        resutado = 'Baixo peso Grau III'
    elif imc < 24.99:
        resutado ='Peso adequado'
    elif imc < 29.99:
        resutado = 'Sobrepeso'
    elif imc < 34.99:
        resutado = 'Obesidade grau I'
    elif imc < 39.99:
        resutado = 'Obesidade grau II'
    else:
        resutado = 'Obesidade grau III'

    list.append([nome,peso,idade,altura, resutado])
    
    cotinua = input("deseja cotinuar?") == "s"

for pesso in list:
    print((pesso[0])+ " - " +str(pesso[2]) +"-" +str(pesso[4]))