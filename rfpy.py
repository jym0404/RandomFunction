import random

def random_execute(functions, ratios=None, args=None):
    if ratios:
        if len(functions) != len(ratios):
            raise ValueError("The length of functions and ratios must be the same")
    else:
        ratios = [1]*len(functions)

    if len(functions) == 1 or random.random() < ratios[0]/sum(ratios):
        if args == None:
            functions[0]()
        elif len(args) == len(functions):
            if isinstance(args[0], dict):
                functions[0](**args[0])
            else:
                functions[0](*args[0])
        elif len(args) == 1:
            if isinstance(args[0], dict):
                functions[0](**args[0])
            else:
                functions[0](*args[0])
        else:
            raise ValueError("The length of args must be equal to that of functions or 1")
    else:
        if args == None:
            random_execute(functions[1:],ratios[1:])
        elif len(args) == len(functions):
            random_execute(functions[1:],ratios[1:],args[1:])
        elif len(args) == 1:
            random_execute(functions[1:],ratios[1:],args)
        else:
            raise ValueError("The length of args must be equal to that of functions or 1")