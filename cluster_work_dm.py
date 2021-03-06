import numpy as np
import random
import time

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

real_alldict = {301: [302], 302: [303, 305, 301], 303: [304, 305, 411, 302], 304: [305, 303],
 305: [306, 302, 303, 304], 306: [307, 409, 305], 307: [308, 392, 410, 411, 306], 308: [309, 307],
 309: [392, 308], 310: [311], 311: [312, 390, 391, 310], 312: [390, 311], 313: [314], 314: [315, 352, 388, 313],
 315: [316, 317, 386, 387, 314], 316: [317, 386, 315], 317: [385, 315, 316],
 318: [319, 320, 321, 322, 323, 383, 384], 319: [320, 321, 384, 318], 320: [321, 318, 319],
 321: [322, 318, 319, 320], 322: [323, 324, 318, 321], 323: [324, 325, 346, 318, 322],
 324: [325, 342, 345, 346, 347, 322, 323], 325: [326, 338, 323, 324], 326: [327, 339, 340, 325],
 327: [328, 326], 328: [329, 337, 339, 400, 327], 329: [330, 331, 335, 336, 372, 328],
 330: [331, 333, 335, 370, 371, 372, 329], 331: [332, 329, 330], 332: [333, 331], 333: [334, 335, 369, 330, 332],
 334: [335, 333], 335: [336, 337, 329, 330, 333, 334], 336: [337, 358, 359, 329, 335], 337: [338, 356, 358, 397, 328, 335, 336],
 338: [339, 355, 356, 357, 325, 337], 339: [340, 355, 326, 328, 338], 340: [341, 342, 326, 339], 341: [342, 340], 342: [343, 344, 345, 324, 340, 341],
 343: [344, 345, 348, 342], 344: [345, 348, 349, 342, 343], 345: [346, 347, 348, 349, 324, 342, 343, 344],
 346: [347, 349, 323, 324, 345], 347: [348, 349, 350, 353, 324, 345, 346], 348: [349, 350, 343, 344, 345, 347], 349: [350, 344, 345, 346, 347, 348],
 350: [351, 352, 347, 348, 349], 351: [352, 353, 350],
 352: [353, 314, 350, 351], 353: [347, 351, 352], 354: [355, 357], 355: [356, 397, 412, 338, 339, 354],
 356: [357, 392, 394, 397, 337, 338, 355], 357: [358, 390, 392, 338, 354, 356],
 358: [359, 360, 391, 393, 336, 337, 357], 359: [360, 361, 367, 390, 336, 358],
 360: [361, 368, 389, 390, 358, 359], 361: [362, 364, 365, 366, 367, 388, 389, 359, 360],
 362: [363, 364, 365, 388, 361], 363: [364, 365, 382, 386, 387, 362], 364: [365, 361, 362, 363],
 365: [366, 367, 361, 362, 363, 364], 366: [367, 368, 361, 365], 367: [370, 375, 359, 361, 365, 366],
 368: [369, 360, 366], 369: [370, 333, 368], 370: [371, 330, 367, 369], 371: [372, 374, 375, 330, 370],
 372: [373, 375, 329, 330, 371], 373: [374, 376, 377, 372], 374: [375, 377, 371, 373],
 375: [376, 377, 378, 379, 367, 371, 372, 374], 376: [377, 378, 379, 380, 373, 375],
 377: [378, 380, 381, 373, 374, 375, 376], 378: [379, 381, 382, 375, 376, 377], 379: [380, 375, 376, 378],
 380: [381, 376, 377, 379], 381: [382, 377, 378, 380], 382: [383, 386, 363, 378, 381],
 383: [384, 385, 386, 318, 382], 384: [385, 318, 319, 383], 385: [386, 317, 383, 384],
 386: [387, 388, 315, 316, 363, 382, 383, 385], 387: [388, 315, 363, 386], 388: [389, 314, 361, 362, 386, 387],
 389: [390, 360, 361, 388], 390: [391, 311, 312, 357, 359, 360, 389], 391: [393, 311, 358, 390],
 392: [393, 394, 307, 309, 356, 357], 393: [394, 396, 358, 391, 392], 394: [395, 396, 406, 356, 392, 393], 395: [396, 406, 394], 396: [393, 394, 395],
 397: [398, 400, 401, 337, 355, 356], 398: [399, 404, 397], 399: [400, 398], 400: [328, 397, 399], 401: [402, 404, 397], 402: [403, 404, 401],
 403: [404, 414, 415, 402], 404: [405, 414, 398, 401, 402, 403], 405: [406, 413, 404], 406: [407, 410, 412, 394, 395, 405], 407: [408, 409, 410, 411, 406],
 408: [409, 407], 409: [410, 411, 306, 407, 408], 410: [411, 307, 406, 407, 409], 411: [303, 307, 407, 409, 410],
 412: [413, 355, 406], 413: [414, 405, 412], 414: [415, 403, 404, 413], 415: [403, 414]}


def distance(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    z = pointA[2] - pointB[2]
    dist = np.sqrt(x**2 + y**2 + z**2)
    return dist

def real_gathering():
    global res_dict, real_alldict
    threshold = 6
    random.seed()
    real_handful = random.sample(list(res_dict2), 21)
    real_handful.insert(0, 313)
    real_handful.append(376)
    bad_apples = set(range(301,416)) - set(real_handful)
    for res in real_handful:
        real_alldict[res] = list(set(real_alldict[res])- bad_apples)
    return real_handful, real_alldict

# z = 0
def real_DFS3(current): # takes a point input
    global real_alldict, real_handful, res_dict, failure
    # global z
    # print('current node: ', current)
    path.append(current)    # add current point to path
    if real_alldict[current] == []: # check that it has options
        failure += 1
        # z += 1
        # print("FAILED HERE", z)
        return print('failed', path)
    current = list(set(real_alldict[current]) - set(path))  # make current now the options for that point, excluding path
    # print('current branchs: ', current)
    if current == []:
        failure += 1
        return print('failed', path)
    puma = 10000000 # set an arbitrarily large initial threshold
    tiger = 0 # initialize the position holder
    for i in range(0,len(current)): # loop through the options
        leopard = distance(res_dict[current[i]], res_dict[real_handful[-1]]) # check distance of option to end point
        if leopard < puma:
            puma = leopard # if it's closer, make it new threshold
            tiger = i # save its position
    if current[tiger] == (real_handful[-1]): # check if it's the end point
        path.append((real_handful[-1]))
        return print('succeed', path)
    next_current = current[tiger] # new variable name for the best choice
    # current = list(set(alldict[current[tiger]]) - set(path))
    # if current == []:
    #     return 'failed', path
    real_DFS3(next_current) # recurse to the next step with as a point

def real_letsgo():
    global res_dict, real_alldict, real_handful, path, failure
    real_handful, real_alldict = real_gathering()
    path = []
    if real_alldict[real_handful[0]] == []:
        failure += 1
        return print('failed start')
    if real_alldict[real_handful[-1]] == []:
        failure += 1
        return print('failed end')
    real_DFS3(315)

f = open('/home/ajstein/allostery/failure.txt', 'w')
f.close()
f = open('/home/ajstein/allostery/failure.txt', 'a')
n = 100000
for i in range(0,n):
    failure = 0
    real_letsgo()
    f.write(str(failure) + '\n')

f.close()




# bottom
