float_increment = 1.03 # random
start = 57.24 # random
floating_point = start
loop_range=10 ** 7

for i in xrange(loop_range):
    for j in range(10):
        floating_point += float_increment

# This is done 6 years ago. I know much more 