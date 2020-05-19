import math
# conversion of cartesian coordinates to polar
def cartesiantopolar(x,y):
    radius=math.sqrt(x*x + y*y)
    theta=math.atan(y/x)
    theta = 180 * theta/math.pi
    return radius,theta
# conversion of polar coordinates to cartesian
def polartocartesian(radius,theta):
    theta = theta * math.pi/180.0
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    return x,y

case=input('Enter your case:')
print(case)
# prompting the user
if (case=='2'):
   x = float(input('Enter value of x: '))
   y = float(input('Enter value of y: '))
   s=cartesiantopolar(x,y)
   print(s)
elif (case=='1'):
   radius=float(input('Enter value of radius:'))
   theta=float(input('Enter value of theta:'))
   z=polartocartesian(radius,theta)
   print(z)

else:
    print('Nothing')
