from rfpy import random_execute

def a(arg):
    print(f'25% A got \'{arg}\'')

def b(arg):
    print(f'50% B got \'{arg}\'')

def c(arg):
    print(f'25% C got \'{arg}\'')

random_execute((a,b,c), (1,2,1), [["This is going to A"],["And this goes to B"],["To C"]])

random_execute((a,b,c), (1,2,1), [["This goes to ALL"]])

#List is recommanded for args, but any iterable object can be used(including string)
#List or dictionary is recommanded for objects inside args, (same)