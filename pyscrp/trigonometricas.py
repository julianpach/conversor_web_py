"""block of code for trigonometrics functions ops"""

import math

def rad_deg(valor,rd_dg):   ## esta funcion esta creada no para el conversor del primer condicional si no para un conversor 
    match rd_dg:             ## de angulos independiente (una funcion de otro proceso)
        case 1:
            return math.degrees(valor) # angle x from radiams to degree
        case 2:
            return math.radians(valor) # angle x from degree to radiams
        case _: 
            raise ValueError ("Opcion no valida.")




def trig(valor, tri_op):
    match tri_op:
        case 1:
            return (f"El sin({valor}):", math.sin(valor))
        case 2: 
            return (f"El cos({valor}):", math.cos(valor))
        case 3:
            return (f"La tan({valor}):", math.tan(valor))
        case 4:
            return (f"La scs({valor}):", 1/math.cos(valor)) # secante 
        case 5:
            return (f"La csc({valor}):", 1/math.sin(valor)) # cosecante
        case 6:
            return (f"La ctg({valor})", 1/math.tan(valor)) # cotangente
        case _:
            raise ValueError ("Opcion no valida. Elija entre 1 - 6")

try:
    print("las funciones trigonometricas devuelven resultados y reciben (x) en radianes por defecto!")
    print("convertir a radianes?")
    switch = input("(Y) or (N): ").lower()

    if switch == "y":
        deg = float(input("ingrese el valor del angulo (X): ")) # obteniendo el valor en grados 
        valor = math.radians(deg)
        print(f"{deg}° = {valor} Radianes")
    elif switch == "n":
        valor = float(input("ingrese el angulo"))
    
    msn = ['  opciones ',
           '1. Sin',
           '2. Cos',
           '3. Tan',
           '4. Sec',
           '5. Csc',
           '6. Ctg']
    
    print("\n".join(msn))

    """print ("1. Sin")
    print ("2. Cos")
    print ("3. Tan")
    print ("4. Sec")
    print ("5. Csc")
    print ("6. Ctg") """
    tri_op = int(input("Opcion: "))
    resultado = trig(valor,tri_op)
    print(f"{resultado}")

    print(f'Pasar {valor} a Grados?')
    switch_2 = input('(Y) or (N)').lower()

    if switch_2 == 'y': 
        resultado = math.degrees(resultado)
        print(f'{resultado} deg')
    elif switch_2 == 'n':
        print(f'{resultado} rad')

    

except ValueError as e:
    print(f"Error {e}")
    exit(1)