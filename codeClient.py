from sage.all import *
import random, decimal
size = 4 #The dimensions of the code. Anything > 4 takes a long time to complete...

#Create random binary array of given size
arr = [random.choice([0,1]) for i in range(size)]
print "Original message: ", arr

#Define a new Walsh Code with given dimension
C = codes.WalshCode(size)
word = vector(GF(2), arr)
enc = C.encode(word)
print "Encoded: ", enc

#Error percentage input (with added validation)
try:
    err_margin = decimal.Decimal(raw_input("Please give in the error percentage (Between 0.01 and 0.99): "))
    if err_margin > 0.99 or err_margin < 0.01:
        raise ValueError
except Exception:
    print "Invalid input given..."
    exit(0)

from Error_Gen import error_gen

#Generate errors
error_gen(enc, err_margin)
print "Encoded (now with errors): ", enc

#Transmit with socket
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
print "Waiting for connections..."
(c, addr) = s.accept()
print "Get Connection from", addr, ". Transmitting..."
stuffToSend = "" #Because we need to convert it to a string...
for i in enc:
    stuffToSend += str(i)
c.send(stuffToSend)
c.close()
print "Transmission ended..."
