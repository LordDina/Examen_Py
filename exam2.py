s = input("entrez une chaine : ")

score = 0  
i = 0
while i < len(s) - 1:

    ascii1 = ord(s[i])
    ascii2 = ord(s[i+1])

    if ascii1 > ascii2:
        difference = ascii1 - ascii2
    else:
        difference = ascii2 - ascii1

    score += difference

    i += 1 

print("le score est :", score)
