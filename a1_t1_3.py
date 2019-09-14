# Fahrenheit to Celsius
def f_to_c (f):

    f = (f - 32) * 5/9
    return f

f = 0
c = f_to_c(f)

print("Fahrenheit of " + str( f ) + " is " +str( c ) + " in Celsius ")
