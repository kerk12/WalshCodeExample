size = 4

import socket
s = socket.socket()
host = socket.gethostname()
port = 12345

print "Connecting..."
try:
    s.connect((host, port))
except Exception:
    print "Could not connect. Check that the client is running..."
    
print "Recieving encoded word..."
data_enc = s.recv(1024) #Get the encoded message
s.close()

#Convert it back to a list...
enc_msg = []
for char in data_enc:
    enc_msg.append(int(char))

from sage.all import *

C = codes.WalshCode(size) #Define new walsh code of given size
word = vector(GF(2), enc_msg) #Convert the list to a vector
print "Recieved word: ", word
print "Decoding... Please wait..."
dec = C.decode_to_message(word) #Decode it...
print "Decoded message: ", dec #Print it out...
