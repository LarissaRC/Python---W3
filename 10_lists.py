# Criando uma lista
lista = [1, 2, 3]
print(lista)

'''
Listas são:
* Ordenadas
    Os itens estão sempre ordenados.
    Se outro item for adicionado, será no fim da lista
* Alteráveis
    Adicionar, alterar e excluir itens
* Permitem duplicidade
    O que realmente importa é a indexação, por isso há duplicidades
* Indexadas
'''

lista = [1, 2, 3, 2, 1]
print(lista)

# Length
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(lista))

# Data Types - Podem conter qualquer tipo de dado
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = [True, False, True]
lista4 = [1, 2.0, "o", True]

# Type
print(type(lista))

# list() Constructor
lista = list((1, 2, 3, 4))
print(lista)

# Access Itens
lista = [1, 2, 3]
print(lista[0])
print(lista[-1])
print(lista[0:2])
print(lista[:2])
print(lista[1:])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[-4:-1])

# Check itens in a list
lista = ["banana", "maça", "pera", "morango"]
print("morango" in lista)

# Change Item
lista = [1, 2, 3]
lista[2] = 4
print(lista)

lista = [1, 2, 3, 4, 5, 6]
lista[1:4] = [7, 8, 9]
print(lista)

lista = [1, 2]
lista[1:2] = [3, 4] # Mais itens do que o limite especificado
print(lista)

lista = [1, 2, 3, 4, 5, 6, 7]
lista[1:6] = [8, 9] # Menos itens do que o limite especificado
print(lista)

# Insert itens
lista = [1, 2, 3]
lista.insert(1, 4) # index + valor
print(lista)

# Add itens
lista = [1, 2]
lista.append(3)
print(lista)

# Extend - Inserir elementos de uma lista a outra
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)

# Remove - Remove um item especificado por seu valor
lista = ["um", "dois", "tres"]
lista.remove("dois")
print(lista)

# pop - Remove um item por seu index
lista = [1, 2, 3]
lista.pop(1)
print(lista)

lista = [1, 2, 3]
lista.pop() # Remove o último item
print(lista)

# del - tbm deleta um index especificado
lista = [1, 2, 3]
del lista[0]
print(lista)

# del também serve para deletar uma lista por completa
del lista # Não limpa a lista, e sim deleta toda a variável

# Clear - Agora sim limpa a lista
lista = [1, 2, 3]
lista.clear()
print(lista)

# Loop for - por itens
lista = [1, 2, 3, 4]
for x in lista:
    print(x)

# Loop for - por index
for i in range(len(lista)):
    print(lista[i])

# While loop
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

# List Comprehension
lista = ["banana", "morango", "uva", "tomate"]
[print(x) for x in lista]