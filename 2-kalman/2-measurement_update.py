#  Measurement Update

#The new belief will be more certain than either the previous belief OR the measurement.
#The takeaway lesson here: more measurements means greater certainty.
# This can be hard to wrap your head around, but multiple measurements ALWAYS gives us a more certain (and therefore taller and narrower) belief.
# 
# or could be called 'update' (see 4-all_in_one.py)
def calcNewPos(mean1,var1, mean2,var2):
     new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
     new_variance = 1 / (1/var1 + 1/var2)
     return [new_mean, new_variance]


# 1) Belief: Position is 10.
# From 8 to 12 (variance = 4.)
#
# 2) Measurement: Our sensors detected that car has moved to 12.
# From 10 to 14 (variance = 4.) 
#
# Calculation will return [11.0, 2.0]
# That means that new position is 11.
# And variance is 2. !!! (please notice - it is much smaller than original! we have reduced uncertainty! we are more confident now!)
print calcNewPos(10., 4., 12., 4.)
