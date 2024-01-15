tupla = (1,2,3)

tupla1 = (4,5)

tuplas = tupla + tupla1

print("Tupla number 1 = " + str(tupla))
print("Tupla number 2 = " + str(tupla1))
print("Tupla concat = " + str(tuplas))

#Otra forma es

t= (1,2,3)
lista = list(t)
lista.append(4)
t2=tuple(lista)

print(t2)