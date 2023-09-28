#Código para calcular o tempo estimado de download, pede para o usuário inserir o tamanho do arquivo e a velocidade da internet

import datetime #importação de funções de data e hora

tam = float(input("Informe o tamanho do arquivo em Mb: "))
vel = float(input("Informe o a velocidade do link de internet (Mbps): "))

#calculo do tempo em segundos
ted = tam / vel

#print formatado, a função datetime.timedelta(seconds=~segundos~) converte o tempo em segundos em formtado de horas "00:00:00"
print("Tempo estimado de download:", datetime.timedelta(seconds=ted))
