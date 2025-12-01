p = input("entrez une phrase: ")

length = 0
i = len(p) - 1

while i>= 0 and p[i] == " ":
    i = i-1
    
while i>= 0 and p[i] != " ":
    length += 1
    i = i-1
    
print("la longueur est", length)