#===strings===#

a = "guitar"
b = "Hello, World!"
print('t' in a)
print(a[2:5])
print(a[:5])
print(a[2:])
print(b[-5:-2])
print(b[-1])

# looping through strings #
for x in a:
    print(x, end="")
print()
print(len(a))

# string manipulations #

c = " Hello, World! "
print(b.upper())
print(b.lower())
print(b.split(","))
print(c.strip())
print(c.replace("H", "Y"))
print(c.strip().replace("H", "Y"))
print(a+" "+b)

# f-strings and placeholders/modifiers #
age = 30
txt = f"Michael Bag is over {age} years old"
print(txt)
txt = f"the price of rice is {age:.2f} dollars"
print(txt)
txt = f"we are the \"vikings\" from the north"
print(txt)

# string methods #