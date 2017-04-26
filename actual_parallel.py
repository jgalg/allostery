import numpy as np
import random
import time
from multiprocessing import Pool
start_time = time.time()

res_dict = {301: (59.665, 65.467, 44.936), 302: (55.93, 65.46, 44.229), 303: (56.331, 62.061, 42.559),
            304: (56.648, 60.478, 45.98), 305: (53.376, 61.897, 47.293), 306: (50.281, 59.726, 47.039),
            307: (47.884, 60.523, 44.205), 308: (44.453, 61.495, 45.625), 309: (42.015, 58.605, 45.252),
            310: (38.781, 60.422, 46.12), 311: (36.424, 61.714, 43.38), 312: (37.164, 65.134, 41.906),
            313: (35.106, 67.556, 39.831), 314: (36.863, 68.917, 36.75), 315: (35.31, 71.661, 34.656),
            316: (36.777, 71.904, 31.194), 317: (35.985, 74.788, 28.874), 318: (36.759, 73.5, 25.382),
            319: (34.343, 75.466, 23.251), 320: (34.067, 73.521, 20.007), 321: (37.271, 71.539, 20.183),
            322: (38.077, 68.031, 21.349), 323: (38.665, 67.403, 25.048), 324: (42.097, 66.074, 24.204),
            325: (42.118, 62.62, 25.768), 326: (41.581, 58.931, 25.006), 327: (39.198, 56.557, 26.771),
            328: (39.273, 52.761, 27.077), 329: (36.783, 50.366, 28.669), 330: (33.008, 50.253, 28.503),
            331: (32.897, 46.532, 27.828), 332: (30.945, 44.453, 30.318), 333: (30.996, 46.798, 33.307),
            334: (34.694, 47.77, 33.473), 335: (34.038, 51.524, 33.501), 336: (35.446, 54.372, 31.379),
            337: (39.117, 55.245, 31.915), 338: (41.461, 57.885, 30.544), 339: (44.297, 56.135, 28.727),
            340: (46.02, 59.17, 27.275), 341: (46.12, 62.93, 27.712), 342: (47.065, 64.95, 24.641),
            343: (49.792, 67.547, 25.118), 344: (48.321, 71.013, 24.702), 345: (44.717, 69.869, 24.729),
            346: (41.964, 71.279, 27.015), 347: (42.251, 68.286, 29.368), 348: (46.016, 68.817, 29.667),
            349: (45.625, 72.583, 30.232), 350: (43.166, 71.787, 33.038), 351: (45.997, 69.965, 34.795),
            352: (43.35, 68.045, 36.734), 353: (43.054, 64.801, 34.76), 354: (45.478, 61.945, 34.183),
            355: (45.839, 58.476, 32.712), 356: (44.248, 55.956, 35.077), 357: (41.395, 58.307, 35.979),
            358: (37.932, 56.804, 35.639), 359: (35.24, 59.123, 34.296), 360: (32.382, 58.689, 36.753),
            361: (30.157, 61.152, 34.922), 362: (29.993, 63.942, 32.365), 363: (27.661, 66.867, 33.045),
            364: (25.691, 64.84, 35.583), 365: (25.379, 61.823, 33.293), 366: (26.561, 58.703, 35.128),
            367: (29.138, 56.895, 32.996), 368: (30.177, 54.231, 35.509), 369: (28.342, 51.546, 33.558),
            370: (28.394, 53.135, 30.113), 371: (29.336, 51.204, 26.977), 372: (32.359, 52.42, 25.025),
            373: (30.622, 54.215, 22.159), 374: (27.838, 55.741, 24.278), 375: (30.503, 57.106, 26.674),
            376: (32.385, 58.557, 23.71), 377: (29.158, 60.025, 22.344), 378: (28.404, 61.503, 25.769),
            379: (31.804, 63.228, 25.952), 380: (31.907, 64.421, 22.343), 381: (28.397, 65.829, 22.627),
            382: (28.873, 67.083, 26.176), 383: (28.766, 70.727, 25.121), 384: (31.27, 73.584, 25.403),
            385: (31.628, 73.418, 29.181), 386: (32.252, 69.855, 30.316), 387: (31.946, 68.973, 33.99),
            388: (33.594, 65.662, 34.701), 389: (33.616, 63.785, 37.996), 390: (36.755, 61.676, 37.842),
            391: (38.361, 59.164, 40.178), 392: (41.872, 57.723, 40.049), 393: (41.723, 53.896, 39.75),
            394: (45.264, 52.832, 38.686), 395: (44.8, 49.174, 39.578), 396: (41.717, 48.951, 37.425),
            397: (43.361, 50.932, 34.651), 398: (46.576, 48.939, 34.679), 399: (44.558, 45.976, 33.373),
            400: (44.266, 47.64, 29.947), 401: (47.847, 48.649, 29.176), 402: (50.436, 45.955, 28.589),
            403: (53.231, 45.553, 31.156), 404: (51.719, 48.17, 33.461), 405: (51.465, 48.155, 37.249),
            406: (51.014, 50.518, 40.183), 407: (53.804, 51.643, 42.503), 408: (53.624, 52.489, 46.219),
            409: (52.541, 56.084, 45.545), 410: (49.81, 54.94, 43.176), 411: (51.712, 55.857, 40.022),
            412: (51.036, 53.761, 36.933), 413: (54.37, 52.309, 35.812), 414: (54.872, 50.526, 32.52),
            415: (57.787, 48.123, 31.992)}
