#Write code that makes the robot move twice and then prints 
#out the resulting distribution, starting with the initial 
#distribution p = [0, 1, 0, 0, 0]

# probability (position)
# we are in 2nd cell
p=[0.2, 0.2, 0.2, 0.2, 0.2]

# color of cells
world=['green', 'red', 'red', 'green', 'green']

# we first saw red, then we saw green!
measurements = ['red', 'green']

# we do 2 motions...
motions = [1,1]

pHit = 0.6
pMiss = 0.2

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# "product" (multiplication)
# "Bayes Rule"
def sense(p, Z):
     q=[]
     for i in range(len(p)):
          hit = (Z == world[i])
          q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
     # normalize
     s = sum(q)
     for i in range(len(q)):
          q[i] = q[i] / s
     return q


# "convolution" (addition)
# "Total Probability"
def move(p, U):
     q = []
     for i in range(len(p)):
          s = pExact * p[(i-U) % len(p)]
          s = s + pOvershoot * p[(i-U-1) % len(p)]
          s = s + pUndershoot * p[(i-U+1) % len(p)]
          q.append(s)
     return q

#p = sense(p,measurements[0])
#p = move(p,motions[0])

#p = sense(p,measurements[1])
#p = move(p,motions[1])

for k in range(len(measurements)):
     p = sense(p, measurements[k])
     p = move(p, motions[k])

print p
