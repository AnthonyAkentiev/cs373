# The function localize takes the following arguments:
#
# colors:       a 2D list, each entry either 'R' (for a red cell) or 'G' (for a green cell)
#
# measurements: a list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:      a list of actions taken by the robot, each entry of the form [dy,dx], where
#               dx refers to the change in the x-direction (positive meaning movement to the right)
#               and dy refers to the change in the y-direction (positive meaning movement downward)
#               NOTE: the *first* coordinate is change in y; the *second* coordinate is change in x
#
# sensor_right: a float between 0 and 1, giving the probability that any given measurement is
#               correct; the probability that the measurement is incorrect is 1-sensor_right
#
# p_move:       a float between 0 and 1, giving the probability that any given movement command takes
#               place; the probability that the movement command fails (and the robot remains still);
#               the robot will NOT overshoot its destination in this exercise
#
# The function should RETURN (not just show) a 2D list (of the same dimensions as colors) that 
# gives the probabilities that the robot occupies each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform probability of being 
# in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
    # Repeat the sense-measure loop as measures exist
    columns = (len(colors[0]))
    rows = (len(colors))
    q=[[0.0 for row in range(len(colors[0]))] for col in range(len(colors))]
    s=0.0
    for k in range(len(measurements)):
        # This is the function move
        s=0.0
        q=[[0.0 for row in range(len(colors[0]))] for col in range(len(colors))]
        for j in range(columns):
            for i in range(rows): 
                s = p_move * p[(i-motions[k][0]) % rows][(j-motions[k][1]) % columns] 
                s = s + (1-p_move) * p[i % rows][j % columns]
                q[i][j] = s
        p = q[:]
        #show(p)
        #This is the function sense  
        s=0.0
        # Update the q matrix using the prior p and the measurement Z
        for j in range(columns):
            for i in range(rows):
                hit = (measurements[k] == colors[i][j])
                q[i][j]=(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
            #show(p)
            #show(q)
   
        # Normalize q, so it is a valid probability distribution
        for j in range(columns):
            for i in range(rows):
                s = s + q[i][j]
        for j in range(columns):
            for i in range(rows):
                q[i][j] = q[i][j]/s
        p = q[:]
        #show(p)
        #print(k)
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'

#############################################################    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8
p = localize(colors,measurements,motions,sensor_right,p_move)
show(p) # displays your answer
