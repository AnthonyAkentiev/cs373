
# Motion is much easier than 'measurement update'

# or could be called 'predict'
def motionUpdate(x1,variance1, x2,variance2):
     return [x1 + x2, variance1 + variance2]

print motionUpdate(8.,4., 10.,6.)
