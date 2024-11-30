"""the main aidea of this code block is raise x to a x^2"""

def number_check(valor):
    if not isinstance(valor,(int,float)):
        raise ValueError("El valor ingresado debe ser numerico (R)")
    return valor

def potent(valor):
    valor = number_check(valor)
    return valor**2

try:
    valor=float(input("X: "))
    resultado = number_check(valor)
    resultado = potent(valor)
    print(f"{valor}^2 = {resultado}")
except ValueError as e:
    print(f"Error {e}")
    exit(0)


    