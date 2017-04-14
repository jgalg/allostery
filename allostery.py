import numpy as np
import matplotlib.pyplot as plt
import random
from random import random as rr


def distance(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    dist = np.sqrt(x**2 + y**2)
    return dist

#test comment here
#another test COMMENT

points = [(0.0,0.0), (0.633203286979593, 0.22112643738670756), (0.5412934629470355, 0.8245739743705389),
(0.8143828383956372, 0.49138563798727863), (0.8266887948696809, 0.5921008945729057), (0.3282184216565035, 0.7273185893319146),
(0.7018341700403963, 0.2303885770008035), (0.919563348912971, 0.7599722500134053), (0.5370488918711036, 0.7692525713077912),
(0.3325542816903544, 0.16905751647044365), (0.8998710338757728, 0.6668577886864834), (0.9272815614950477, 0.07823250986964814),
(0.4889281133052741, 0.49280050393872665),(0.22707445242538993, 0.3970271014005622), (0.8267137143980487, 0.44375549428814354),
(0.15415733070671378, 0.44356049760283334), (0.17683781586555392, 0.44678231177216976), (0.677153525300377, 0.654482998285455),
(0.9260468236100381, 0.6679707089578177), (0.4882155796995482, 0.9149532736767197), (0.5277453428420754, 0.44882933445992323), (1.0, 1.0)]


# points = []
#
# for i in range(20):
#     x = rr.uniform(0,1)
#     y = rr.uniform(0,1)
#     point = (x,y)
#     points.append(point)

n = 20
xy = []
for i in range(0,n):
    xy.append((rr(),rr()))
xy.insert(0,(0.0,0.0))
xy.append((1.0,1.0))
points = xy

alldict = {}
threshold = .35

for i in range(0,len(points)):
    templist = []
    for j in range(0, len(points)):
        if i == j:
            continue
        if distance(points[i], points[j]) < threshold:
            templist.append(j)
    alldict[i] = templist


print(alldict)

path = []

def DFS2(current): # takes a point input
    # print('current node: ', current)
    path.append(current)    # add current point to path
    if alldict[current] == []: # check that it has options
        return print('failed', path)
    current = list(set(alldict[current]) - set(path))  # make current now the options for that point, excluding path
    # print('current branchs: ', current)
    if current == []:
        return print('failed', path)
    puma = 1.5 # set an arbitrarily large initial threshold
    tiger = 0 # initialize the position holder
    for i in range(0,len(current)): # loop through the options
        leopard = distance(points[current[i]], points[-1]) # check distance of option to end point
        if leopard < puma:
            puma = leopard # if it's closer, make it new threshold
            tiger = i # save its position
    if current[tiger] == 21: # check if it's the end point
        path.append(21)
        return print('succeed', path)
    next_current = current[tiger] # new variable name for the best choice
    # current = list(set(alldict[current[tiger]]) - set(path))
    # if current == []:
    #     return 'failed', path
    DFS2(next_current) # recurse to the next step with as a point


DFS2(0)


# for i in range(0,len(points)):
#     print('\n')
#     path = []
#     DFS2(i)





#VISUALIZATION

xs = []
ys = []

for i in range(0,len(points)):
    x = points[i]
    xs.append(x[0])
    ys.append(x[1])

plt.clf()

x_data = [] # create list for line-segment x-data
y_data = [] # create list for line-segment y-data

for point in alldict:   # each point is a list of points to draw line-segments to
    if alldict[point] != []: # if there are no points, loop
        x_data.append(points[point][0]) # store the initial point's x
        y_data.append(points[point][1]) # store the initial point's y
        # print("WE ARE NOW ON POINT", point)
        # print("SEE:", x_data, y_data)
        for i in range(len(alldict[point])): # look at each of its neighbors
            x_data.append(points[alldict[point][i]][0]) # save neighbor's x
            y_data.append(points[alldict[point][i]][1]) # save neighbor's y
            # print("and now drawing a line from", x_data, "to", y_data)
            plt.plot(x_data, y_data, '-', lw = 1) # draw line from point to neighbor
            x_data = x_data[:1] # erase neighbor's x
            y_data = y_data[:1] # erase neighbor's
        x_data = [] # reset for new point
        y_data = [] # reset for new point

plt.plot(xs,ys, '.') # plot all points

if path[-1] == 21:
    for point in path:
        x_data.append(points[point][0]) # store the initial point's x
        y_data.append(points[point][1]) # store the initial point's y
        plt.plot(x_data, y_data, ':r', lw = 3) # draw line from point to neighbor

plt.show()




# TO DO LIST
# get the forward-thinking aspect of DFS working
# fix visualization
# generating random points and fitting them between 0,0 ; 1,1.
# ask Prof Thayer about getting the 100 amino acids / proteins with known paths
# parallelization





# bottom
