# Enter your code here. Read input from STDIN. Print output to STDOUT
d = dict()
n = int(input())

for i in range(0, n):
    name, number = input().split()
    d[name] = number
    
for i in range(0, n):
    name = input()
    if name in d:
        print("{}={}".format(name, d[name]))
    else:
        print("Not found")

#Help by https://github.com/ehouarn-perret/EhouarnPerret.Python.HackerRank/blob/master/0%20-%20Tutorials/30%20Days%20of%20Code/Day%208%20-%20Dictionaries%20and%20Maps.py

