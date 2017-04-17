import numpy as np
import matplotlib.pyplot as plt

# there are 115 residues - the first is 301, the last 415
# each entry in the dict contains a tuple (x,y,z) with coordinates for that residue

res_dict = {301: (59.665, 65.467, 44.936), 302: (55.93, 65.46, 44.229), 303: (56.331, 62.061, 42.559), 304: (56.648, 60.478, 45.98), 305: (53.376, 61.897, 47.293), 306: (50.281, 59.726, 47.039), 307: (47.884, 60.523, 44.205), 308: (44.453, 61.495, 45.625), 309: (42.015, 58.605, 45.252), 310: (38.781, 60.422, 46.12), 311: (36.424, 61.714, 43.38), 312: (37.164, 65.134, 41.906), 313: (35.106, 67.556, 39.831), 314: (36.863, 68.917, 36.75), 315: (35.31, 71.661, 34.656), 316: (36.777, 71.904, 31.194), 317: (35.985, 74.788, 28.874), 318: (36.759, 73.5, 25.382), 319: (34.343, 75.466, 23.251), 320: (34.067, 73.521, 20.007), 321: (37.271, 71.539, 20.183), 322: (38.077, 68.031, 21.349), 323: (38.665, 67.403, 25.048), 324: (42.097, 66.074, 24.204), 325: (42.118, 62.62, 25.768), 326: (41.581, 58.931, 25.006), 327: (39.198, 56.557, 26.771), 328: (39.273, 52.761, 27.077), 329: (36.783, 50.366, 28.669), 330: (33.008, 50.253, 28.503), 331: (32.897, 46.532, 27.828), 332: (30.945, 44.453, 30.318), 333: (30.996, 46.798, 33.307), 334: (34.694, 47.77, 33.473), 335: (34.038, 51.524, 33.501), 336: (35.446, 54.372, 31.379), 337: (39.117, 55.245, 31.915), 338: (41.461, 57.885, 30.544), 339: (44.297, 56.135, 28.727), 340: (46.02, 59.17, 27.275), 341: (46.12, 62.93, 27.712), 342: (47.065, 64.95, 24.641), 343: (49.792, 67.547, 25.118), 344: (48.321, 71.013, 24.702), 345: (44.717, 69.869, 24.729), 346: (41.964, 71.279, 27.015), 347: (42.251, 68.286, 29.368), 348: (46.016, 68.817, 29.667), 349: (45.625, 72.583, 30.232), 350: (43.166, 71.787, 33.038), 351: (45.997, 69.965, 34.795), 352: (43.35, 68.045, 36.734), 353: (43.054, 64.801, 34.76), 354: (45.478, 61.945, 34.183), 355: (45.839, 58.476, 32.712), 356: (44.248, 55.956, 35.077), 357: (41.395, 58.307, 35.979), 358: (37.932, 56.804, 35.639), 359: (35.24, 59.123, 34.296), 360: (32.382, 58.689, 36.753), 361: (30.157, 61.152, 34.922), 362: (29.993, 63.942, 32.365), 363: (27.661, 66.867, 33.045), 364: (25.691, 64.84, 35.583), 365: (25.379, 61.823, 33.293), 366: (26.561, 58.703, 35.128), 367: (29.138, 56.895, 32.996), 368: (30.177, 54.231, 35.509), 369: (28.342, 51.546, 33.558), 370: (28.394, 53.135, 30.113), 371: (29.336, 51.204, 26.977), 372: (32.359, 52.42, 25.025), 373: (30.622, 54.215, 22.159), 374: (27.838, 55.741, 24.278), 375: (30.503, 57.106, 26.674), 376: (32.385, 58.557, 23.71), 377: (29.158, 60.025, 22.344), 378: (28.404, 61.503, 25.769), 379: (31.804, 63.228, 25.952), 380: (31.907, 64.421, 22.343), 381: (28.397, 65.829, 22.627), 382: (28.873, 67.083, 26.176), 383: (28.766, 70.727, 25.121), 384: (31.27, 73.584, 25.403), 385: (31.628, 73.418, 29.181), 386: (32.252, 69.855, 30.316), 387: (31.946, 68.973, 33.99), 388: (33.594, 65.662, 34.701), 389: (33.616, 63.785, 37.996), 390: (36.755, 61.676, 37.842), 391: (38.361, 59.164, 40.178), 392: (41.872, 57.723, 40.049), 393: (41.723, 53.896, 39.75), 394: (45.264, 52.832, 38.686), 395: (44.8, 49.174, 39.578), 396: (41.717, 48.951, 37.425), 397: (43.361, 50.932, 34.651), 398: (46.576, 48.939, 34.679), 399: (44.558, 45.976, 33.373), 400: (44.266, 47.64, 29.947), 401: (47.847, 48.649, 29.176), 402: (50.436, 45.955, 28.589), 403: (53.231, 45.553, 31.156), 404: (51.719, 48.17, 33.461), 405: (51.465, 48.155, 37.249), 406: (51.014, 50.518, 40.183), 407: (53.804, 51.643, 42.503), 408: (53.624, 52.489, 46.219), 409: (52.541, 56.084, 45.545), 410: (49.81, 54.94, 43.176), 411: (51.712, 55.857, 40.022), 412: (51.036, 53.761, 36.933), 413: (54.37, 52.309, 35.812), 414: (54.872, 50.526, 32.52), 415: (57.787, 48.123, 31.992)}
#
#


