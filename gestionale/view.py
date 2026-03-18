

import flet as ft

class View:
    def __init__(self, page):
        self._page = page
        self._controller = None
        self._page.title =("Tdp 2025-software gestionale")
        self._page.horizontal_alignment = "CENTER"
        self._page.theme_mode = "light"
        self.update_page()

    def carica_interfaccia(self):
        #prodotto
        self._txtInNomeP = ft.TextField(label="Nome prodotto", width = 200)
        self._txtInPrezzo = ft.TextField(label="Prezzo",width = 200)
        self._txtInQuantita = ft.TextField(label="Quantita", width = 200)
        row1 = ft.Row(controls = [self._txtInNomeP, self._txtInPrezzo, self._txtInQuantita], alignment=ft.MainAxisAlignment.CENTER)

        #cliente
        self._txtInNomeC = ft.TextField(label="Nome Cliente", width = 200)
        self._txtInMail = ft.TextField(label="Mail", width = 200)
        self._txtInCategoria = ft.TextField(label="Categoria", width = 200)
        row2 = ft.Row(controls = [self._txtInNomeC, self._txtInMail], alignment=ft.MainAxisAlignment.CENTER)

        #bottone
        self._btnAdd = ft.ElevatedButton(text = "Aggiungi ordine", on_click = self._controller.add_ordine,
                                        width = 200)   #DOPO ONCLICK DEVI METTERE IL NOME DELLA FUNZIONE E NON LA CHIAMATA
        self._btnGestisciOrdine =  ft.ElevatedButton(text = "Gestisci prossimo ordine", on_click = self._controller.gestisci_ordine,
                                        width = 200)
        self._btnGestisciAllOrdini =  ft.ElevatedButton(text = "Gestisci tutti gli ordini", on_click = self._controller.gestisci_all_ordini,
                                        width = 200)
        self._btnStampaInfo =   ft.ElevatedButton(text = "Stampa sommario", on_click = self._controller.stampa_sommario,
                                        width = 200)

        row3 = ft.Row(controls = [self._btnAdd, self._btnGestisciOrdine, self._btnGestisciAllOrdini,self._btnStampaInfo])

        #lista di cose che verranno stampate
        self._lvOut = ft.ListView(expand = True)


        self._page.add_row(row1, row2, row3, self._lvOut)
        self.update_page()


    def set_controller(self,c):
        self._controller = c

    def update_page(self):
        self._page.update()