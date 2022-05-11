to run the program:
open terminal on the current folder where the program is at, then run:

>>> python3 RSAParameter.py p_bit_length q_bit_lenth

the program only accept 32 bit length integer for both p and q

example:

>>> python3 RSAParameter.py 32 32

<br/>
the program will take the bit-length (at least 32) of p and q as input, and
produce the following parameters in an output file out.txt.<br/> 
it will generate:<br/>
p: the value of p<br/>
q: the value of q<br/>
N: p*q<br/>
e: the public/encryption key<br/>
d: the private/decryption key<br/>
