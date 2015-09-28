#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.

# Initial probabilities
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']

# Robot senses red! You can change it to green
Z = 'red'

pHit = 0.6
pMiss = 0.2

def sense(p, Z):
     q=[]
     totalSum = 0

     for i in range(len(p)):
          hit = (Z == world[i])

          val = p[i] * (hit * pHit + (1-hit) * pMiss)
          q.append(val)
          totalSum = totalSum + val

     for i in range(len(p)):
          q[i] = q[i] / totalSum

     return q


print sense(p,Z)
