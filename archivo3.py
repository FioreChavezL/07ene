import collections as cl

counter = cl.Counter()
print(counter)

counter = cl.Counter(['a','a','b'])
print(counter)

counter = cl.Counter(a=2,b=3,c=1)
print(counter)
