import random

def generar_fichas(num_fichas):
    fichas = []
    for i in range(num_fichas):
        fichas.append(random.randint(0, 100))
    return fichas

def realizar_sorteo():
    return [random.randint(0, 100) for _ in range(5)]

def verificar_ganador(fichas, numeros_sorteados):
    for ficha in fichas:
        if ficha in numeros_sorteados:
            return True
    return False


def doblar_apuesta(apuesta):
    return apuesta * 2

saldo = 500
while 0 < saldo < 1000:
    num_fichas = int(input("¿Cuántas fichas quieres comprar? Cada ficha vale 10 pesos. "))
    costo_fichas = num_fichas * 10
    if costo_fichas > saldo:
        print("No tienes suficiente saldo para comprar esa cantidad de fichas.")
        continue
    
    fichas = generar_fichas(num_fichas)
    print(f"Tus fichas son:" , fichas)
    
    numeros_sorteados = realizar_sorteo()
    print("Los números sorteados son:", numeros_sorteados)
    
    if verificar_ganador(fichas, numeros_sorteados):
        saldo += doblar_apuesta(costo_fichas)
        print("¡Felicidades, has ganado! Tu saldo actual es:", saldo)
    else:
        saldo -= costo_fichas
        print("Lo siento, no has ganado esta vez. Tu saldo actual es:", saldo)
