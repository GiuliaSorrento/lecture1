import copy

from gestionale.core.prodotti import ProdottoRecord

p1 = ProdottoRecord("Laptop",1200.0)
p2 = ProdottoRecord("Mouse",20.0)
p3= ProdottoRecord("Auricolari",250.0)

carrello = [p1,p2,p3, ProdottoRecord("tablet", 700.0)] #lista

print("prodotti nel carrello:")
for i,p in enumerate(carrello):   #enumerate metodo prende come argomento una lista e restituisce una lista di tuple indice, elemento
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#aggiungere a una lista
carrello.append(ProdottoRecord("Monitor", 150.0))
#ordino lista
carrello.sort(key = lambda x: x.prezzo_unitario, reverse = True)  #ordino in base al prezzo unitario(con reverse decrescente), equivalente a itemgetter
print("prodotti nel carrello ordinati:")
for i,p in enumerate(carrello):   #enumerate metodo prende come argomento una lista e restituisce una lista di tuple indice, elemento
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"totale nel carrello: {tot}")

#aggiungere
carrello.append(ProdottoRecord("prodotto", 20.0)) #aggiunge singolo elemento
carrello.extend([ProdottoRecord("prodotto", 20.0),ProdottoRecord("prodotto", 20.0)])  #aggiunge elementi in una lista, o più elementi
carrello.insert(2,ProdottoRecord("prodotto", 20.0))   #inserisce l'oggetto in quell'indice

#rimuovere
carrello.pop() #rimuove l'ultimo elemento
carrello.pop(2)  #rimuove elemento in posizione 2
carrello.remove(p1)   #scorro tutta la lista, cerco p1, quando trovo p1 lo levo e poi esco, ma la lista può contentere p1 più volte,
                      #sto eliminando la prima occorrenza che trovo di p1
#carrello.clear()   #pulisce tutto

#sorting- modificano la lista, una volta chiamati quella lista è stata modificata, non va bene se ci sto ciclando sopra
#carrello.sort()  #ordina seguendo ordinamento naturale, non funziona se prodotto recordo non ha metodo __lt__
#carrello.sort(reverse=True)   #ordina al contrario
#carrello.sort(key= function)  #function(lambda, itemgetter)
#carrello_ordinato =sorted(carrello)   #ordina la copia della lista, ora hai due liste una ordinata e una no
carrello.reverse()   #restituisce la lista al contrario, inverte l'ordine
carrello_copia = carrello.copy()  #crea una nuova lista che è la copia di carrello, #shallow copy, stessi identici oggetti di carrello
                                  #se modifico un oggetto p1, viene modificato in entrambe le liste
                                  #ha senso se mi voglio portare dietro gli stessi medesimi oggetti
carrello_copia2 = copy.deepcopy(carrello)   #gli oggetti della copia sono distinti dagli oggetti della lista originale, fa una copia degli oggetti
                                               #le hashfunction sono uguali ma gli indirizzi di memoria sono diversi

#TUPLE
sede_principale = (45,8)  #latitudine e longitudine della sede di torino
sede_milano = (45,9)
#kat e long non cambiano mai, uso una tupla e non una lista

print(f"sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")  #accedo allo stesso modo di una lista


aliquotaIVA = (
("Standard", 0.22),
("Ridotta", 0.10),
("Alimentari", 0.04),
("Esente", 0.0)
)   #tupla di tuple
#posso ciclare su una tupla di tuple

for descr,valore in aliquotaIVA:
    print(f"{descr}: {valore*100}%")


def calcola_statistiche_carrello(carrello):
    """"Restituisce prezzo totale, prezzo medio, massimo, minimo"""
    prezzi =[p.prezzo_unitario for p in carrello]   #metto nella lista prezzi tutti i prezzi presenti nel carrello
    return(sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))    #posso restituire con una tupla

#tupla = calcola_statistiche_carrello(carrello)
#tot,media,max,min = calcola_statistiche_carrello(carrello)    #fa l'unpacking di questi argomenti, si può fare solo se il numero degli argomenti è quello esatto
tot, *altri_campi =  calcola_statistiche_carrello(carrello)   #il primo elemento della tupla viene messo in tot e gli altri campi in una tupla

print(tot)


#SET
categorie ={"Gold", "Silver", "Bronze", "Gold"}  #il duplicato non viene inserito
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "elite", "Gold"}
#categorie_all = categorie.union(categorie2)   #unisco due set: .union(zzz)
categorie_all = categorie | categorie2    #unione
categorie_comuni = categorie & categorie2   #solo elementi comuni
print(categorie_all)  #nessun ordinamento particolare
print(categorie_comuni)   #solo gold
categorie_eslcusive = categorie- categorie2  #solo gli elementi presenti in uno dei due set
print(categorie_eslcusive)
categorie_esclusive_simmetrico = categorie^categorie2 #differenza simmetrica
print(categorie_esclusive_simmetrico) #elementi nel primo set non contenuti nel secondo e anche elementi del secondo non contenuti nel primo


prodotti_ordinaA = {ProdottoRecord("Laptop", 1200.0), ProdottoRecord("Mouse", 20.0), ProdottoRecord("Tablet", 700.0)}
prodotti_ordinaB = {ProdottoRecord("Laptop2", 1200.0), ProdottoRecord("Mouse2", 20.0), ProdottoRecord("Tablet", 700.0)}

#metodi utili per i set
s = set()    #insieme vuoto
s1 = set()
s.add(ProdottoRecord("aaa", 20.0))   #aggiungo un elemento
s.update([ProdottoRecord("aaa", 1200.0), ProdottoRecord("bbb", 20.0)]) #aggiunge più elementi, li metto dentro una lista

#togliere
s.remove(elem)   #se non esiste elemento, da errore come key error
s.discard(elem)  #rimuove un elemento SENZA ARRABBIARSI SE QUESTO NON ESISTE, EVIT0 DI DOBER GESTIRE UN'ECCEZIONE
s.pop()  #rimuove e restituisce un elemento arbitrario, visto che non abbiamo un ordinamento, casuale
s.clear() #svuota il set

#operazioni di tipo insiemistico
s.union(s1)   #unisce s e s1, genera un set che unisce i due set di partenza
s.intersection(s1) #and, crea un set con solo gli elementi comuni
s.difference(s1) #s-s1, elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #differenza simmetrica

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s)       #se gli elmenti di s sono contenuti in s1
s1.isdisjoint(s)  #True se gli elementi di s e di s1 sono tutti diversi

#dizionario

