outerR = 1
innerR = 0.5
nPoints = 16
nEnclosed = 0

import random
import math

#Calculate the true area of the donut
outerA = math.pi * outerR * outerR
innerA = math.pi * innerR * innerR

actualA = outerA - innerA

#Choose a random point
x = random.random()
y = random.random()

for i in range(nPoints):
    #Calculate the value of the point chosen
    val = x ** 2 + y ** 2
    
    #If the value is within the bounded area, add one to the enclosed curve
    if (val >= 0.25) and (val <= 1):
        nEnclosed += 1
    #Choose new point    
    x = random.random()
    y = random.random()

#Calculate the area enclosed by the curves via MC method
A_enclosed = (outerR ** 2) * (nEnclosed/nPoints) * 4
print("A_enclosed: " + str(A_enclosed))
print("A_true: " + str(actualA))

#Calculate the error in the MC method
error = abs(A_enclosed - actualA) / actualA
print("Error: " + str(error))