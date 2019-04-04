import os

f = open('name.py', 'w')
f.write("hi buddy")

print(os.path.isfile("name.py") and os.path.getsize("name.py") > 0)
