""" this code is a longitude unit conversor.
    firts we need to define a global rate in m of all the units that we 
     gonna use for this excersice """

def convertir_longitud(valor, unidad_origen, unidad_destino):
    # unidades variables a m para estandarizar #
    if unidad_origen == "m":
        valor = valor * 1
    elif unidad_origen =="km":
        valor = valor * 1000
    elif unidad_origen == "dm":
        valor = valor / 10
    elif unidad_origen == "cm":
        valor = valor / 100
    elif unidad_origen == "mm":
        valor = valor / 1000
    elif unidad_origen == "um":
        valor = valor / 1000000
    elif unidad_origen== "nm":
        valor = valor / 1000000000
    elif unidad_origen in ["a","A","angstrom"]:
        valor = valor / 10000000000
    elif unidad_origen == "legua":
        valor = valor * 4828.03
    elif unidad_origen in ["mi","Mi"]: 
        valor = valor * 1609.344
    elif unidad_origen in ["yd","yardas"]:
        valor = valor * 0.9144
    elif unidad_origen == "ft":
        valor = valor * 0.3048
    elif unidad_origen != "m"or "km"or"dm"or"cm"or"nm"or"mm"or"um"or"A"or "legua"or"mi"or"yd"or"ft":
        raise ValueError("Unidad no valida")
     # ahora configuramos las opciones para tomar los valores estandarizados a m para movrlos a 
     #cualquier unidad de destino"
    if unidad_destino == "km":
        return valor/1000
    elif unidad_destino == "m":
        return valor 
    elif unidad_destino == "dm":
        return valor*10
    elif unidad_destino == "cm":
        return valor*100
    elif unidad_destino == "mm":
        return valor * 1000
    elif unidad_destino == "um":
        return valor*1000000
    elif unidad_destino == "nm":
        return valor*1000000000
    elif unidad_destino in ["a","angstrom"]:
        return valor*10000000000
    elif unidad_destino == "legua":
        return valor * 0.000207
    elif unidad_destino in ["mi","Mi"]:
        return valor*0.000621
    elif unidad_destino in ["yd","yardas"]:
        return valor*1.09
    elif unidad_destino == "ft":
        return valor*3.281
    elif unidad_destino != "m"or "km"or"dm"or"cm"or"nm"or"mm"or"um"or"A"or "legua"or"mi"or"yd"or"ft":
        raise ValueError("Unidad no valida")
    return "ingrese de nuevo"
""" En esta parte del codigo introduje una correccion debido a que no se realizaban los calculos de manera
    correcta. la solucion viene a cuenta de que al usar: 

    elif unidad_origen =="a" or "A" or "anstrong":
        valor = valor / 10000000000
    elif unidad_origen == "mi" or "Mi": 
        valor = valor * 1609.344
    elif unidad_origen == "yd" or "yardas":
    ---------------------------------------------------------
    elif unidad_destino == "A" or "a" or "anstrong":
        return valor*10000000000
    elif unidad_destino == "mi" or "Mi":
        return valor*0.000621
    elif unidad_destino == "yd" or "yardas":
        return valor*1.09
estaba saltandome algunas verificaciones-- la doumentaicion dice que en este caso para una 
accurate and cleaner verification es necesarion arreglar una especie de vector [x,y,z...Nn,n] para que se recorra toda
las variaciones dentro de la lista de variables [x,y,z...Nn,n] y no solamente haga la comprobacion de la primera y al no salir 
correcta siga de largo o en su defecto no no revise las demas del "or"
"""
try:
    valor= float(input("Valor de Longitud: "))
    unidad_origen = input("Introduzca la unidad de longitud de partida,(km,m,dm,cm,mm,um,nm,A,legua,yd,mi,ft): ").lower()
    unidad_destino = input("Introduzca la unidad de longitud de destino,(km,m,dm,cm,mm,um,nm,A,legua,yd,mi,ft): ").lower()
    resultado = convertir_longitud(valor,unidad_origen,unidad_destino)
    print(f"para {valor}{unidad_origen} se obtienen {format(resultado)}{unidad_destino}")
except ValueError as e:
    print(f"Error {e}")
    exit(1)
# esta es una de las funcionalidades de la aplicacion calculadora #