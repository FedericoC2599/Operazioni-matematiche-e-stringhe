def inverti_stringa(s):
    return s[::-1]

def palindroma(s):
    i = 0;
    j = len(s) - 1
    controllo = False
    while(i < j):
        if(s[i] == s[j]):
            controllo = True
            i = i+1
            j = j-1
        else:
            return False
    return controllo


a="Mi"
b="chiamo"
c="Federico"
d="ho"
e=24
f="anni"
g="e"
h="vivo"
i="a"
l="Milano"

presentazione=a + " " + b + " " + c + ", " + d + " " + str(e) + " " + f + " " + g + " " + h + " " + i + " " + l
'''
print("Io ho: " + str(24) + " " + f)

nome="Federico"
iniziale=nome[0]
finale=nome[7]

finale=presentazione[len(presentazione) - 1]

print(len(presentazione) - 1)

'''
nome="Mauro Rossi"

'''
stringa = s0,s1,...,sn con s carattere contando da 0
stringa[indiceinizio:indicefine] -> indiceinizio INCLUSO, indicefine ESCLUSO contando da 0
'''

print(nome[3:7])
print(nome[:5])
print(nome[2:])

print(nome[::-1])

print(palindroma('anna'))
print(palindroma('ossesso'))
print(palindroma('federico'))
print(palindroma('ediolognomomongoloide'))
