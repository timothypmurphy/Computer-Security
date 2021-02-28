import itertools
import hashlib
import csv
import bcrypt

def foo(x):
     yield from itertools.product(*([x] * 5)) 

def computesha1hash(my_string):
    m = hashlib.sha1()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

l = []
word = '123456'

with open('rockyou-samples.bcrypt.txt', 'r') as f:
     i = 0
     temp = f.read().splitlines()
     for line in temp: 
        i+=1
        if bcrypt.hashpw(word.encode('utf-8'), line.encode('utf-8')) == line.encode('utf-8'):
            l.append(i)
            print(i)
        if len(l) > 5:
            break

w = csv.writer(open("outputsalt.csv", "w"))

file = open("bcrypt-lines.txt","w")
s = ""

for line in l[0:5]:
    s += str(line) + "\n"
s = s[:-1]
file.write(s)