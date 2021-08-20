# Não há comando para criar uma variável

x = 5
y = 'Jay'
print(x, y)

# Não é preciso definir o tipo de uma variável

print(type(x))
print(type(y))

# Casting - Especificando qual o tipo da variável que vai ser recebida
x = str(3)
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

# Aspas simples e duplas são válidas para strings
x = 'Jay'
y = "Jack"

# Case-sensitive
a = 1
A = 1
# a & A não são a mesma variável

# Nomes válidos
'''
- Deve começar com uma letra ou _
- Não pode começar com um número
- Deve conter apenas caracteres alfanuméricos e _
- Variáveis são case-sensitive
'''
jay = 1
JAY = 1
_jay = 1
ja_y = 1
jay1 = 1
minhaVariavel = 1
MinhaVariavel = 1
minha_variavel = 1

# Múltiplos valores - Múltiplas variáveis
x, y, z = 1, 2, 3
print(x, y, z)

# Um valor - Múltiplas variáveis
x = y = z = 3
print(x, y, z)

# Unpack a Collection
nomes = ["Mateus", "Felipe", "Carlos"]
x, y, z = nomes
print(x, y, z)

# Output variables
x = str(18)
print("Eu tenho " + x + " anos")

nome1 = 'Larissa '
nome2 = "Carvalho"
nome = nome1 + nome2
print(nome)

x = 1
y = 2
print(x + y)

# Valor numérico + string = erro

# Global variables
x = "legal"
def funct():
    print("Que " + x)

funct()

def funct2():
    x = "bacana"
    print("Que " + x)

funct2()

# Global keyword

# Criar uma variável global dentro de uma função
def funct3():
    global b
    b = "dia"
    print("Bom " + b)
funct3()
print(b)

# Alterar uma variável global numa função
num = 3

def funct4():
    global num
    num = 4
funct4()
print(num)