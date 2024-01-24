print("¿Quieres ver los años uno a uno o no?")
TAño = input().lower()

if TAño == "si":
    print("Por favor escriba un año cualquiera de 1900 a 2199")
    AEntrada = int(input())
    Año = 1900
    CanABis = 0
    while Año <= AEntrada:
        if Año%4 == 0:
            if Año%100 != 0:
                CanABis = CanABis + 1
                print(Año)
            elif Año%400 == 0:
                    CanABis = CanABis + 1
                    print(Año)
        Año = Año + 1
    print("la cantidad de años bisiestos entre 1900 y " + str(AEntrada))
    print("es de " + str(CanABis))
    print("y el año " + str(AEntrada))
    SerONoSer = "no es bisiesto"
    if AEntrada%4 == 0:
        if AEntrada != 0:
            SerONoSer = "es bisiesto"
        elif AEntrada%400 == 0:
                SerONoSer = "es bisiesto"
else:
     print("Por favor escriba un año cualquiera de 1900 a 2199")
     AEntrada = int(input())
     Año = 1900
     CanABis = (AEntrada - Año)//4
     print("entre " + str(Año) + " y " + str(AEntrada))
     print("hubo " + str(CanABis) + "años bisiestos")
     print("y " + str(AEntrada))
     SerONoSer = "no es bisiesto"
     if AEntrada%4 == 0:
        if AEntrada%100 != 0:
             SerONoSer = "es bisiesto"
        elif AEntrada%400 == 0:
             SerONoSer = "es bisiesto"
print("el año " + SerONoSer)
