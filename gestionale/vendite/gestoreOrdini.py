#scrivere un software gestionale
#1) supportare l'arrivo e la gestione degli ordini
#2)quando arriva un nuovo ordine lo aggiungo in coda, assicurandomi che sia eseguito dopo gli altri
#3)avere statistiche sugli ordini
#4)fornire statistiche sulla distribuzione degli ordini per categorie di clienti
from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def addOrdine(self,ordine: Ordine):
        """Aggiunge un nuovo ordine agli elementi da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"ordini ancora da evadere: {self._ordini_da_processare}")

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        if not self._ordini_da_processare:    #se non ci sono ordini nella coda
            print(f"non ci sono ordini in coda")
            return False

        ordine = self._ordini_da_processare.popleft() #logica fifo

        print(f"sto processando l'ordine di {ordine.cliente}")
        #print(ordine.riepilogo())

        for riga in ordine.righe:   #ciclo su tutte le righe del mio ordine, per ognuna vado a aggiornare la mia collections di statistiche su ogni prodotto
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita   #la chiave è il nome del prodotto e la quantità è la frequenza, che aggiorno

        #RAGGRUPPARE GLI ORDINI PER CATEGORIA
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("ordine correttamente processato")
        return True


    def processa_tutti_ordini(self):
        """Processa tutti gli ordini attualmente in coda"""
        print(f"processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()

        print(f"tutti gli ordini sono processati")

    def get_statistiche_prodotti(self, top_n: int = 5):    #se non mi passi un intero usa il 5 di default
        """Questo metodo restituisce infor sui prodotti più venduti"""
        valori = []
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantita))   #lista di tuple
            return valori


    def get_distribuzione_categoria(self):
        """restutuisce info su totale fatturato per ogni categoria"""
        for categorie in self._ordini_per_categoria.keys():   #cicla sulle categorie
            valori = []
            ordini = self._ordini_per_categoria[categorie]
            totale_fatturato = sum([o.totale_lordo(0.22) for o in ordini])  #per ogni ordine mi prendo il totale lordo e poi li sommo tutti
            valori.append((categorie, totale_fatturato))


    def get_riepilogo(self):
        """info di """
        print("\n" + "-"*58)
        print("stato attuale del business")
        print(f"ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"ordini in coda {len(self._ordini_da_processare)}")

        print("prodotti più venduti")
        for prod,quantita in self.get_statistiche_prodotti():
            print(f"{prod}---{quantita}")


def test_module():   #è un metodo del modulo non della classe
    sistema = GestoreOrdini()    #crea un'istanza della classe gestore ordini

    ordini= [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0),1), RigaOrdine(ProdottoRecord("mouse", 70.0),3)], ClienteRecord("Mario Rossi", "mariorossi@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0),1), RigaOrdine(ProdottoRecord("mouse", 70.0),3)], ClienteRecord("Fulvio Bianchi", "fulviobianchi@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0),1), RigaOrdine(ProdottoRecord("mouse", 70.0),3)], ClienteRecord("Giuseppe Averta", "giuseppeaverta@gmail.com", "Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0),1), RigaOrdine(ProdottoRecord("mouse", 70.0),3)], ClienteRecord("Giuseppe Averta", "giuseppeaverta@gmail.com", "Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0),1), RigaOrdine(ProdottoRecord("mouse", 70.0),3)], ClienteRecord("Giuseppe Averta", "giuseppeaverta@gmail.com", "Silver"))
    ]

    for o in ordini:
        sistema.addOrdine(o)

    sistema.processa_tutti_ordini()
    sistema.get_riepilogo()


if __name__ =="__main__":
    test_module()
