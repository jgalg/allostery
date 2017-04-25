import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr


res_dict = {301: (59.665, 65.467, 44.936), 302: (55.93, 65.46, 44.229), 303: (56.331, 62.061, 42.559), 304: (56.648, 60.478, 45.98), 305: (53.376, 61.897, 47.293), 306: (50.281, 59.726, 47.039), 307: (47.884, 60.523, 44.205), 308: (44.453, 61.495, 45.625), 309: (42.015, 58.605, 45.252), 310: (38.781, 60.422, 46.12), 311: (36.424, 61.714, 43.38), 312: (37.164, 65.134, 41.906), 313: (35.106, 67.556, 39.831), 314: (36.863, 68.917, 36.75), 315: (35.31, 71.661, 34.656), 316: (36.777, 71.904, 31.194), 317: (35.985, 74.788, 28.874), 318: (36.759, 73.5, 25.382), 319: (34.343, 75.466, 23.251), 320: (34.067, 73.521, 20.007), 321: (37.271, 71.539, 20.183), 322: (38.077, 68.031, 21.349), 323: (38.665, 67.403, 25.048), 324: (42.097, 66.074, 24.204), 325: (42.118, 62.62, 25.768), 326: (41.581, 58.931, 25.006), 327: (39.198, 56.557, 26.771), 328: (39.273, 52.761, 27.077), 329: (36.783, 50.366, 28.669), 330: (33.008, 50.253, 28.503), 331: (32.897, 46.532, 27.828), 332: (30.945, 44.453, 30.318), 333: (30.996, 46.798, 33.307), 334: (34.694, 47.77, 33.473), 335: (34.038, 51.524, 33.501), 336: (35.446, 54.372, 31.379), 337: (39.117, 55.245, 31.915), 338: (41.461, 57.885, 30.544), 339: (44.297, 56.135, 28.727), 340: (46.02, 59.17, 27.275), 341: (46.12, 62.93, 27.712), 342: (47.065, 64.95, 24.641), 343: (49.792, 67.547, 25.118), 344: (48.321, 71.013, 24.702), 345: (44.717, 69.869, 24.729), 346: (41.964, 71.279, 27.015), 347: (42.251, 68.286, 29.368), 348: (46.016, 68.817, 29.667), 349: (45.625, 72.583, 30.232), 350: (43.166, 71.787, 33.038), 351: (45.997, 69.965, 34.795), 352: (43.35, 68.045, 36.734), 353: (43.054, 64.801, 34.76), 354: (45.478, 61.945, 34.183), 355: (45.839, 58.476, 32.712), 356: (44.248, 55.956, 35.077), 357: (41.395, 58.307, 35.979), 358: (37.932, 56.804, 35.639), 359: (35.24, 59.123, 34.296), 360: (32.382, 58.689, 36.753), 361: (30.157, 61.152, 34.922), 362: (29.993, 63.942, 32.365), 363: (27.661, 66.867, 33.045), 364: (25.691, 64.84, 35.583), 365: (25.379, 61.823, 33.293), 366: (26.561, 58.703, 35.128), 367: (29.138, 56.895, 32.996), 368: (30.177, 54.231, 35.509), 369: (28.342, 51.546, 33.558), 370: (28.394, 53.135, 30.113), 371: (29.336, 51.204, 26.977), 372: (32.359, 52.42, 25.025), 373: (30.622, 54.215, 22.159), 374: (27.838, 55.741, 24.278), 375: (30.503, 57.106, 26.674), 376: (32.385, 58.557, 23.71), 377: (29.158, 60.025, 22.344), 378: (28.404, 61.503, 25.769), 379: (31.804, 63.228, 25.952), 380: (31.907, 64.421, 22.343), 381: (28.397, 65.829, 22.627), 382: (28.873, 67.083, 26.176), 383: (28.766, 70.727, 25.121), 384: (31.27, 73.584, 25.403), 385: (31.628, 73.418, 29.181), 386: (32.252, 69.855, 30.316), 387: (31.946, 68.973, 33.99), 388: (33.594, 65.662, 34.701), 389: (33.616, 63.785, 37.996), 390: (36.755, 61.676, 37.842), 391: (38.361, 59.164, 40.178), 392: (41.872, 57.723, 40.049), 393: (41.723, 53.896, 39.75), 394: (45.264, 52.832, 38.686), 395: (44.8, 49.174, 39.578), 396: (41.717, 48.951, 37.425), 397: (43.361, 50.932, 34.651), 398: (46.576, 48.939, 34.679), 399: (44.558, 45.976, 33.373), 400: (44.266, 47.64, 29.947), 401: (47.847, 48.649, 29.176), 402: (50.436, 45.955, 28.589), 403: (53.231, 45.553, 31.156), 404: (51.719, 48.17, 33.461), 405: (51.465, 48.155, 37.249), 406: (51.014, 50.518, 40.183), 407: (53.804, 51.643, 42.503), 408: (53.624, 52.489, 46.219), 409: (52.541, 56.084, 45.545), 410: (49.81, 54.94, 43.176), 411: (51.712, 55.857, 40.022), 412: (51.036, 53.761, 36.933), 413: (54.37, 52.309, 35.812), 414: (54.872, 50.526, 32.52), 415: (57.787, 48.123, 31.992)}


