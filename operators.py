print(4/2)
# will outputs -> 2.0

# ---------------

# if exact 2 is needed in above case :

print(4//2)
# will outputs  -> 2

# ----------------

print(2**3)
# output -> 8

# Exercise :
a,b = 1,2
c = a+b
print(c)
c+=a
print(c)

# ------------------------
c %= b
print(c)
c//=a
print(c)

# -------------------

val_1 = input('enter weight in kg')
val_2 = input ('enter height in m2')

print(float(val_1) // float(val_2)**2)

# ------------------------

# round()
print(round(11.5))
print(round(12.5))

# ---------------------------

# f-strings
name = 'Kishan'
age = 27
print(f"My name is {name} . Iam {age} years old")

# -------------------------