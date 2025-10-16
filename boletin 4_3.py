def numero_a_letras_simple(numero):

    unidades = {
        1: 'un', 2: 'dous', 3: 'tres', 4: 'catro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'
    }

    dieces = {
        10: 'dez', 11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince',
        20: 'vinte', 30: 'trinta', 40: 'corenta', 50: 'cincuenta',
        60: 'sesenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa'
    }

    if numero in dieces:
        return dieces[numero]
    if numero in unidades:
        return unidades[numero]

    if 16 <= numero <= 19:
        unidad = numero % 10
        return 'deza' + unidades[unidad]

    if 21 <= numero <= 29:
        unidad = numero % 10
        return 'vinte e ' + unidades[unidad]

    if numero > 29:
        decena = (numero // 10) * 10
        unidad = numero % 10
        if unidad > 0:
            return f"{dieces[decena]} e {unidades[unidad]}"
        return dieces[decena]

while True:
    entrada = input("Introduce un número entre 1 e 99: ")
    num = int(entrada)

    if 1 <= num <= 99:
        resultado = numero_a_letras_simple(num)
        print(f"O número {num} escríbese: \"{resultado.capitalize()}\"")
        break  # Salir del bucle
    else:
        print("O número debe estar entre 1 e 99. Tenta de novo.")
