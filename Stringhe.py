def inverti_stringa(s):
    '''
    Funzione che inverte una stringa

    Parametri:
        s -- La stringa da invertire

    Ritorna: La stringa invertita
    '''
    return s[::-1]

def palindroma(s):
    '''
    Funzione riconosce se una stringa è palindroma

    Parametri:
        s -- La stringa di cui verificare l'essere palindroma

    Ritorna: Valore booleano (True o False) che indica se la stringa è palindroma o meno
    '''
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

def conta_lettere(s):
    '''
    Funzione che conta le vocali e le consonanti di una stringa

    Parametri:
        s -- La stringa di cui contare le vocali e le consonanti

    Ritorna: Una lista di due elementi indicante in ordine il numero di vocali e di consonanti
    '''
    vocali=0
    consonanti=0
    for carattere in s:
        
        if carattere.isalpha():
            if carattere.lower() in ['a','e','i','o','u']:
                vocali = vocali + 1
            else:
                consonanti = consonanti + 1
    return [vocali,consonanti]

def presentazione(*args):
    '''
    Funzione che concatena più argomenti in una stringa

    Parametri:
        *args -- Argomenti da concatenare in una stringa

    Ritorna: La stringa risultante dalla concatenazione degli argomenti
    '''
    stringa = ""
    for arg in args:
        stringa = stringa + str(arg) + ' '
    return stringa




