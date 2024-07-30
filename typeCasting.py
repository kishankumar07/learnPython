print(len(12345))
# the above line => error =>TypeError: object of type 'int' has no len()

# The len() property is only to calculate the length of string only , wrong input gives error

# ----------- imp idea about type conversion of int to str ---------------------------------------

length = len('Jenny Khatri')
print("Your name has " + length + "characters")

# error : TypeError: can only concatenate str (not "int") to str

# To solve this issue, do one thing -> convert that int to str

print("Your name has " + str(length)+ " characters")

# the type of int converted to string 

# -------------------------------------------------------------------------------------------------

# """
# int()
# float()
# str()

# Same as int was converted to string using str() vise versa is also possible using int() , float().
# """
# ----------------------------------------------------------------------------------------------------

# Take 2 inputs from the user and check their types, it is indeed surprising :

val_1 = input("enter value_1")
val_2 = input ('enter value_2')

print(type(val_1))
print(type(val_2))

# output : 
# enter value_1  :  123
# enter value_2  :  hello
# <class 'str'>
# <class 'str'>

# even int is shown as type str
# ----------------------------------------------------------------------------------------------------

val_1 = input ('Enter value 1')
val_2 = input ('Enter value 2')

print(val_1 + val_2)

# the output : is concatenated string not the sum 
# ------------------------------------------------------------------------------------------------------

# So how to convert the string to number :

val_1 = input("enter the val_1")
val_2 = input("enter the val_2")

print(int(val_1) + int(val_2))

# ------------------------------------------------------------------------------------------

# Write a program to add digits of a number :


val = 34
strConv = str(34)
val_1 = strConv[0]
val_2 = strConv[1]
conV1 = int(val_1)
conV2 = int(val_2)
print(conV1 + conV2)


# ----------------------------------------------------------------------------------------------
