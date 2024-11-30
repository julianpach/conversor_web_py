
"""Este scrip es para definir una funcion adicionable posteriormente al proyecto principal. El fin de temp...py es 
    crear un conversor de temperaturas a diferentes unidades"""

# definiendo la funcion tmp()
def temp(valor,t_op,t_des):
    if t_op in ['c','celsius']: #inicialmente todo se llevara a la unidad de C
        jmp = valor
    elif t_op in ['fahrenheit','f']:
        jmp = (valor-32)*(5/9) # (T(F) - 32) × 5/9
    elif t_op in ['k','kelvin']:
        jmp = (valor-273.15)
    else:
        raise ValueError('Unidad no reconocida. Digite de nuevo')
    # pasando de C el valor de destino
    if t_des in ['c','celsius']:
        return jmp
    elif t_des in ['fahrenheit','f']:
        return ((9/5)*jmp)-32
    elif t_des in ['k','kelvin']:
        return jmp+273
    else:
        raise ValueError('Unidad no reconocida. Digite de nuevo')

try:
    print('Sistema de entrada')
    print('Fahrenheit, (F)')
    print('Celsius, (C)')
    print('Kelvin, (K)')
    t_op = input('--> ').lower()
    valor = float(input('Temperatura: '))
    t_des = input('sistema de salida: ').lower()
    resultado = temp(valor,t_op,t_des)
    print(f"{valor} {t_op} --> {resultado:2f} {t_des}")
except ValueError as e:
    print(f'Error {e}')
    exit(1)