alldict = {301: [302, 303, 304], 302: [301, 303, 304, 305], 303: [301, 302, 304, 305], 304: [301, 302, 303, 305], 305: [302, 303, 304, 306], 306: [305, 307, 409], 307: [306, 308, 410], 308: [307, 309, 310], 309: [308, 310, 392], 310: [308, 309, 311], 311: [310, 312, 390, 391], 312: [311, 313, 389, 390], 313: [312, 314, 388, 389], 314: [313, 315, 387, 388], 315: [314, 316, 386, 387], 316: [315, 317, 385, 386], 317: [316, 318, 319, 384, 385], 318: [317, 319, 321, 346, 384], 319: [317, 318, 320, 321, 384], 320: [319, 321], 321: [318, 319, 320, 322], 322: [321, 323, 324], 323: [322, 324, 325, 346, 347], 324: [322, 323, 325, 342, 345, 346, 347], 325: [323, 324, 326, 340, 341, 342], 326: [325, 327, 338, 339, 340], 327: [326, 328, 337, 338, 339], 328: [327, 329, 336, 337], 329: [328, 330, 331, 334, 335, 336], 330: [329, 331, 334, 335, 336, 370, 371, 372], 331: [329, 330, 332, 333, 371], 332: [331, 333, 334], 333: [331, 332, 334, 335, 369], 334: [329, 330, 332, 333, 335], 335: [329, 330, 333, 334, 336, 368, 369], 336: [328, 329, 330, 335, 337, 358, 359], 337: [327, 328, 336, 338, 357, 358, 359], 338: [326, 327, 337, 339, 340, 355, 356, 357], 339: [326, 327, 338, 340, 355], 340: [325, 326, 338, 339, 341, 355], 341: [325, 340, 342], 342: [324, 325, 341, 343, 345], 343: [342, 344, 345], 344: [343, 345, 348], 345: [324, 342, 343, 344, 346, 347, 348], 346: [318, 323, 324, 345, 347, 348, 349], 347: [323, 324, 345, 346, 348, 349, 350], 348: [344, 345, 346, 347, 349, 350, 351], 349: [346, 347, 348, 350, 351], 350: [347, 348, 349, 351, 352], 351: [348, 349, 350, 352, 353], 352: [350, 351, 353], 353: [351, 352, 354], 354: [353, 355, 357], 355: [338, 339, 340, 354, 356, 357], 356: [338, 355, 357, 392, 393, 394, 397], 357: [337, 338, 354, 355, 356, 358, 391, 392, 393], 358: [336, 337, 357, 359, 360, 390, 391, 392], 359: [336, 337, 358, 360, 361, 390], 360: [358, 359, 361, 367, 368, 389, 390], 361: [359, 360, 362, 364, 365, 366, 367, 388, 389], 362: [361, 363, 364, 365, 387, 388], 363: [362, 364, 365, 387], 364: [361, 362, 363, 365], 365: [361, 362, 363, 364, 366], 366: [361, 365, 367, 368], 367: [360, 361, 366, 368, 369, 370], 368: [335, 360, 366, 367, 369, 370], 369: [333, 335, 367, 368, 370], 370: [330, 367, 368, 369, 371, 375], 371: [330, 331, 370, 372, 373, 374], 372: [330, 371, 373, 374, 375], 373: [371, 372, 374, 375, 376, 377], 374: [371, 372, 373, 375, 376, 377, 378], 375: [370, 372, 373, 374, 376, 377, 378], 376: [373, 374, 375, 377, 378, 379], 377: [373, 374, 375, 376, 378, 379, 380, 381], 378: [374, 375, 376, 377, 379, 380, 381, 382], 379: [376, 377, 378, 380, 381, 382], 380: [377, 378, 379, 381, 382], 381: [377, 378, 379, 380, 382, 383], 382: [378, 379, 380, 381, 383], 383: [381, 382, 384, 385], 384: [317, 318, 319, 383, 385], 385: [316, 317, 383, 384, 386], 386: [315, 316, 385, 387], 387: [314, 315, 362, 363, 386, 388], 388: [313, 314, 361, 362, 387, 389, 390], 389: [312, 313, 360, 361, 388, 390], 390: [311, 312, 358, 359, 360, 388, 389, 391], 391: [311, 357, 358, 390, 392], 392: [309, 356, 357, 358, 391, 393], 393: [356, 357, 392, 394, 395, 396], 394: [356, 393, 395, 396, 397, 398], 395: [393, 394, 396, 397, 398], 396: [393, 394, 395, 397, 398, 399], 397: [356, 394, 395, 396, 398, 399, 400], 398: [394, 395, 396, 397, 399, 400, 401, 404, 405], 399: [396, 397, 398, 400, 401], 400: [397, 398, 399, 401], 401: [398, 399, 400, 402, 404], 402: [401, 403, 404], 403: [402, 404, 414], 404: [398, 401, 402, 403, 405, 413, 414], 405: [398, 404, 406, 412, 413], 406: [405, 407, 410, 411, 412, 413], 407: [406, 408, 409, 410, 411], 408: [407, 409, 410], 409: [306, 407, 408, 410, 411], 410: [307, 406, 407, 408, 409, 411], 411: [406, 407, 409, 410, 412], 412: [405, 406, 411, 413], 413: [404, 405, 406, 412, 414], 414: [403, 404, 413]}


