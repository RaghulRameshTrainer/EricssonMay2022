from math import pi

def circle_area(r):

    if type(r) not in [int, float]:
        raise TypeError('Radius should be a int or float')
    if r < 0:
        raise ValueError("radius cannot be in negative")
    # if r == 0:
    #     raise ValueError("Radius cannot be 0 for a circle")
    return pi*r*r

# radius=[2,0,-3,2+3j,True,"chennai"]
#
# for r in radius:
#     print("for radius r:",circle_area(r))