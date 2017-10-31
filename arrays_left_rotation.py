#Roberto Del Valle Rodriguez - Arrays: Left Rotation

'''
Given an array of n integers and a number d, perform left rotations
on the array. Then print the updated array as a single line of
space-separated integers.

Sample Input:
5 4
1 2 3 4 5

Sample Output:
5 1 2 3 4
'''



def array_left_rotation(a, n, k):
        return a[k:] + a[:k]
            
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