xs_1 = []
ys_1 = []
zs_1 = []
xs_2 = []
ys_2 = []
zs_2 = []
xs_3 = []
ys_3 = []
zs_3 = []
xs_4 = []
ys_4 = []
zs_4 = []
xs_5 = []
ys_5 = []
zs_5 = []
xs_6 = []
ys_6 = []
zs_6 = []

for i in range (301,415):
    x = res_dict[i]
    if x[2] <  27:
        xs_1.append(x[0])
        ys_1.append(x[1])
        zs_1.append(x[2])
    if (x[2] >=  27 and x[2] < 30):
        xs_2.append(x[0])
        ys_2.append(x[1])
        zs_2.append(x[2])
    if (x[2] >=  30 and x[2] < 34):
        xs_3.append(x[0])
        ys_3.append(x[1])
        zs_3.append(x[2])
    if (x[2] >=  34 and x[2] < 38):
        xs_4.append(x[0])
        ys_4.append(x[1])
        zs_4.append(x[2])
    if (x[2] >=  38 and x[2] < 42):
        xs_5.append(x[0])
        ys_5.append(x[1])
        zs_5.append(x[2])
    if (x[2] >  42):
        xs_6.append(x[0])
        ys_6.append(x[1])
        zs_6.append(x[2])

# VERSION 1

