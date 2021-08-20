# Built-in Data Types
'''

Text Type:      str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Types:  dict
Set Types:      set, frozenset
Boolean Types:  bool
Binary Types:   bytes, bytearray, memoryview

'''

# Gettind data type
x = 5
print(type(x))

# Setting the Data Type
'''
Em python o tipo do dado é estabelecido ao se inserir um valor
na variável

x = 'a'                   str
x = 1                     int
x = 1.0                   float
x = 1j                    complex
x = [1, 2, 3]             list
x = (1, 2, 3)             tuple
x = range(6)              range
x = {"Num" : 1}           dict
x = {1, 2, 3}             set
x = frozenset({1, 2, 3})  frozenset
x = True                  bool
x = b"Hello"              bytes
x = bytearray(5)          bytearray
x = memoryview(bytes(5))  memoryview

'''

# Setting the Specific Data Type
x = str("Banana")
x = int(5)