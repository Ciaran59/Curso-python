from random import*


nombre = input("Ingrese su nombre: ")
numero = randint(1,100)
intentos = 0
adivinado = False


print(f"{nombre} he pensado en un número del 1 al 100, y tendrás 8 intentos para adivinarlo")

for num in range(1,9):
    intentos = num
    numero1 = int(input("Ingrese su numero: "))
    if numero1 < 1 or numero1 > 100:
        print("Ingresa un número entre 1 y 100")
    elif numero1 < numero:
        print("El numero es mayor al que escogiste")
    elif numero1 > numero:
        print("El numero es menor al que escogiste")
    else:
        print("El numero es igual al que escogiste")
        adivinado = True
        print(f"{nombre} has adivinado el número en {intentos} intentos ")
        break

if adivinado == False:
    print("Se te han acabado los intentos para adivinarlo")
