from rfpy import random_execute

iter = 10000
a_num, b_num, c_num = 0, 0, 0

def a():
    global a_num
    a_num += 1

def b():
    global b_num
    b_num += 1

def c():
    global c_num
    c_num += 1

for i in range(iter):
    random_execute((a,b,c),(1,2,1))

print(f'{a_num*100/iter}% {b_num*100/iter}% {c_num*100/iter}%')