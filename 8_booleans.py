print(1 == 2)
print(1 == 1)
print(1 > 2)
print(1 < 2)

idade = 18

if idade >= 18:
    print("Vc é maior de idade")
else:
    print("Vc é menor de idade")

print(bool("a"))
print(bool(""))
print(bool(1))
print(bool(0))

# Toda string é verdadeira se tiver conteúdo
# Todo número é verdadeiro se não for 0
# Toda lista, tupla e set é verdadeiro se não estiver vazio

# Valores falsos
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

# Funções que retornam um valor booleano
def funct11():
    return True

if funct11():
    print("Sim!")
else:
    print("Não!")