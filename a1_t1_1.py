# Celsius to Fahrenheit
def c_to_f (c):

    f = (c * 9/5 ) + 32
    return f

c = 0
f = c_to_f(c)

print("Celsius of " + str( c ) + " is " +str( f ) + " in Fahrenheit")
