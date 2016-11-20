import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def split_line(text):
    # split the text
    locations = text.split(";")
    fiblocation = []
    # for each word in the line:
    for location in locations:
        fiblocation.append(location)
        # print the word
        # print(fiblocation, file=sys.stderr)

    print(fiblocation[5], file=sys.stderr)
    return fiblocation


def calculate_distance(user_lon, user_lat, fib_lon, fib_lat):
    print(user_lon, file=sys.stderr)
    print(user_lat, file=sys.stderr)
    rad_fib_lon = math.radians(fib_lon)
    rad_fib_lat = math.radians(fib_lat)
    print(rad_fib_lon, file=sys.stderr)
    print(rad_fib_lat, file=sys.stderr)
    x = (rad_fib_lon - user_lon) * math.cos((user_lat + rad_fib_lat) / 2)
    y = rad_fib_lat - user_lat
    print(x, file=sys.stderr)
    print(y, file=sys.stderr)
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) * 6371
    print(distance, file=sys.stderr)
    return distance


lon = input()
fltlon = float(lon.replace(',', '.'))
fltlon = math.radians(fltlon)
print(fltlon, file=sys.stderr)
lat = input()
fltlat = float(lat.replace(',', '.'))
fltlat = math.radians(fltlat)
print(fltlat, file=sys.stderr)
n = int(input())
current_distance = 9999
closest = ""
for i in range(n):
    defib = input()
    fiblocation = split_line(defib)
    print(fiblocation, file=sys.stderr)
    calc_distance = calculate_distance(fltlon, fltlat, float(fiblocation[4].replace(',', '.')),
                                       float(fiblocation[5].replace(',', '.')))
    print(current_distance, file=sys.stderr)
    print(calc_distance, file=sys.stderr)
    if (calc_distance < current_distance):
        current_distance = calc_distance
        closest = fiblocation[1]
    print(closest, file=sys.stderr)

# print(location[0], file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(closest)


