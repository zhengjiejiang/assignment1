temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
a = 0
max = temperatures_arr[0]
while a < 8:
   temp = temperatures_arr[a]
   a = a + 1
   if temp > max:
       max = temp

print("The max degree from temperatures_arr is ",max)


temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
a = 0
min = temperatures_arr[0]
while a < 8:
   temp = temperatures_arr[a]
   a = a + 1
   if temp < min:
       min = temp

print("The min degree from temperatures_arr is ",min)
