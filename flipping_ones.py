#Roberto Del Valle Rodriguez - Flipping Ones

'''

You are given an integer array with N elements: d[0], d[1], ... d[N - 1]. 
You can perform AT MOST one move on the array: choose any two integers [L, R]
and flip all the elements between (and including) the L-th and R-th bits.
L and R represent the left-most and right-most index of the bits marking
the boundaries of the segment which you have decided to flip.

What is the maximum number of '1'-bits (indicated by S)
which you can obtain in the final bit-string? 

'Flipping' a bit means, that a 0 is transformed to a 1
and a 1 is transformed to a 0 (0->1,1->0).

Input Format 
An integer N 
Next line contains the N bits, separated by spaces: d[0] d[1] ... d[N - 1] 

Output: 
S 

Constraints: 
1 <= N <= 100000 
d[i] can only be 0 or 1 
0 <= L <= R < n 

Sample Input: 
8 
1 0 0 1 0 0 1 0 

Sample Output: 
6 

'''

def flipper(N,bits):
        bit_array = list(map(int, bits))
        left = 0
        n = int(N)
        score = sum(bit_array)
        for i in range(n):
                for k in range(i,n):
                        bit2_array = bit_array[:]
                        for m in range(i,k+1):
                                if bit2_array[m] == 0:
                                        bit2_array[m] = 1
                                elif bit2_array[m] == 1:
                                        bit2_array[m] = 0
                                newscore = sum(bit2_array)
                                if newscore > score:
                                        score = newscore
        return score



def main():
        number_of_bits = input()
        bits = input().strip()
        print (flipper(number_of_bits, bits))


if __name__=="__main__":main()
