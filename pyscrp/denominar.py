""" the idea is put the imput x down bellow the 1 in a form 1/(x), and also give the value """
def denominador(valor):
    if valor == 0:
        raise ValueError ("No se puede dividir entre cero")
    return 1/(valor)

try:
    valor = float(input("valor X^-1: "))
    resultado= denominador(valor)
    print(f"para 1/({valor}): {resultado}")
except ValueError as e: #con esta excepsion limpiamos para cualquier error diferente del raise inicial del la funcion denominador()
    print(f"Error {e}") 
    exit(1) # se usa para terminar el proceso de forma sencilla son el traceback. Puede usarse opcionalmente exit(0)

