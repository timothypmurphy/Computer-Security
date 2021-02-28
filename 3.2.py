import itertools
import hashlib
import csv

def foo(x):
     yield from itertools.product(*([x] * 5)) 

def computesha1hash(my_string):
    m = hashlib.sha1()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

d = dict()
l = dict()
words = ['123456','12345','123456789','password','iloveyou','princess','1234567','rockyou','12345678','abc123','nicole','daniel','babygirl','monkey','lovely','jessica','654321','michael','ashley','qwerty','111111','iloveu','000000','michelle','tigger']

for w in words:
    i = 0
    with open('rockyou-samples.sha1-salt.txt', 'r') as f:
         temp = f.read().splitlines()
         for line in temp: 
            
            salt = line[7:17]
            hash = computesha1hash(salt + w)
            if line[18:] == hash:
                i += 1
    print(w + " " + str(i))
    d[w] = i
        
#for x in foo('abcdefghijklmnopqrstuvwxyz1234567890'):
#     w = ''.join(x)
#     h = computesha1hash(w)
#     #print(w)
#     if h in l: 
#          d[w] = l[h]
#         
#          print(w)
#          
#     #f = open("rockyou-samples.md5.txt", "r")
w = csv.writer(open("outputsalt.csv", "w"))

file = open("salt-cracked.txt","w")
s = ""

for key, val in d.items():
    w.writerow([key, val])
    s += str(val) + "," + key + "\n"
s = s[:-1]
file.write(s)