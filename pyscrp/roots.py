"""block of code that define a function thar raise to 0.5 each introoduced X"""
import cmath
# creamos una definicion de funcion que se llamara en la app general #
"""def roots(valor):
    if valor < 0:
        raise ValueError ("Entrada no valida")#esta version solo da valores para positivos,
    return (valor)**(0.5)"""
# el problema de la primera version es que no considera las soluciones generales a raices negativas
# las cuales pueden obtenerse por medio de la descomposicion del numero en una raiz obtenible + j (imaginario)
# para solucionar esto importamos el modulo de matematicas complejas de python cmath
# y redefinimos la funcion ROOTS()
def roots(valor):
    if valor <0:
        return cmath.sqrt(valor) # retorna raices complejas √-n = (x+i)
    return valor**(0.5)
try:
    valor = float(input("√(x):"))
    resultado=roots(valor)
    print(f"√{valor}: {resultado}")
except ValueError as e:
    print(f"Error {e}")
    exit(1)


