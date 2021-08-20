print("Hello")
print('Hello')

a = "Bye"
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(a)

# Strings are Arrays
a = "Hello"
print(a[2])

# Loop Through a String
for x in "Banana":
    print(x)

# String Length
a = "Cachorro"
print("A palavra " + a + " possui " + str(len(a)) + " letras")

# Check String
txt = "Toda quarta-feira visto rosa"
print("rosa" in txt)
print("azul" in txt)
print("rosa" not in txt)
print("azul" not in txt)

# Slicing
a = "0123456789"
print(a[2:6])
print(a[:7])
print(a[3:])

# Negative Indexing Slicing
print(a[-5:-1])

# Modify Strings
a = "Helo, World!"
print(a.upper())
print(a.lower())

b = " Hello, World! "
print(b.strip()) # tira os espaços no começo e fim

print(a.replace("H", "J"))

print(a.split(", ")) # retorna uma lista

# Concatenação
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

# Format Strings
idade = 18
txt = "Eu tenho {} anos"
print(txt.format(idade))

dia = 3
mes = 9
ano = 2002
txt = "Eu nasci em {} de {} de {}"
print(txt.format(dia, mes, ano))

dia = 21
mes = 3
ano = 2001
txt = "Ela nasceu dia {2} de {0} de {1}"
print(txt.format(mes, ano, dia))

# Methods
a = "aaa"
print(a.capitalize()) # Primeira letra maiúscula

a = "AAA"
print(a.casefold()) # Texto inteiro em lower case

a = "1426742571491"
print(a.count("1")) # Conta o número de vezes que um valor aparece

a = "Banana-maca"
print(a.encode()) # Codifica um valor