#Kelvin to Celsius
def k_to_c (k):
    
    f = k - 273.15
    return f

k = 200
c = k_to_c(k)

print("Kelvin of " + str( k ) + " is " +str( c ) + " in Celsius ")
