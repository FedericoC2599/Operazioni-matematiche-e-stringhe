def area_triangolo(base,altezza):
    '''
    Calcolo dell'area di un generico triangolo
    
    Parametri:
        base -- Base del triangolo
        altezza -- Altezza del triangolo
        
    Ritorna: Area del triangolo calcolata come base per altezza diviso due
    '''
    area=(base*altezza)/2
    return area

def volume_cubo(lato):
    '''
    Calcolo del volume di un generico cubo
    
    Parametri:
        lato -- Misura del lato del cubo
        
    Ritorna: Volume del cubo calcolato come lato al cubo
    '''
    volume=lato**3
    return volume

'''
    Calcolo dell'area di un generico rombo
    
    Parametri:
        base -- Misura della base del rombo
        altezza -- Misura dell'altezza del rombo
        
    Ritorna: Area del rombo secondo la formula base per altezza
    '''
def area_rombo(base, altezza):
    area=base*altezza
    return area

def stampa_quadrato(lato):
    if lato<1: return

    stampa_quadrato(lato-1)
    
    print("[]"*lato)

