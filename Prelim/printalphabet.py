import string

# using ascii values(chr() function)
i = 65
while i <= 90:
    print(chr(i))
    i +=  1
for i in range(97, 123):
    print(chr(i), end=" ")

# using string module
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

