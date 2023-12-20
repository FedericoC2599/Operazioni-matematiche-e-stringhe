#Il ciclo for

fondo=1000.0

while (fondo>0):
    #Si acquistano prodotti fino a quando il fondo non è esaurito.

    prezzo=float(input("Il prezzo del prodotto ammonta a: "))

    if (fondo<prezzo):
        
        #Se il prodotto ha un prezzo maggiore del fondo disponibile, sarà necessario acquistare un prodotto il cui prezzo devo essere
        #di costo inferiore almeno alla differenza stampata dalla funzione print.

        print("Fondi insufficienti, la somma supplementare per acquistare il prodotto è pari a", prezzo - fondo)
        
                        
    else:

        #Se il prodotto ha un prezzo inferiore al fondo disponibile, allora si può procedere all'acquisto e la funzione
        #print stampa il fondo residuo utile all'acquisto di ulteriori prodotti
        fondo=fondo - prezzo 
        print("Il fondo residuo ammonta a:", fondo)

print("Il fondo è esaurito")

fondo=100
spesa=0

while(fondo>spesa):

    #Calcola la spesa avvenuta in seguito all'acquisto di prodotti, cumulando le spese di tutti i prodotti

    prod=float(input("Prezzo del prodotto "))
    spesa=spesa + prod
#Quando il prezzo del prodotto è superiore al fondo, l'acquisto di prodotti si interrompe.
    
print("Fondi insufficienti")

residuo=fondo - (spesa - prod)
integrazione=prod - residuo

#Quando il prezzo del prodotto è maggiore del fondo, termina l'acquisto di prodotti e viene stampato il credito residuo.
#Inoltre viene stampato il credito che sarebbe stato necessario per l'acquisto del prodotto.

print("Il credito residuo è: ", residuo)
print("Denaro aggiuntivo necessario per l'acquisto del prodotto è pari a:", integrazione)