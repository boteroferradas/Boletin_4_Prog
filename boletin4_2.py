def menu_opcions():
    print("A continuacion mostranse as opcions de figuras para calcularlle a area")
    print("1...cuadrado")
    print("2...triangulo")
    print("3...circulo")
    eleccion = input("Escriba unha opcion: ")
    return eleccion

def areatriangulo():
    base = int(input("Introduzca la longitud de la base: "))
    altura = int(input("Introduzca la longitud de la altura: "))
    area = base * altura / 2
    print(f"El area del triangulo es: {area}")
    return area

def areacuadrado():
    lado= int(input("Introduzca una longitud: "))
    area = lado * lado
    print(f"El area el cuadrado es: {area}")
    return area

def areacirculo():
    radio = int(input("Introduzca un radio: "))
    area = 3.14 * (radio^2)
    print(f"El area del circulo es: {area}")
    return area

eleccion_menu = menu_opcions()
if eleccion_menu == "cuadrado":
    areacuadrado()
elif eleccion_menu == "triangulo":
    areatriangulo()
elif eleccion_menu == "circulo":
    areacirculo()
