import random

# dec_err is the percentange of errors in decimal form , i.e: 0,5 , 0,125 etc
def error_gen(Array, decimal_err):
    array_size = len(Array)
    errors = (int) (decimal_err * array_size)-1 # Number of elements with wrong values -1 in integer form

    for i in range(0, errors):
        r = random.randint(0, array_size-1) #Get a random element from the list
        if (Array[i] == 0): #Change it accordingly
            Array[i] = 1
        else:
            Array[i] = 0
    return
