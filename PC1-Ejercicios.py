# Ejercicio 1
nombre=input("Introduzca su nombre: ")
print(f"Hola {nombre}")

# Ejercicio 2
consumo=int(input("Introduzca su consumo de hoy: "))
propina=int(input("Introduzca el porcentaje de propina que desea dejar: "))
propina_final=int(consumo*propina/100)
print(f"La propina que dejará es {propina_final}")


# Ejercicio 3
peso_payaso=int(112)
peso_muñeca=int(75)
cantidad_payasos=int(input("Introduzca la cantidad de payasos vendidos: "))
cantidad_muñecas=int(input("Introduzca la cantidad de muñecas vendidas: "))
peso_total=int(peso_payaso*cantidad_payasos+peso_muñeca*cantidad_muñecas)
print(f"El peso total del paquete enviado es de {peso_total:,} gramos")


# Ejercicio 4
entero_positivo=int(input("Introduzca un número entero positivo: "))
suma=int(entero_positivo*(entero_positivo+1)/2)
print(f"{suma:,}")


# Ejercicio 5
shows_musicales=int(input("Introduzca el número de shows musicales que vio en el ultimo año: "))
p = 3
shows_musicales > p



# Ejercicio 6
edad=int(input("Introduzca su edad: "))
if edad<4 :
    print('Puedes entrar gratis')
elif 4<edad<18:
    print('Debes pagar $5')
else:
    print('Debes pagar $10')


# Ejercicio 7
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

print("Menú de opciones:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

opcion = input("Elija una opción: ")

if opcion == '1':
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es igual a {suma}")
elif opcion == '2':
    resta = num1 - num2
    print(f"La resta de {num1} y {num2} es igual a {resta}")
elif opcion == '3':
    multiplicacion = numero1 * numero2
    print(f"La multiplicación de {num1} y {num2} es igual a {multiplicacion}")
else:
    print("Opción inválida.")


# Ejercicio 8
hora = input("Introduzca la hora en formato HH:MM: ")
hora2 = hora.split(':')

if len(hora2) != 2:
    print("Formato de hora incorrecto. Debe ser HH:MM.")
else:
    horas, minutos = map(int, hora2)

rango_desayuno = range(7, 9)
rango_almuerzo = range(12, 14)
rango_cena = range(18, 20)

if horas in rango_desayuno:
    print("Es hora del desayuno.")
elif horas in rango_almuerzo:
    print("Es hora del almuerzo.")
elif horas in rango_cena:
    print("Es hora de la cena.")
else:
    print("Hora incorrecta.")


#Ejercicio 9
lista1 = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista1[::-1]
print(lista_invertida)


#Ejercicio 10
colores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

del colores[0]
del colores[3]
del colores[3]

print(colores)


# Ejercicio 11
lista_inicial = [1, 1, 2, 3, 4, 4, 5, 1]

conjunto = set(lista_inicial)
lista_nueva= list(conjunto)

print(lista_nueva)


# Ejercicio 12

tipo = input("Introduce el tipo de archivo: ")

if ".gif" in tipo.lower():
    print("image/gif")
elif ".jpg" in tipo.lower():
    print("image/jpg")
elif ".jpeg" in tipo.lower():
    print("image/jpeg")
elif ".png" in tipo.lower():
    print("image/png")
elif ".pdf" in tipo.lower():
    print("application/pdf")
elif ".txt" in tipo.lower():
    print("text/plain")
elif ".zip" in tipo.lower():
    print("application/zip")
else:
    print("application/octet-stream")
