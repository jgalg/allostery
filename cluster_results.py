import os
import numpy as np

rootdir = '/Users/ajstein/Documents/allostery/output_files/'

avg = []

for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        num_lines = sum(1 for line in open(rootdir + f))
        sum_lines = sum(int(line) for line in open(rootdir + f))
        # print('Success Ratio: ', (num_lines - sum_lines)*100./num_lines, '%')
        print((num_lines - sum_lines)*100./num_lines, '%')
        x = (num_lines - sum_lines)*100./num_lines
        avg.append(x)

print(avg)
print(np.mean(avg))

# num_lines = sum(1 for line in open('/Users/ajstein/Documents/allostery/failure.txt'))
# sum_lines = sum(int(line) for line in open('/Users/ajstein/Documents/allostery/failure.txt'))
#
# print('Total Failures: ', sum_lines)
# print('Success Ratio: ', (num_lines - sum_lines)*100./num_lines, '%')
