# This program calculates different geometrical characteristics of a polygon shape.

print("This program calculates different geometrical characteristics of a polygon shape")

#Request number of points from user
n=int (input("Enter the number of polygon points:"))

x = []
y = []

#Request x and y coordinates from user
print()
print ('Enter the x and y coordinates for the polygon points:..')
print()

for i in range(n):
    xInput = float (input(f'x [{i + 1}]: '))
    yInput = float (input(f'y [{i + 1}]: '))
    
    x.append(xInput)
    y.append(yInput)

print()


Ax, Sx, Sy, Ix, Iy, Ixy, Xt, Yt, Ixt, Iyt, Ixyt=0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0

#Calculate the polygon geometric characteristics
for i in range(n - 1):
    Ax = Ax + (x[i+1] + x[i]) * (y[i+1] - y[i])  
    Sx = Sx + (x[i+1] - x[i]) * (y[i+1]**2 + y[i]*y[i+1]+ y[i]**2)  
    Sy = Sy + (y[i+1] - y[i]) * (x[i+1]**2 + x[i]*y[i+1]+ x[i]**2)  
    Ix = Ix + (x[i+1] - x[i]) * (y[i+1]**3 + y[i]**2*y[i+1] + y[i+1]**2*y[i]+ y[i]**3)  
    Iy = Iy + (y[i+1] - y[i]) * (x[i+1]**3 + x[i]**2*y[i+1]+ x[i]*y[i+1]**2 + x[i]**3)  
    Ixy = Ixy + (y[i+1] - y[i]) * (y[i+1]*(3*x[i+1]**2 + 2*x[i]*x[i]+x[i]**2) + y[i]*(3*x[i]**2 + 2*x[i+1]*x[i] + x[i+1]**2))
    
Ax = 0.5*Ax
Sx = -Sx/6
Sy = Sy/6
Ix = -Ix/12
Iy = Iy/12
Ixy = -Ixy/24
Xt = Sy/Ax
Yt = Sx/Ax
Ixt = Ix - (Yt**2*Ax)
Iyt = Iy - (Xt**2*Ax)
Ixyt = Ixy + Xt*Yt*Ax


#Display data in a table
print()
print(f"{'Point':>5} {'x':>10} {'y':>10}")
print("-" *30)
for i in range(n):
    print(f"{i+1:<5} {x[i]:>10.2f} {y[i]:>10.2f}") 



#Display final results 
print('Geometric characteristics: ') 
print(f"{'Ax:':<10} {Ax:<10.2f}")
print(f"{'Sx:':<10} {Sx:<10.2f}")
print(f"{'Sy:':<10} {Sy:<10.2f}")
print(f"{'Ix:':<10} {Ix:<10.2f}")
print(f"{'Iy:':<10} {Iy:<10.2f}")
print(f"{'Ixy:':<10} {Ixy:<10.2f}")
print(f"{'Xt:':<10} {Xt:<10.2f}")    
print(f"{'Yt:':<10} {Yt:<10.2f}")
print(f"{'Ixt:':<10} {Ixt:<10.2f}")
print(f"{'Iyt:':<10} {Iyt:<10.2f}")
print(f"{'Ixyt:':<10} {Ixyt:<10.2f}")        
