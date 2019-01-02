def even(s):
    se = ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            se += s[i]
    se += " "
    for i in range(0, len(s)):
        if i % 2 != 0:
            se += s[i]
    
    print(se)

n = int(input(""))

for i in range(0, n):
    string = input("")
    even(string)