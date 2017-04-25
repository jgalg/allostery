import numpy as np
import random
from random import random as rr
from threading import Thread
import time
import sys
import os
from multiprocessing import Pool


start_time = time.time()

def quiet():
    sys.stdout = open(os.devnull, "w")

def loud():
    sys.stdout = sys.__stdout__

def distance(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    z = pointA[2] - pointB[2]
    # dist = np.sqrt(x**2 + y**2)
    dist = np.sqrt(x**2 + y**2 + z**2)
    return dist

def gen_points(n):
    # xy = []
    xyz = []
    for i in range(0,n):
    # xy.append((rr(),rr()))
        xyz.append((rr(), rr(), rr()))
    xyz.insert(0, (0.0,0.0,0.0))
    # xy.insert(0,(0.0,0.0))
    xyz.append((1.0,1.0,1.0))
    # xy.append((1.0,1.0))
    points = xyz
    # points = xy
    alldict = {}
    threshold = .22
    for i in range(0,len(points)):
        templist = []
        for j in range(0, len(points)):
            if i == j:
                continue
            if distance(points[i], points[j]) < threshold:
                templist.append(j)
        alldict[i] = templist
    # print(alldict)
    return alldict, points

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
    if current[tiger] == (len(points)-1): # check if it's the end point
        path.append((len(points)-1))
        return print('succeed', path)
    next_current = current[tiger] # new variable name for the best choice
    # current = list(set(alldict[current[tiger]]) - set(path))
    # if current == []:
    #     return 'failed', path
    DFS2(next_current) # recurse to the next step with as a point


# If you want to run it in series, comment out MAIN below and call
# your function in series.

def full_run(stuff):
    global path, alldict, points
    path = []
    alldict, points = gen_points(200)
    print(type(points))
    # DFS2(0)

full_run(3.)

# quiet()
# for i in range(0,10):
#     full_run()
# loud()

# print("--- serial: %s seconds ---" % (time.time() - start_time))

def Main():
    p = Pool()
    p.map(full_run, np.arange(0,100))

# start_time = time.time()

# quiet()
if __name__ == '__main__':
    Main()

# print("--- parallel: %s seconds ---" % (time.time() - start_time))

# quiet()
# loud()


# serial: 63.95 seconds.
# parallel: 81.22 seconds.

# I don't think it's actually running in parallel, but pseudo parallel.
# Once we get everything else running, we'll need to talk to Prof. Thayer
# about how to actually run things in parallel on the cluster.


# bottom
