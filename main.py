def menu_opcions():
    print("A continuacion mostranse as opcions de figuras para calcularlle a area")
    print("1...Cadrado")
    print("2...Triangulo")
    print("3...Circulo")
    return input("Escriba unha opcion: ")

def areatriangulo():
    base = int(input("Introduzca la longitud de la base: "))
    altura = int(input("Introduzca la longitud de la altura: "))
    area = base * altura / 2
    return area

def areacadrado():
    lado= int(input("Introduzca una longitud: "))
    area = lado * lado
    print(area)
    return area

def areacirculo(radio):
    area = 3.14 * radio^2
    return area

if menu_opcions() == "Cadrado":
    areacadrado()

if menu_opcions() == "Triangulo":
    areatriangulo()
