"""Script  that define a function vol_cvrs() which translate or convert between measurement volumen systems """

def vol_cvrs(valor, op_in, op_ds):
    if op_in == 'km3':
        valor = valor * (1*(10**(9)))
    elif op_in == 'm3':
        valor = valor
    elif op_in == 'hl':
        valor = valor / 10
    elif op_in in ['l','dm3']:
        valor = valor / 1000
    elif op_in == 'dl':
        valor = valor / 10000
    elif op_in == 'cl':
        valor  = valor / 100000
    elif op_in == 'cm3':
        valor = valor / 1e+6
    elif op_in == 'ml':
        valor = valor / 1e+6
    elif op_in == 'mm3':
        valor = valor / 1e+9
    elif op_in == 'ul':
        valor = valor / 1e+18
    elif op_in == 'glen':
        valor = valor / 220
    elif op_in == 'glee':
        valor = valor / 264.2
    elif op_in == 'ft3':
        valor = valor / 35315
    elif op_in == 'in3':
        valor = valor / 61020
    else:
        raise ValueError('Unidad errada. Digite nuevamente')
    if op_ds == 'km3':
        return valor/1e+9
    elif op_ds == 'm3':
        return valor 
    elif op_ds == 'hl':
        return valor * 10
    elif op_ds in ['l','dm3']:
        return valor * 1000
    elif op_ds == 'dl':
        return valor*10000
    elif op_ds == 'cl':
        return valor * 100000
    elif op_ds == 'cm3':
        return valor / 1e+6
    elif op_ds == 'ml':
        return valor * 1e+6
    elif op_ds == 'mm3':
        return  valor *1e+9
    elif op_ds == 'ul':
        return valor * 1e+18
    elif op_ds == 'glen':
        return valor *220
    elif op_ds == 'glee':
        return valor * 264.2
    elif op_ds == 'ft3':
        return valor*35315
    elif op_ds == 'in3':
        return valor* 61020
    else: 
        raise ValueError('Unidad no reconocida. Intente de nuevo')
    
try: 
    wng = ["                     conversor                       ", 
           "Kilometro Cubico_______km3    metro cubico_________m3",
           "Hectolitro______________hl   Litro/decimetro3__[l,dm3]",
           "Decilitro_______________dl    Centilitro___________cl",
           "centimetro cubico______cm3    mililitro____________ml",
           "Milimetro Cubico_______mm3    Microlitro___________ul",
           "Galon Imperial________glen    Galon EEUU_________Glee",
           "Pie cubico_____________ft3    Pulgada cubica______in3"]
    #print(wng) ___ para mejorar la legibilidad de la tabla :print("\n".join(wng))
    print("\n".join(wng))
    valor = float(input('valor: '))
    op_in = input('Unidad de partida: ').lower().strip()
    op_ds = input('Unidad de destino: ').lower().strip()
    resultado = vol_cvrs(valor,op_in,op_ds)
    print(f'{valor} {op_in} ----> {resultado} {op_ds} ')

except ValueError as e:
    print(f"Error {e}")
    exit(1)