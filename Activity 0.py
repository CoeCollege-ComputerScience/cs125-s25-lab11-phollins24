
A = {'a', 'b', 'c', 'd', 'i', 'j'}
B = {'i', 'j', 'k', 'l'}
C = {'m', 'n', 'o', 'p', 'j', 'i'}

print(A & B & C)
print(A - (B | C))
print((C & (A | B)) - B)
print(A - B - C)
print((B | C) - A)
