import string

# Using the string module
word = string.ascii_lowercase
print(word[::-1])

word = string.ascii_uppercase
print(word[::-1])

# Using chr() function
for i in range(122, 96, -1):
    print(chr(i), end="")
print()

j = 90
while j >= 65:
    print(chr(j))
    j -= 1
    