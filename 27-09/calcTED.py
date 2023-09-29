import datetime

tam = float(input("Informe o tamanho do arquivo em Mb: "))
vel = float(input("Informe o a velocidade do link de internet (Mbps): "))

ted = tam / vel 

print("Tempo estimado de download:", datetime.timedelta(seconds=ted))