ventas = int(input("Introduze o numero de ventas: "))

if ventas <= 100:
    print("Baja prioridad")
elif ventas > 100 and ventas <= 500:
    print("Media prioridad")
elif ventas > 100 and ventas <= 1000:
    print("Alta prioridad")
elif ventas > 1000:
    print("Primera necesidad")