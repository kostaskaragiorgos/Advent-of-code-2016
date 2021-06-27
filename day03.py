tricounter = 0
with open("day3.txt") as f:
    lines = f.read().strip().split("\n")
    for i in lines:
        x,y,z =  i.split()
        x,y,z = sorted([int(x),int(y),int(z)])
        if x + y > z:
            tricounter += 1
print(tricounter)