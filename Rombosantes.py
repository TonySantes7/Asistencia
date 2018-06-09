# Santes Mejia Antonio
print "...Tecnicas de programacion.."

a=int(input("Ingrese un numero:"))
   
if a==1:
   
    n=int(input("Ingrese el numero de la columna de enmedio"))
   
    for i in range(n+1):
    for j in range(n-i):
    print(" ",end="")
    for k in range(2*i-1):
    print("#",end="")
    print("")
    for i in range(n-1,0,-1):
    for j in range(n-i):
    print(" ",end="")
    for k in  range(2*i-1):
    print("#",end="")
    print("")
elif a ==2:
    
    print("Introducir un numero y debe ser un numero entero")
    print("entre 1 y 2  y el numero corresponde al segmento de enmedio.")

else:
print("Opcion invalida.Ingrese un numero entero entre 1 y 2 ")
