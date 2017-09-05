# Simple add and subtract operations
import fileinput

lines = []
i = 0

for line in fileinput.input():
    a = ''
    b = ''
    while line[i] != " ":
        a += line[i]
        i += 1
    i += 1
    while line[i] != "\n":
        b += line[i]
        i += 1

    i = 0
    a = int(a)
    b = int(b)
    c = a+b
    print(c)

#