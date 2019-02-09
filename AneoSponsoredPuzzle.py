import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    print("distance %d: %d"% (i, distance), file=sys.stderr)
    print("duration %d: %d"% (i, duration), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(speed, file=sys.stderr)
print(light_count, file=sys.stderr)
print("answer")
