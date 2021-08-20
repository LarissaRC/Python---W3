x = 1    # int
y = 1.0  # Float
z = 1j   # Complex

print(type(x))
print(type(y))
print(type(z))

# Integer
x = 1
y = 123344566678
z = -53315

print(type(x))
print(type(y))
print(type(z))

# Float
x = 1.111
y = 3728163.9
z = -0.12

print(type(x))
print(type(y))
print(type(z))

# Float também pode conter números científicos (notação)
x = 1e8  # "e" indica potência de 10
print(x)
print(type(x))

# Complex - o "j" representa a parte imaginária
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Convertion
x = 1
a = float(x)

print(a)
print(type(a), type(x))

# Random Number
import random # É preciso importar
print(random.randrange(1, 9))

# Casting

x = int(1)   # = 1
y = int(2.8) # = 2
z = "3"      # = 3

x = float(1)   # = 1.0
y = float(2.8) # = 2.8
z = float("3") # = 3.0

x = str(1)   # = "1"
y = str(2.8) # = "2.8"
z = str(3.0) # = "3.0"