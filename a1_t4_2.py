pressure_arr = [80, 90, 100, 150, 120, 110, 160, 110, 100]
sum = 0
i = 0
while i < len(pressure_arr):
    sum = pressure_arr[i] + sum
    i = i + 1
mean = sum/len(pressure_arr)
print(mean)
