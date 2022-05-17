x = 0

while x <= 10:
    x += 1
    if x == 5:
        continue
    print(x)  # 1,2,3,4,6,7,8,9,10,11
else:
    print("The current value of x is :", x)

print('I am a new line and not part of the loop')