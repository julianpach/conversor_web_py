"""the script define a function that convert between velocity unit's"""

def cv_spd(valor, v_op,v_des): #the initial idea is pass all the units to a ms and then move to the required unit of destiny
    if v_op == "kms":
        valor  = valor * 1000
    elif v_op == 'ms':
        valor = valor
    elif v_op == 'kmh':
        valor = valor / 3.6
    elif v_op == 'mms':
        valor = valor / 1000
    elif v_op == 'ums': ## micrometro (1*10^-6)
        valor = valor /1*10**(-6)
    elif v_op == 'mps':
        valor = valor * 1609
    elif v_op == 'mph':
        valor = valor / 2.237
    elif v_op == 'fts':
        valor = valor / 3.281
    elif v_op == 'nts':
        valor = valor / 1.944
    elif v_op == 'ligth':
        valor = valor * 2.99*(10**(8))
    else : 
        raise ValueError ("Unidad no reconocida. Por favor ingrese nuevamente")
    if v_des == 'kms':
        return valor /1000
    elif v_des ==  'ms':
        return valor
    elif v_des == 'kmh':
        return valor * 3.6
    elif v_des == 'mms':
        return valor * 1000
    elif v_des == 'ums':
        return valor * 1*10**(-6)
    elif v_des == 'mps':
        return valor/1609
    elif v_des == 'mph':
        return valor*2.237
    elif v_des == 'fts':
        return valor * 3.281
    elif v_des == 'nts':
        return valor*1.944
    elif v_des == 'ligth':
        return valor / 2.99*(10**(8))
    else: 
        raise ValueError ('Unidad no reconocida. Por favir ingrese de nuevo')

try: 
    print(f'Conversor de velocidades:')
    print(f"Km/s (kms)          m/s (ms)")
    print(f'Km/h (kmh)          mm/s(mms)')
    print (f'um/s (ums)     millas/s (mps)')
    print(f'Millas/h (mph)       pies/s (fts)')
    print(f'nudo (nts)        luz (ligth)')
    valor = float(input("velocidad: "))
    v_op = input("Unidad: ").lower().strip()
    v_des = input("Unidad destino: ").lower().strip()

    resultado = cv_spd(valor, v_op, v_des)
    print(f'{valor} {v_op} ----> {resultado} {v_des}')
except ValueError as e:
    print(f'Error {e}')
    exit(1)


      
