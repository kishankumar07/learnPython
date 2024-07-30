height = int(input('Enter height in feet'))

if height > 3 :
    print('Height is greater than 3')
else :
    print('Height is less than 3')    

# ----------------------------------------
# nested if
a = 52
if a > 2 :
    print('even number ')
    if a > 10 :
        print('Number is both even and greater than 10')

# -----------------------------------------
# else and if

height = int(input('Enter your height in feet'))        
if height > 3 :
    print('You can go for rollercoaster')
    age = int(input('enter your age'))
    if age <=18 :
        print('Please pay Rs.250')
    else :
        print('Please pay Rs. 500')    
else :
    print('Sorry you cant ride')        
print('bye')

# -------------------------------------------

mark = float(input('Enter your mark'))
if mark > 90 :
    print('Your outstanding')
elif (mark >5 and mark < 90) :
    print('Average')    
else :
    print('failed')

# -------------------------------------------    