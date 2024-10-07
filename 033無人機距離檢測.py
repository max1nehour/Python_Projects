n = int(input())
list =[]
for i in range(n):
  drone = str(input())
  drone = drone.split()
  #print(drone)
  list.append(drone)
#print(list)
#print(len(list))

#sqrt( (x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2 )
import math

def distance(a,b):
  a = [int(i) for i in a]
  b = [int(i) for i in b]
  dist = math.sqrt((a[1]-b[1])**2 +  (a[2]-b[2])**2 + (a[3]-b[3])**2)
  #print("dist",dist)
  return dist

closest = []
min_distance = float('inf')

for i in range(len(list)):
        for j in range(i + 1, len(list)):
            dist = distance(list[i], list[j])
            #print("i:{} j:{}".format(i+1,j+1))
            closest.append([i+1,j+1,dist])

closest = sorted(closest, key= lambda x: x[2])

#print(closest)
#print(closest[:3])
final = closest[:3]

for i in range(3):
    print(final[i][0],final[i][1],end = " ")
    x, y = final[i][0], final[i][1]
    print(list[x-1][1],list[x-1][2],list[x-1][3],list[y-1][1],list[y-1][2],list[y-1][3])
    
