from sage.all import *
import random, decimal
size = 4

err_margin = decimal.Decimal(raw_input("Please give in the error percentage (Between 0.01 and 0.99): "))

arr = [random.choice([0,1]) for i in range(size)]

from Error_Gen import error_gen


print "Original array: ", arr
C = codes.WalshCode(size)
word = vector(GF(2), arr)
enc = C.encode(word)
print "Encoded: ", enc
error_gen(enc, err_margin)
print "Encoded (now with errors): ", enc
dec = C.decode_to_message(enc)
print "Decoded: ", dec
#print "Basis: ", dec.basis()
