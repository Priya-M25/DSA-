''' Problem statement:-

There is a song concert going to happen in the city. The price of each ticket is equal 
to the number obtained after reversing the bits of a given 32 bits unsigned integer ‘n’.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
2
0
12
Sample Output 1:
 0
 805306368
Explanation For Sample Input 1 :
For the first test case :
Since the given number N = 0 is represented as 00000000000000000000000000000000 in 
its binary representation. So after reversing the bits, it will become 00000000000000000000000000000000 which is 
equal to 0 only. So the output is 0.     

For the second test case :
Since the given number N = 12 is represented as 00000000000000000000000000001100 in its binary representation. 
So after reversing the bits, it will become 0110000000000000000000000000000, which is equal to 805306368 only. So the output is 805306368.
'''
''' Output :-

Original number: 12
Reversed number: 805306368
'''

def reverseBits(n):
    bn = bin(n)[2:].zfill(32)  # Convert integer to binary and pad with zeros to make it 32 bits
    rb = bn[::-1]  # Reverse the binary string
    rn = int(rb, 2)  # Convert the reversed binary string back to an integer
    return rn

# Example usage
n = 12
print("Original number:", n)
print("Reversed number:",reverseBits(n))
