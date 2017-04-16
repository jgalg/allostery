import os

res_dict = {}

f = open("/Users/jessegalganov/Documents/allostery/xyz.txt", "r")
for line in f:

    res = line[:4]
    x = line[9:16]
    y = line[18:25]
    z = line[26:32]

    res = int(res)
    x = float(x)
    y = float(y)
    z = float(z)

    # print(res,x,y,z)
    res_dict[res] = (x,y,z)

# print(res_dict)
