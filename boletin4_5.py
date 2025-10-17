lista_letras = ["T","R","W","A","G","M","Y","F","P","D","B","N","J","Z","S","Q","V","H","L","C","K","E"]

numerodni = int(input("Introduza o seu DNI: "))
numerodni_a_str = str(numerodni)
letra = numerodni % 23
print(numerodni_a_str + lista_letras[letra])