def condizionatore(soglia,attuale):
    if attuale > soglia :
        print('Accendere il condizionatore')
    else: 
        print('La temperatura è ancora accettabile')

def diverso_da(x,y):
    return x != y

def uguale_a(x,y):
    return x == y

def verifica_uguaglianza(x,y):
    if(diverso_da(x,y)):
        print("Valori diversi")
    else:
        print("Valori uguali")

def misura_Richter(richter):
    if richter >=8.0:
        print('Distrutta la quasi totalità delle strutture')
    elif richter >=7.0:
        print('Molte strutture sono distrutte')
    elif richter >=6.0:
        print('Molte strutture danneggiate, alcune distrutte')
    elif richter >=4.5:
        print('danni alle strutture più deboli di media e bassa entità')
    else:
        print('nessun danno a strutture')

def esito_test(test):
    if (test):
        print('Il test è andato a buon fine')
    else:
        print ('Il test ha avuto esito negativo')


def stato_materiale_acqua(temp):
    if temp> 0 and temp<100:
        print("L'acqua è allo stato liquido")
    elif temp<=0:
        print("L'acqua è allo stato solido")
    else:
        print("L'acqua è allo stato gassoso")