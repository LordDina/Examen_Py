val = {
    "I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000
}

s = input("entrer le chiffre : ")

n = 0
i = 0

while i < len(s):

    val_cur = val[s[i]]

    if i + 1 < len(s):
        val_next = val[s[i + 1]]
    else:
        val_next = 0 
    if val_cur < val_next:
        n += val_next - val_cur
        i = i + 2 
    else:
        n = val_cur + n
        i = i + 1

print("la sortie  est =", n)
