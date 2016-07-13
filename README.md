# Walsh Code example in SageMath
##### Implemented by Kyriakos Giannakis (kerk12), Vasilis Zografos, Panagiotis Efstathiadis

This project is a client-server example of Walsh Code encoding and decoding in [SageMath](http://www.sagemath.org/). In this example, the client sends an encoded message to the server, after adding some errors to it. The server then decodes and corrects the errors (or at least tries to...) it and prints it out.

## Usage:
1. Make sure you have SageMath installed
2. git clone...
3. Start the client:
```
sage codeClient.py
```
A random 4-byte binary message will be generated and will be encoded. Type the percentage of the encoded array that you want to scramble. The scrambling will then take place and the final encoded (but now with errors) word will be printed out. You are ready to start the server!
4. Start the server:
```
sage codeServer.py
```
The server will connect via a TCP socket to the client and the encoded word will be "transmitted". The word will be decoded and the server will try to correct the errors. After that is done, the initial message will be printed out (or may be altered, depending on the amount of errors).
