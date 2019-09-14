# Celsius to Kelvin
def c_to_k (c):

    f = c + 273.15
    return f

c = 0
k = c_to_k(c)

print("Celsius of " + str( c ) + " is " +str( k ) + " in Kelvin")
