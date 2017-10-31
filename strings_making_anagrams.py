#Roberto Del Valle Rodriguez - String: Making Anagrams

'''
Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make
a and b anagrams. Any characters can be deleted from either of the strings.

Sample Input:
cde
abc

Sample Output:
4
'''

def number_needed(a, b):
        deletions = 0
        a = list(a)
        b = list(b)
        d = {}
        d['a'] = 0
        d['b'] = 0
        d['c'] = 0
        d['d'] = 0
        d['e'] = 0
        d['f'] = 0
        d['g'] = 0
        d['h'] = 0
        d['i'] = 0
        d['j'] = 0
        d['k'] = 0
        d['l'] = 0
        d['m'] = 0
        d['n'] = 0
        d['o'] = 0
        d['p'] = 0
        d['q'] = 0
        d['r'] = 0
        d['s'] = 0
        d['t'] = 0
        d['u'] = 0
        d['v'] = 0
        d['w'] = 0
        d['x'] = 0
        d['y'] = 0
        d['z'] = 0
        d2 = dict(d)
        for character in a:
                d[character] +=1
        for character in b:
                d2[character] +=1

        for key in d:
                if key in d2:
                        if d[key] > d2[key]:
                                while d[key] > d2[key]:
                                        d[key]-=1
                                        deletions+=1
                        elif d2[key] > d[key]:
                                while d2[key] > d[key]:
                                        d2[key]-=1
                                        deletions+=1
                else:
                        deletions+=dictionary[key]
        return deletions

a = input()
b = input()

print (number_needed(a,b))