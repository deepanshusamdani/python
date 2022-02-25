"""
https://www.hackerearth.com/problem/algorithm/find-the-number-1-e419398c-1f04afca/
"""
import numpy as np
import itertools
N,X,K= map(int, input().split())
S = str(input())

new = []
for index in range(0, len(S), X):
    new.append(S[index : index + X])
out = [x for x in itertools.product(*new)]
def join_tuple_string(strings_tuple):
   return ''.join(strings_tuple)
final = list(map(join_tuple_string, out))
final.sort()
result = final[K-1]
print(result)

# N,X,K = 10,5,10
# S= "1234567891"
