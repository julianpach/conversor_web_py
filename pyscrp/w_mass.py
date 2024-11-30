
"""block of code in charge the conversions of values of mass and weigth"""
# defining inplicit function of rate od convertion for differents units # 

def w_mass(valor,u_origen,u_destino):
    # unidad comodin kg # 
    if u_origen in ['ton','t']:
        valor = valor * 1000 # ton - kg
    elif u_origen in ['kg','kilogramo']:
        valor = valor
    elif u_origen in ['hactogramo','hg']:
        valor = valor / 10
    elif u_origen in ['decagramo','dag']:
        valor = valor / 100
    elif u_origen in ['gramo','g']:
        valor = valor / 1000
    elif u_origen in ['quilate','qlt']:
        valor = valor / 5000
    elif u_origen in ['centigramo','cg']:
        valor = valor / 100000
    elif u_origen in ['miligramo','mg']:
        valor = valor / 1000000
    elif u_origen in ['microgramo','ug']:
        valor = valor / (1*(10**9))
    elif u_origen in ['nanogramo','ng']:
        valor = valor/(1*(10**(12)))
    else:
        raise ValueError ('Unidad de masa invalida. Por favor verifique')
    if u_destino in ['ton','t']:
        return valor / 1000
    elif u_destino in ['kilogramo','kg']:
        return valor
    elif u_destino in ['hectogramo','hg']:
        return valor*10
    elif u_destino in ['decagramo','dag']:
        return valor*100
    elif u_destino in ['gramo','g']:
        return valor*1000
    elif u_destino in ['quilate','qlt']:
        return valor*5000
    elif u_destino in ['centigramo','cg']:
        return valor*100000
    elif u_destino in ['miligramo','mg']:
        return valor*(1*(10**6))
    elif u_destino in ['microgramo','ug']:
        return valor*(1*(10**9))
    elif u_destino in ['nanogramo','ng']:
        return valor*(1*(10**(12)))
    else:
        raise ValueError ('Unidad de masa invalida, por favor verifique')

try:
     print(f'Conversor de unidades de Masa: ')
     valor= float(input("Valor de masa: "))
     u_origen = input("Introduzca la unidad de masa de partida,(T,kg,hg,cg,g,qlt,cg,mg,ug,ng: ").lower().strip()
     u_destino = input("Introduzca la unidad de masa de destino,(T,kg,hg,cg,g,qlt,cg,mg,ug,ng: ").lower().strip()
     resultado = w_mass(valor,u_origen,u_destino)
     print(f"para {valor}{u_origen} se obtienen {format(resultado)}{u_destino}")
except ValueError as e:
    print(f"Error {e}")
    exit(1)
    