# collections.Counter lets you find the most common
# elements in an iterable:


import collections



c = collections.Counter('helloworld')

print("--"*50)
print("Counter result")
print(c)

print("--"*50)
print("The most 3 common elements in the string 'helloworld'")

print(c.most_common(3))
