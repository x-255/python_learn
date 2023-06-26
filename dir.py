from os.path import *
from os import *

dirs = listdir('.')
pys: list[str] = []

for d in dirs:
    if d.endswith('.py'):
        pys.append(d)

print(pys)
