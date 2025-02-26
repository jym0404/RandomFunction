from rfpy import random_execute

def a():
    print('25% A')

def b():
    print('50% B')

def c():
    print('25% C')

random_execute((a,b,c), (1,2,1))
#Tuple is recommanded, but any iterable object can be used