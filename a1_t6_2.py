
import statistics
# This code demonstrates that we have a mode value.
values = [8,  11,  9,  14,  9,  15,  18,  6,  9,  10]
mode = statistics.mode(values)
print(mode)
# This code demonstrates that we cannot calculate mode value because there
# are more then one mode.
values = [8, 9, 10, 10, 10, 11, 11, 11, 12, 13]
mode = statistics.mode(values)
print(mode)
