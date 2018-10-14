

import math

fun_str = input("Please input a function: ")
x_max = float(input("Please input x-max: "))
x_min = float(input("Please input x-min: "))
ns = int(input("Please input the number of points you'd like to graph: "))
xs=[]
ys=[]
i= x_min
evenly_divided = (x_max-x_min)/ns
j = 0
while i <= x_max + 1:
    xs.append(i)
    i+=evenly_divided
    print(xs[j], " ")
    j+=1
    
for x in xs:
    y = eval(fun_str)
    ys.append(y)

first_line = '{0:<12s} | {1:<12s}'.format('x','y')
print(first_line)
print('-'*27)

for i in range(ns+1):
    print('{0:>+12.4f} | {1:>+12.4f}'.format(xs[i],ys[i]))
    #print(xs[i])
    #print(ys[i])'''
    



'''plot(xs, ys, marker='o', linestyle='-')
xlabel('x')
ylabel('y')
title(fun_str)
show()'''
