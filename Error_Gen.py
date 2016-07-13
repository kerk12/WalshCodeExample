import random
#
# L = [0,1,1,0,1,0,0,1,0,1]
# err_in_dec = 0.5
# print L
# print "\n"
# print "=============================="
# print "\n"
#
# error_gen(L, err_in_dec)
# print L

# dec_err is the percentange of errors in decimal form , i.e: 0,5 , 0,125 etc
def error_gen(Array, decimal_err):
    array_size = len(Array)
    errors = (int) (decimal_err * array_size)-1 # Number of elements with wrong values -1 in integer form

    for i in range(0, errors):
        r = random.randint(0, array_size-1)
        if (Array[i] == 0):
            Array[i] = 1
        else:
            Array[i] = 0
    return
