
"""x = int(input("what's x?"))
y= int(input("what's y?"))
z= x+y
print(z)"""

#Addition
"""num1=float(input("sumando "))
num2=float(input("sumando "))
sum = num1+num2
print(f"the sum of {num1}+{num2}:{sum}")"""

"""## Division ##
dv1=float(input("dividend: "))
dv2=float(input("divisor: "))

if dv1==0:
    print("Error, division by 0")
else: 
    Rdv=dv1/dv2
    print(f"the result of {dv1}/{dv2}={Rdv}")"""

"""## area of a triangle
bs = float(input("length of the base: "))
hs = float(input("length of height: "))
area = (bs*hs)/2
print(f"the area of the triangle is: {area}")"""

"""#swap values
x = input("insert the value a: ")
y = input("insert the value b: ")
print(f"the initial conditions are: a:{x} & b:{y}")
#hay que poner una variable de paso para que no se pierda el valor inicial 
tm = x
x=y
y= tm
print(f"the swaped variables are: a:{x} & b:{y}")"""

"""# definir funcion max() que devuelva el valor mayor
def maximus():
    if a1 > a2:
        print(f"the highest is {a1}")
    elif a2>a1:
        print(f"the highest value is {a2}")    


a1 = float(input("the 1st value: "))
a2 = float(input("write 2nd value: "))

maximus()"""

"""# definir una funcion maxima que devuelva el mayor de 3 numeros
#max_seg tomara una lista de valores con n elementos y devolvera el mayor 
def max_seg():
    for i in range(len(vc)):
      if i == 0 : 
         temp = vc[i]
         
      elif vc[i] > temp:
         temp = vc[i]
    return temp


# hay varias maneras de hacerlo. primero arreglare el input secuencial de 3 datos al tiempo
ipt= input("digite los valores separados por espacios: ") #input de datos
vc = list(map(float,ipt.split())) # separacion de datos en valores individuales
# print(f"the vector es: {vc}") # este es para verificar si la separacion funciono ##
print("El valor maximo es: ", max_seg())"""


"""#definir una funcion que de la longitud de una lista
#funcion de recorrido
def counter():
  count = 0
  for i in range(len(ls)):
    i == 0
    count  +=1
    if i == ls[-1]:
      return count

vc = input("digite los valores separados por espacios: ")
ls = list(map(
        int,vc.split()))
print("la longitud de la lista es: ", counter(ls))"""

"""desarrollo de conversor completo:"""