# print(len(xs_1))
# print(len(xs_2))
# print(len(xs_3))
# print(len(xs_4))
# print(len(xs_5))
# print(len(xs_6))


color1 = "#0000" + str(25*(int(100/45)))
color2 = "#0000" + str(29*(int(100/45)))
color3 = "#0000" + str(33*(int(100/45)))
color4 = "#0000" + str(37*(int(100/45)))
color5 = "#0000" + str(41*(int(100/45)))
color6 = "#0000" + str(45*(int(100/45)))

# # print(color1)
# # print(color2)
# # print(color3)
# # print(color4)
# # print(color5)
# # print(color6)

first, = plt.plot(xs_1, ys_1,) # plot all points
plt.setp(first, linestyle = '', marker = '.', color=color1)

second, = plt.plot(xs_2, ys_2) # plot all points
plt.setp(second, linestyle = '', marker = '.', color=color2)

third, = plt.plot(xs_2, ys_2) # plot all points
plt.setp(third, linestyle = '', marker = '.', color=color3)

fourth, = plt.plot(xs_2, ys_2) # plot all points
plt.setp(fourth, linestyle = '', marker = '.', color=color4)

fifth, = plt.plot(xs_2, ys_2) # plot all points
plt.setp(fifth, linestyle = '', marker = '.', color=color5)

sixth, = plt.plot(xs_2, ys_2) # plot all points
plt.setp(sixth, linestyle = '', marker = '.', color=color6)



# VERSION 2





fig, ax = plt.subplots(figsize=(5,5))

colors = ['red', 'blue']
levels = [0, 1]

nearness1 = np.where(np.array(zs_1) < 26, 0, 1)
cmap, norm = clr.from_levels_and_colors(levels = [0,1], colors = ['#ccccff', '#e5e5ff'], extend='max')
ax.scatter(xs_1, ys_1 ,c = nearness1, s=150, marker='.', edgecolor='none', cmap=cmap, norm=norm)

nearness2 = np.where(np.array(zs_2) < 29, 0, 1)
cmap, norm = clr.from_levels_and_colors(levels = [0,1], colors = ['#9999ff', '#b2b2ff'], extend='max')
ax.scatter(xs_2, ys_2 ,c = nearness2, s=150, marker='.', edgecolor='none', cmap=cmap, norm=norm)

nearness3 = np.where(np.array(zs_3) < 33, 0, 1)
cmap, norm = clr.from_levels_and_colors(levels = [0,1], colors = ['#6666ff', '#7f7fff'], extend='max')
ax.scatter(xs_3, ys_3 ,c = nearness3, s=150, marker='.', edgecolor='none', cmap=cmap, norm=norm)

nearness4 = np.where(np.array(zs_4) < 36, 0, 1)
cmap, norm = clr.from_levels_and_colors(levels = [0,1], colors = ['#3232ff', '#4c4cff'], extend='max')
ax.scatter(xs_4, ys_4 ,c = nearness4, s=150, marker='.', edgecolor='none', cmap=cmap, norm=norm)

nearness5 = np.where(np.array(zs_5) < 40, 0, 1)
cmap, norm = clr.from_levels_and_colors(levels = [0,1], colors = ['#0000b2', '#1919ff'], extend='max')
ax.scatter(xs_5, ys_5 ,c = nearness5, s=150, marker='.', edgecolor='none', cmap=cmap, norm=norm)

nearness6 = np.where(np.array(zs_6) < 44, 0, 1)
cmap, norm = clr.from_levels_and_colors(levels = [0,1], colors = ['#000019', '#00007f'], extend='max')
ax.scatter(xs_6, ys_6 ,c = nearness6, s=150, marker='.', edgecolor='none', cmap=cmap, norm=norm)


# blue hexstring color chart -

#000019 darkest
#00007f
#0000b2
#1919ff
#3232ff
#4c4cff
#6666ff
#7f7fff
#9999ff
#b2b2ff
#ccccff
#e5e5ff lightest



plt.show()