import math
import numpy as np

duration = 10
time = 4
if (time//duration) % 2 == 0:
    print("Green Light")
else:
    print("Red Light")

for i in range(100):
    print(round(1/(1+(1/math.exp((i//duration) % 2)))))

distance0 = 10
duration0 = 4
distance1 = 30
duration1 = 6
distance4 = 50
duration4 = 10
distance5 = 100
duration5 = 25
possible_time = list(range(0, distance5))
possible_time_array = np.arange(0, distance5)
print(possible_time_array)

# distance0_array = possible_time_array // duration0 % 2 == 0


distance0_filter = np.extract(possible_time_array // duration0 % 2 == 0, possible_time_array)
distance1_filter = np.extract(possible_time_array // duration1 % 2 == 0, possible_time_array)
distance4_filter = np.extract(possible_time_array // duration4 % 2 == 0, possible_time_array)
distance5_filter = np.extract(possible_time_array // duration5 % 2 == 0, possible_time_array)

# distance0_list = list(filter(lambda x: (x//duration0) % 2 == 0, possible_time))
# distance1_list = list(filter(lambda x: (x//duration1) % 2 == 0, possible_time))
# distance4_list = list(filter(lambda x: (x//duration4) % 2 == 0, possible_time))
# distance5_list = list(filter(lambda x: (x//duration5) % 2 == 0, possible_time))
# print(distance0_array)

print(distance0_filter)
print(distance1_filter)
print(distance4_filter)
print(distance5_filter)

# print(possible_time_array // duration0 % 2 == 0)
