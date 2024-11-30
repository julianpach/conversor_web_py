"""This script is in charge of the function to convert values given by the user onto differents numerics 
    systems, for this inital stage it will be: Hex, Dec, Oct, Bin"""

def nsys_conversor(valor,nb_op,nb_des):
    if nb_op =='HEX':
        valor_d = int(valor,16)
    elif nb_op == 'DEC':
        valor_d = int(valor) # no se agrega nada xq ya es decimal
    elif nb_op == 'OCT': 
        valor_d = int(valor,8)
    elif nb_op == 'BIN':
        valor_d = int(valor, 2)
    else:
        raise ValueError ("Sistema numerico no valido. Ingrese de nuevo")
    
    if nb_des == 'HEX':
        return hex(valor_d)[2:] #[2:] es usado para eliminar la parte string de la salida (0x, 0o, 0b...)
    elif nb_des == 'DEC':
        return valor_d
    elif nb_des == 'OCT':
        return oct(valor_d)[2:]
    elif nb_des == 'BIN':
        return bin(valor_d)[2:]
    else:
        raise ValueError('Sistema numerico no valido. Seleccione nuevamente')

try: 
    valor = input('Ingrese el valor: ').strip().upper()# strip y upper eliminan los posibles espacios en la respuesta y las pone en mayusculas
    print('sistemas de entrada: HEX / DEC / OCT / BIN')
    nb_op = input(f'{valor}: ').strip().upper()
    nb_des = input('Sistema destino: ').strip().upper()
    resultado = nsys_conversor(valor,nb_op,nb_des)
    print(f'{valor}{nb_op} --> {nb_des} : {resultado} {nb_des}')
except ValueError as e:
    print(f'Error {e}')
    exit (1)