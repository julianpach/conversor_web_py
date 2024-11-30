"""block of code in charge of execute log ops and ln ops or logs in base"""

# definir funcion log # 
import cmath
import math
def logs(valor,log_op):
    match log_op:
        case 1:
            if valor <= 0:
                raise ValueError ("Indefinido")
            return cmath.log10(valor)
        case 2:
            if valor <= 0:
                raise ValueError ("Indefinido") 
            base = int(input("base (n) del log: ")) # logaritmo de x con base definida por el usuario
            if base <= 0 or base == 1:
                raise ValueError ("La base del logaritmo debe ser mayor que 0 y distinta de 1")
            return cmath.log(valor,base)
        case 3:
            if valor <= 0:
                raise ValueError ("Indefinido")
            return cmath.log(valor)
        case 4:
            if valor <= 0:
                raise ValueError ("Indefinido")
            return math.log2(valor)
        case _:
            raise ValueError ("Opcion no valida. Elija una entre 1 - 4")

try:
    valor = float(input("ingrese el valor: "))
    print ("opciones")
    print ("1. logaritmo de x en base 10")
    print ("2. logaritmo de x en base n (definida por el usuario)")
    print ("3. ln de x")
    print ("4. logaritmo de x base 2")
    log_op = int(input("Opcion: "))
    resultado = logs(valor,log_op)
    print(f"Resultado: {resultado}: ")
except ValueError as e:
    print(f"Error {e}")
    exit(1)