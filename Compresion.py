#Compresion de listas
import pdb
import time

pdb.set_trace()
inicio = time.time()
numero_ejercicio = [max([2,8,5,3,9]), max([6,12,8]), max([9,15,195,989,3])]
fin = time.time()
print("Tiempo de ejecución de compresion", (fin-inicio), "segundos")
print("Los números máximos de cada lista son: ", numero_ejercicio)



#Numeros primos de una lista :

my_list = list(range(1,200+1))
a = 0
new_list = []
for num in my_list:
    a_list = list(range(1,num+1))
    for num2 in a_list:
        resto = num % num2
        if resto == 0:
            a += 1

    if a <= 2:
        new_list.append(num)
    a = 0
print (new_list)


# Numeros primos  con la funcion filter
numeros=[1,5,9,8,7,5,6,158]
def es_primo(n):
    primo = True
    for i in range(2,n):
        if(n%i==0):
            primo = False
    return primo

def listar_n_primos(n):
    for i in range(2, n+1):
        if(es_primo(i)):
            print(f"{i}, es primo")

listar_n_primos(20)

primos1 = list(filter(listar_n_primos,numeros))
print(primos1)
