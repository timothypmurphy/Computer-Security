import itertools
import hashlib
import csv

def foo(x):
     yield from itertools.product(*([x] * 5)) 

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

d = dict()
l = dict()
with open('rockyou-samples.md5.txt', 'r') as f:
     temp = f.read().splitlines()
     for line in temp: 
          if line in l:
               l[line] += 1
          else :
               l[line] = 1      
for x in foo('abcdefghijklmnopqrstuvwxyz1234567890'):
     w = ''.join(x)
     h = computeMD5hash(w)
     #print(w)
     if h in l: 
          d[w] = l[h]
         
          print(w)
          
     #f = open("rockyou-samples.md5.txt", "r")
w = csv.writer(open("output.csv", "w"))

file = open("md5-cracked.txt","w")
s = ""

for key, val in d.items():
    w.writerow([key, val])
    s += str(val) + "," + key + "\n"
s = s[:-1]
file.write(s)