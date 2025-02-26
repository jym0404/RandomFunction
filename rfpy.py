import random

def random_execute(functions, ratios=None):
    if ratios:
        if len(functions) != len(ratios):
            raise ValueError("The length of functions and ratios must be the same")
    else:
        ratios = [1]*len(functions)
    
    if len(functions) == 1:
        functions[0]()
        return

    if random.random() < ratios[0]/sum(ratios):
        functions[0]()
    else:
        random_execute(functions[1:],ratios[1:])