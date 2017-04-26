

num_lines = sum(1 for line in open('/Users/ajstein/Documents/allostery/failure.txt'))
sum_lines = sum(int(line) for line in open('/Users/ajstein/Documents/allostery/failure.txt'))

print('Total Failures: ', sum_lines)
print('Success Ratio: ', (num_lines - sum_lines)*100./num_lines, '%')