res_dict2 = {301: (59.665, 65.467, 44.936), 302: (55.93, 65.46, 44.229), 303: (56.331, 62.061, 42.559),
            304: (56.648, 60.478, 45.98), 305: (53.376, 61.897, 47.293), 306: (50.281, 59.726, 47.039),
            307: (47.884, 60.523, 44.205), 308: (44.453, 61.495, 45.625), 309: (42.015, 58.605, 45.252),
            311: (36.424, 61.714, 43.38), 312: (37.164, 65.134, 41.906),
            313: (35.106, 67.556, 39.831), 314: (36.863, 68.917, 36.75), 315: (35.31, 71.661, 34.656),
            316: (36.777, 71.904, 31.194), 317: (35.985, 74.788, 28.874), 318: (36.759, 73.5, 25.382),
            319: (34.343, 75.466, 23.251), 320: (34.067, 73.521, 20.007), 321: (37.271, 71.539, 20.183),
            322: (38.077, 68.031, 21.349), 323: (38.665, 67.403, 25.048), 324: (42.097, 66.074, 24.204),
            325: (42.118, 62.62, 25.768), 326: (41.581, 58.931, 25.006), 327: (39.198, 56.557, 26.771),
            328: (39.273, 52.761, 27.077), 329: (36.783, 50.366, 28.669), 330: (33.008, 50.253, 28.503),
            331: (32.897, 46.532, 27.828), 332: (30.945, 44.453, 30.318), 333: (30.996, 46.798, 33.307),
            334: (34.694, 47.77, 33.473), 335: (34.038, 51.524, 33.501), 336: (35.446, 54.372, 31.379),
            337: (39.117, 55.245, 31.915), 338: (41.461, 57.885, 30.544), 339: (44.297, 56.135, 28.727),
            340: (46.02, 59.17, 27.275), 341: (46.12, 62.93, 27.712), 342: (47.065, 64.95, 24.641),
            343: (49.792, 67.547, 25.118), 344: (48.321, 71.013, 24.702), 345: (44.717, 69.869, 24.729),
            346: (41.964, 71.279, 27.015), 347: (42.251, 68.286, 29.368), 348: (46.016, 68.817, 29.667),
            349: (45.625, 72.583, 30.232), 350: (43.166, 71.787, 33.038), 351: (45.997, 69.965, 34.795),
            352: (43.35, 68.045, 36.734), 353: (43.054, 64.801, 34.76), 354: (45.478, 61.945, 34.183),
            355: (45.839, 58.476, 32.712), 356: (44.248, 55.956, 35.077), 357: (41.395, 58.307, 35.979),
            358: (37.932, 56.804, 35.639), 359: (35.24, 59.123, 34.296), 360: (32.382, 58.689, 36.753),
            361: (30.157, 61.152, 34.922), 362: (29.993, 63.942, 32.365), 363: (27.661, 66.867, 33.045),
            364: (25.691, 64.84, 35.583), 365: (25.379, 61.823, 33.293), 366: (26.561, 58.703, 35.128),
            367: (29.138, 56.895, 32.996), 368: (30.177, 54.231, 35.509), 369: (28.342, 51.546, 33.558),
            370: (28.394, 53.135, 30.113), 371: (29.336, 51.204, 26.977),
            373: (30.622, 54.215, 22.159), 374: (27.838, 55.741, 24.278), 375: (30.503, 57.106, 26.674),
            376: (32.385, 58.557, 23.71), 377: (29.158, 60.025, 22.344), 378: (28.404, 61.503, 25.769),
            379: (31.804, 63.228, 25.952), 380: (31.907, 64.421, 22.343), 381: (28.397, 65.829, 22.627),
            382: (28.873, 67.083, 26.176), 383: (28.766, 70.727, 25.121), 384: (31.27, 73.584, 25.403),
            385: (31.628, 73.418, 29.181), 386: (32.252, 69.855, 30.316), 387: (31.946, 68.973, 33.99),
            388: (33.594, 65.662, 34.701), 389: (33.616, 63.785, 37.996), 390: (36.755, 61.676, 37.842),
            391: (38.361, 59.164, 40.178), 392: (41.872, 57.723, 40.049), 393: (41.723, 53.896, 39.75),
            394: (45.264, 52.832, 38.686), 395: (44.8, 49.174, 39.578), 396: (41.717, 48.951, 37.425),
            397: (43.361, 50.932, 34.651), 398: (46.576, 48.939, 34.679), 399: (44.558, 45.976, 33.373),
            400: (44.266, 47.64, 29.947), 401: (47.847, 48.649, 29.176), 402: (50.436, 45.955, 28.589),
            403: (53.231, 45.553, 31.156), 404: (51.719, 48.17, 33.461), 405: (51.465, 48.155, 37.249),
            406: (51.014, 50.518, 40.183), 407: (53.804, 51.643, 42.503), 408: (53.624, 52.489, 46.219),
            409: (52.541, 56.084, 45.545), 410: (49.81, 54.94, 43.176), 411: (51.712, 55.857, 40.022),
            412: (51.036, 53.761, 36.933), 413: (54.37, 52.309, 35.812), 414: (54.872, 50.526, 32.52),
            415: (57.787, 48.123, 31.992)}


