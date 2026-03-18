import flet as ft

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class Controller:

    def __init__(self, v):
        self._view = v


    def add_ordine(self, e):#e, è l'evento generato da quel pulsante
        #prodotto
        nomeP = self._view._txtInNomeP.value
        try:
              prezzoP= float(self._view._txtPrezzoP.value)
        except ValueError:
              self._view._lvOut.controls.append(ft.Text("Attenzione, il prezzo deve essere un numero", color ="red"))
              self._view.update_page()
              return
        try:
              quantitaP =int(self._view._txtQuantitaP.value)
        except ValueError:
              self._view._lvOut.controls.append(ft.Text("Attenzione, la quantita deve essere un numero", color ="red"))
              self._view.update_page()
              return

        #cliente
        nomeC = self._view._txtNomeC.value
        mail = self._view._txtMailP.value
        categoria = self._view._txtCategoriaP.value

    def crea_ordine(self, nomeP,prezzoP,quantitaP,nomeC, mail,categoria):
        return Ordine([RigaOrdine[(ProdottoRecord(nomeP,prezzoP),quantitaP)]],ClienteRecord(nomeC,mail,categoria))

    def gestisci_ordine(self):
        pass
    def gestisci_all_ordini(self):
        pass
    def stampa_sommari(self):
        pass