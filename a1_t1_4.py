# Fahrenheit to Kelvin
def f_to_k (f):

    f = (f - 32) * 5/9 + 273.15
    return f

f = 0
k = f_to_k(f)

print("Fahrenheit of " + str( f ) + " is " +str( k ) + " in Kelvin ")
