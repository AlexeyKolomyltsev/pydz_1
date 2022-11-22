def f(x,y,z):
    return not(x or y or z) == (not(x) or not(y) or not(z))

values = [0, 1]

print("X Y Z F")
for x in values:
    for y in values:
        for z in values:
            print(f"{x} {y} {z} {f(x,y,z)}")