import math

i = # a positive integer on the Ulam spiral
d = math.ceil(i ** 0.5) // 2  # calculate the numbers's distance 'd' from the origin based on its square root
n = i - (2*d-1)**2  # calculate how many numbers 'n' are in the outer loop of the spiral by subtracting the inner square of numbers 

# calculate which section 's' of the spiral the number is in, and the remaining amount of numbers 'r' in that section
s, r = divmod(n, 2*d) if d else (0, 0)

# calculate the x and y values of the number in the spiral based on s and r
x, y = {
    0: (d, -d + r),
    1: (d - r, d),
    2: (-d, d - r),
    3: (-d + r, -d),
    4: (d, -d)
}.get(s)

print(f'({x}, {y})')