def distance(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    z = pointA[2] - pointB[2]
    # dist = np.sqrt(x**2 + y**2)
    dist = np.sqrt(x**2 + y**2 + z**2)
    return dist

alldict = {}
threshold = 6

for i in range(301,415):
    templist = []
    for j in range(301, 415):
        if i == j:
            continue
        if distance(res_dict[i], res_dict[j]) < threshold:
            templist.append(j)
    alldict[i] = templist

print(alldict)

xs_1 = []
ys_1 = []
xs_2 = []
ys_2 = []
xs_3 = []
ys_3 = []
xs_4 = []
ys_4 = []
xs_5 = []
ys_5 = []
xs_6 = []
ys_6 = []

for i in range (301,415):
    x = res_dict[i]
    if x[2] <  27:
        xs_1.append(x[0])
        ys_1.append(x[1])
    if (x[2] >=  27 and x[2] < 30):
        xs_2.append(x[0])
        ys_2.append(x[1])
    if (x[2] >=  30 and x[2] < 34):
        xs_3.append(x[0])
        ys_3.append(x[1])
    if (x[2] >=  34 and x[2] < 38):
        xs_4.append(x[0])
        ys_4.append(x[1])
    if (x[2] >=  38 and x[2] < 42):
        xs_5.append(x[0])
        ys_5.append(x[1])
    if (x[2] >  42):
        xs_6.append(x[0])
        ys_6.append(x[1])

print(len(xs_1))
print(len(xs_2))
print(len(xs_3))
print(len(xs_4))
print(len(xs_5))
print(len(xs_6))


color1 = "#0000" + str(25*(int(100/45)))
color2 = "#0000" + str(29*(int(100/45)))
color3 = "#0000" + str(33*(int(100/45)))
color4 = "#0000" + str(37*(int(100/45)))
color5 = "#0000" + str(41*(int(100/45)))
color6 = "#0000" + str(45*(int(100/45)))

print(color1)
print(color2)
print(color3)
print(color4)
print(color5)
print(color6)

plt.plot(xs_1, ys_1, '#000050.') # plot all points
plt.plot(xs_2, ys_2, color2) # plot all points
plt.plot(xs_3, ys_3, color3) # plot all points
plt.plot(xs_4, ys_4, color4) # plot all points
plt.plot(xs_5 ,ys_5, color5) # plot all points
plt.plot(xs_6 ,ys_6, color6) # plot all points

# print(plt.get_plot_commands())


# # Generate data...
# t = np.linspace(0, 2 * np.pi, 20)
# x = np.sin(t)
# y = np.cos(t)
#
# plt.scatter(t,x,c=y)
# plt.show()

# x_data = [] # create list for line-segment x-data
# y_data = [] # create list for line-segment y-data
#
# for point in alldict:   # each point is a list of points to draw line-segments to
#     if alldict[point] != []: # if there are no points, loop
#         x_data.append(points[point][0]) # store the initial point's x
#         y_data.append(points[point][1]) # store the initial point's y
#         # print("WE ARE NOW ON POINT", point)
#         # print("SEE:", x_data, y_data)
#         for i in range(len(alldict[point])): # look at each of its neighbors
#             x_data.append(points[alldict[point][i]][0]) # save neighbor's x
#             y_data.append(points[alldict[point][i]][1]) # save neighbor's y
#             # print("and now drawing a line from", x_data, "to", y_data)
#             plt.plot(x_data, y_data, '-', lw = 1) # draw line from point to neighbor
#             x_data = x_data[:1] # erase neighbor's x
#             y_data = y_data[:1] # erase neighbor's
#         x_data = [] # reset for new point
#         y_data = [] # reset for new point
#
# plt.plot(xs,ys, '.') # plot all points
#
# if path[-1] == 21:
#     for point in path:
#         x_data.append(points[point][0]) # store the initial point's x
#         y_data.append(points[point][1]) # store the initial point's y
#         plt.plot(x_data, y_data, ':r', lw = 3) # draw line from point to neighbor

plt.show()
