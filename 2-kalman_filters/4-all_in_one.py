# KALMAN filter for 1d
# www.udacity.com/course/viewer#!/c-cs373/l-48723604/e-48311864/m-48700413

# Was called 'calcNewPos' before
def update(mean1,var1, mean2,var2):
     new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
     new_variance = 1 / (1/var1 + 1/var2)
     return [new_mean, new_variance]


# Was called 'motionUpdate' before
def predict(x1,variance1, x2,variance2):
     return [x1 + x2, variance1 + variance2]

# That what sensor is telling us:
measurements = [5., 6., 7., 9., 10.]
# That what we were doing:
motion = [1., 1., 2., 1., 1.]

measurement_sig = 4.
motion_sig = 2.

mu = 0.
sig = 10000.

for n in range(len(measurements)):
     [mu, sig] = update(mu, sig, measurements[n], measurement_sig)
     print 'update: ', [mu, sig]

     [mu, sig] = predict(mu, sig, motion[n], motion_sig)
     print 'predict: ', [mu, sig]

