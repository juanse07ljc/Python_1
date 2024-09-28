puntaje=int(input("ingresa el valor del puntaje "))

if puntaje >100:
    print("su puntaje es mayor a 100, por favor 101repitalo ")
    puntaje=int(input("ingresa el valor del puntaje"))

if puntaje >= 90:
    print("Excelente")
elif puntaje >= 75:
    print("Bueno")
elif puntaje >= 50:
    print("Regular")
else:
    print("Reprobado")  

