from rfpy import random_execute

def a(arg1, arg2, arg3):
    print(f'{arg1} {arg2} {arg3}')

def b(arg1, arg2, arg3):
    print(f'{arg1} {arg2} {arg3}')

random_execute((a,b), (1,1), [{"arg1":"a arg1", "arg2":"a arg2", "arg3":"a arg3"}, ["b arg1", "b arg2", "b arg3"]])
#List is recommanded for args, but any iterable object can be used(including string)
#List or dictionary is recommanded for objects inside args, (same)