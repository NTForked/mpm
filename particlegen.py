from math import sqrt
from numpy import random

template = "x:{},{},{} v:{},{},{} m:{},0,0\n"
text_file = open("./input/input.in", "w")

start = [0.65,0.5,0.5]
h = 0.025
r = 0.25
rho = 400;
# totmass = 3.141592 * (r*r) * (h * 3) * rho
totmass = 3.141592 * 4./3. * (r*r*r) * rho
# totmass = (h * 7) * (h * 7) * (h * 7) * rho 
# totmass = 3.14 * (2.5) * (2.5) * (h * 8) * rho
pos = []
noise = 1.0;
for i in range(-10,11):
    for j in range(-10,11):
        for k in range(-10,11):
            if ( sqrt((h*i)*(h*i) + (h*j)*(h*j) + (h*k)*(h*k)) < r ):
                pos.append([start[0] + h * (i + noise * (random.rand() - 1)), start[1] + h * (j + noise * (random.rand() - 1)), start[2] + h * (k + noise * (random.rand() - 1))])

# for i in range(-3,4):
#     for j in range(-3,4):
#         for k in range(10,13):
#             # if ( sqrt((h*i)*(h*i) + (h*j)*(h*j) + (h*k)*(h*k)) < r ):
#             pos.append([start[0] + h * i, start[1] + h * j, start[2] + h * k])

pmass = totmass / len(pos);

for p in pos:
    # if p[2] > 2.3 :
    #     text_file.write(template.format(p[0],p[1],p[2],
    #                                     0,0,-10.,
    #                                     pmass))
    # else:
    #     text_file.write(template.format(p[0],p[1],p[2],
    #                                     0,0,0.,
    #                                     pmass))
    text_file.write(template.format(p[0],p[1],p[2],
                                    3,0,-1,
                                    pmass))

print("{} particles generated. total mass : {} kg".format(len(pos),totmass))

text_file.close()