def distance(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    z = pointA[2] - pointB[2]
    dist = np.sqrt(x**2 + y**2 + z**2)
    return dist


def gathering():
    global res_dict
    threshold = 6
    alldict = {}
    random.seed()
    handful = random.sample(list(res_dict2), 21)
    handful.insert(0, 310)
    handful.append(372)
    for i in handful:
        templist = []
        for j in handful:
            if i == j:
                continue
            if distance(res_dict[i], res_dict[j]) < threshold:
                templist.append(j)
        alldict[i] = templist
    return handful, alldict


def DFS3(current): # takes a point input
    global alldict, handful, res_dict, failure
    # print('current node: ', current)
    path.append(current)    # add current point to path
    if alldict[current] == []: # check that it has options
        failure += 1
        return print('failed', path)
    current = list(set(alldict[current]) - set(path))  # make current now the options for that point, excluding path
    # print('current branchs: ', current)
    if current == []:
        failure += 1
        return print('failed', path)
    puma = 10000000 # set an arbitrarily large initial threshold
    tiger = 0 # initialize the position holder
    for i in range(0,len(current)): # loop through the options
        leopard = distance(res_dict[current[i]], res_dict[handful[-1]]) # check distance of option to end point
        if leopard < puma:
            puma = leopard # if it's closer, make it new threshold
            tiger = i # save its position
    if current[tiger] == (handful[-1]): # check if it's the end point
        path.append((handful[-1]))
        return print('succeed', path)
    next_current = current[tiger] # new variable name for the best choice
    # current = list(set(alldict[current[tiger]]) - set(path))
    # if current == []:
        # return 'failed', path
    DFS3(next_current) # recurse to the next step with as a point

def DFS4(current): # takes a point input
    global alldict, handful, res_dict, failure
    # print('current node: ', current)
    path.append(current)    # add current point to path
    if alldict[current] == []: # check that it has options
        failure += 1
        return #failed
    current = list(set(alldict[current]) - set(path))  # make current now the options for that point, excluding path
    # print('current branchs: ', current)
    if current == []:
        failure += 1
        return  # failed
    puma = 10000000 # set an arbitrarily large initial threshold
    tiger = 0 # initialize the position holder
    for i in range(0,len(current)): # loop through the options
        leopard = distance(res_dict[current[i]], res_dict[handful[-1]]) # check distance of option to end point
        if leopard < puma:
            puma = leopard # if it's closer, make it new threshold
            tiger = i # save its position
    if current[tiger] == (handful[-1]): # check if it's the end point
        path.append((handful[-1]))
        return # succeed
    next_current = current[tiger] # new variable name for the best choice
    # current = list(set(alldict[current[tiger]]) - set(path))
    # if current == []:
    #     return 'failed', path
    DFS4(next_current) # recurse to the next step with as a point

def letsgo():
    global res_dict, alldict, handful, path, failure
    handful, alldict = gathering()
    path = []
    if alldict[handful[0]] == []:
        failure += 1
        return print('failed start')
    if alldict[handful[-1]] == []:
        failure += 1
        return print('failed end')
    DFS3(310)

def letsgo2():
    global res_dict, alldict, handful, path, failure
    handful, alldict = gathering()
    path = []
    if alldict[handful[0]] == []:
        failure += 1
        return
    if alldict[handful[-1]] == []:
        failure += 1
        return
    DFS4(310)
    # f.write(str(failure))

# f = open('/Users/ajstein/Documents/allostery/failure.txt', 'w')
# f.close()
# f = open('/Users/ajstein/Documents/allostery/failure.txt', 'a')
n = 100
for i in range(0,n):
    failure = 0
    letsgo()
    # f.write(str(failure) + '\n')
    # print(failure)
# print('success: ', (n - failure))
# print('success rate: ', (n - failure)*100/n,'%')
f.close()



# READING THE FILES RETURNED FROM THE CLUSTER #
# n = 1000000
# num_lines = sum(int(line) for line in open('/Users/ajstein/Documents/allostery/failure.txt'))
# print('\n')
# print('Total Failures: ', num_lines)
# print('Success Ratio: ', (n - num_lines)*100./n, '%')







print("--- %s seconds ---" % (time.time() - start_time))
# bottom
